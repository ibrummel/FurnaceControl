import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QProxyStyle, QStyle
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QObject
from time import sleep
from src.ui.main_v2_ui import Ui_MainWindow
from Omega_Platinum import OmegaPlatinumControllerModbus
from datetime import datetime
from Signal_Thermocouple import SignalThermocouple


class FurnaceLogger(QDialog):
    # Done: Check that outputs are 1 indexed not 0 indexed.
    control_output = 3
    heat_init_temp = 140

    def __init__(self, comport: str, tcdevpath="Dev1/ai0"):
        super(FurnaceLogger, self).__init__()

        self.controller = OmegaPlatinumControllerModbus(comport)
        self.external_tc = SignalThermocouple('Ext_TC', tcdevpath)
        self.control_temp = None
        self.external_temp = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.profile_editor.set_parent(self)

        self.setup_plot_lines()

        self.heat_init_timer = QTimer()
        self.live_read_timer = QTimer()
        self.furnace_running_timer = QTimer()
        self.timer_log_interval = QTimer()
        self.log_interval_timeout = 10000
        self.log_file = r"C:\Users\Ian\Documents\Furnace Runs\default_temp_log.csv"
        self.data_thread = QThread()

        self.preheat_trims = [0., 3.00, 100., 3.00]
        self.trim_limits = [0., 0., 100., 5.]

        self.init_fields()
        self.init_connections()

    def init_fields(self):
        self.ui.combo_monitor_tc.addItems(list(self.external_tc.tc_types.keys()))
        self.ui.combo_controller_tc.addItems(['K', 'J', 'T', 'E', 'N', 'L', 'R', 'S', 'B', 'C'])
        self.update_fields()

    def update_fields(self):
        self.ui.combo_monitor_tc.setCurrentText(self.external_tc.get_tc_type())
        tc_type = self.controller.get_tc_type()
        if tc_type == '<Reserved>':
            raise ValueError('Received invalid enumeration of thermocouple type from furnace controller.')
        self.ui.combo_controller_tc.setCurrentText(tc_type)
        self.ui.line_log_interval.setText('{0:.1f}'.format(self.log_interval_timeout / 1000))
        self.ui.line_log_file.setText(self.log_file)
        self.set_logging_gbox()

    def init_connections(self):
        self.ui.combo_monitor_tc.currentTextChanged.connect(self.external_tc.set_tc_type)
        self.ui.combo_controller_tc.currentTextChanged.connect(self.set_controller_tc_type)
        self.ui.check_enable_logging.clicked.connect(self.set_logging_gbox)
        self.ui.line_log_interval.editingFinished.connect(self.set_log_interval)
        self.ui.line_log_file.editingFinished.connect(self.set_log_file_path_by_line)
        self.ui.btn_log_file.clicked.connect(self.set_log_file_path_by_dialog)
        self.ui.btn_logging_state.clicked.connect(self.set_logging_state)
        self.ui.btn_start_run.clicked.connect(self.handle_furnace_run)
        self.heat_init_timer.timeout.connect(self.check_heat_init)
        self.furnace_running_timer.timeout.connect(self.check_furnace_running)
        self.live_read_timer.timeout.connect(self.update_temps)
        self.live_read_timer.start(1500)
        self.timer_log_interval.timeout.connect(self.write_log)

    def set_logging_gbox(self):
        if self.ui.check_enable_logging.isChecked():
            self.ui.line_log_file.setDisabled(False)
            self.ui.btn_log_file.setDisabled(False)
            self.ui.line_log_interval.setDisabled(False)
        else:
            self.ui.line_log_file.setDisabled(True)
            self.ui.btn_log_file.setDisabled(True)
            self.ui.line_log_interval.setDisabled(True)

    def setup_plot_lines(self):
        # Add lines to the live plot widget
        self.ui.live_plot.canvas.add_line('Controller', {'color': '#0173b2', 'x': [], 'y': [], 'subplot_row': 0,
                                                         'subplot_col': 0})
        self.ui.live_plot.canvas.add_line('External', {'color': '#de8f05', 'x': [], 'y': [], 'subplot_row': 0,
                                                       'subplot_col': 0})

    def set_logging_state(self, startonly=False):
        if self.ui.btn_logging_state.text() == "Start Logging":
            self.ui.live_plot.clear_data()
            self.setup_plot_lines()

            self.check_log_file()
            if os.path.exists(self.log_file):
                raise UserWarning("Error deleting log file that already exists, new furnace run data will be appended.")
                mode = 'a'
            else:
                mode = 'w'

            with open(self.log_file, mode) as log_file:
                log_file.write("Furnace Run Notes:,{}".format(self.ui.text_log_notes.toPlainText()))
                log_file.write(
                    "\nTimestamp,Controller Temp,Controller TC Type, External Temp, External TC Type, Runstate\n")
            self.write_log()
            # Get the element tree with the profile information and write it to a modified version of the log file name
            profile_tree = self.ui.profile_editor.generate_profile_xml()
            profile_tree.write(self.log_file.replace(os.path.splitext(self.log_file)[1], "_profile_settings.xml"))

            self.ui.btn_logging_state.setText("Stop Logging")
            if not self.timer_log_interval.isActive():
                self.timer_log_interval.start(int(self.log_interval_timeout))
                print('Log interval timer started. Timer isActive: {}'.format(self.timer_log_interval.isActive()))
        elif self.ui.btn_logging_state.text() == "Stop Logging" and not startonly:
            self.ui.btn_logging_state.setText("Start Logging")
            if self.timer_log_interval.isActive():
                self.timer_log_interval.stop()
                print('Log interval timer stopped. Timer isActive: {}'.format(self.timer_log_interval.isActive()))

    def check_log_file(self):
        if os.path.isfile(self.log_file):
            overwrite = QMessageBox.warning(self, 'File already exists',
                                            'This log file already exists. Would you like to overwrite?',
                                            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                            QMessageBox.No)
            if overwrite == QMessageBox.Yes:
                os.remove(self.log_file)
            elif overwrite == QMessageBox.No:
                self.set_log_file_path_by_dialog()
            elif overwrite == QMessageBox.Cancel:
                return
        elif self.log_file == os.path.join(os.getenv('USERPROFILE'), 'Desktop') or self.log_file == '':
            no_file_selected = QMessageBox.warning(self, 'No File Selected',
                                                   'No file has been selected for writing log data, '
                                                   'please pick a file to save to.',
                                                   QMessageBox.Ok | QMessageBox.Cancel,
                                                   QMessageBox.Ok)
            if no_file_selected == QMessageBox.Ok:
                self.set_log_file_path_by_dialog()
                self.start_measurement()
            elif no_file_selected == QMessageBox.Cancel:
                return
            # Done: maybe add more file save path checking i.e. blank or default location.

    def set_log_file_path_by_dialog(self):
        file_name = QFileDialog.getSaveFileName(self,
                                                'Select a file to save data...',
                                                self.log_file,
                                                "CSV Files (*.csv);;xyz Files (*.xyz);;All Types (*.*)",
                                                options=QFileDialog.DontConfirmOverwrite)
        self.log_file = file_name[0]
        if not os.path.exists(os.path.dirname(os.path.abspath(self.log_file))):
            try:
                os.mkdir(os.path.dirname(os.path.abspath(self.log_file)))
            except PermissionError:
                permission_denied = QMessageBox.warning(self, 'Permission Denied',
                                                        'Permission to create the specified folder was denied. \
                                                        Please pick another location to save your data',
                                                        QMessageBox.OK, QMessageBox.Ok)
                if permission_denied == QMessageBox.Ok:
                    self.set_save_file_path_by_dialog()

        self.ui.line_log_file.setText(self.log_file)

    def set_log_file_path_by_line(self):
        if self.ui.line_log_file.text() != '':
            self.log_file = self.ui.line_log_file.text()

    def set_log_interval(self):
        interval = float(self.ui.line_log_interval.text()) * 1000
        self.log_interval_timeout = interval
        if self.timer_log_interval.isActive():
            self.timer_log_interval.setInterval(self.log_interval_timeout)

    def update_temps(self):
        ext_temp = self.external_tc.read_temp()
        ctrl_temp = self.controller.get_process_temp()

        self.ui.lbl_external_temp.setText("{:.2f} C".format(ext_temp))
        self.ui.lbl_controller_temp.setText("{:.2f} C".format(ctrl_temp))

        self.control_temp = ctrl_temp
        self.external_temp = ext_temp
        return ext_temp, ctrl_temp

    def write_log(self):
        ext_temp, ctrl_temp = self.update_temps()
        with open(self.log_file, 'a') as logfile:
            tstamp = datetime.now()
            t_str = tstamp.strftime('%Y-%m-%d %H:%M:%S')
            ctrl_tc = self.controller.get_tc_type()
            ext_tc = self.external_tc.get_tc_type()
            runstate = self.controller.get_system_state()
            logfile.write('{timestamp},{ctrl_temp},{ctrl_tc},{ext_temp},{ext_tc},{runstate}\n'.format(timestamp=t_str,
                                                                                                      ctrl_temp=ctrl_temp,
                                                                                                      ctrl_tc=ctrl_tc,
                                                                                                      ext_temp=ext_temp,
                                                                                                      ext_tc=ext_tc,
                                                                                                      runstate=runstate))
        self.ui.live_plot.add_data('Controller', [tstamp, ctrl_temp])
        self.ui.live_plot.add_data('External', [tstamp, ext_temp])

    def set_controller_tc_type(self, tc_type):
        self.controller.set_tc_type(tc_type)

    # ToDo: Add output setup functionality to the manual control widget/window
    # def set_output_mode(self, output_mode: str):
    #     self.controller.set_output_mode(self.control_output, output_mode)
    #     if output_mode != 'Retransmission':
    #         # Reset output trims on controller, preserve values in GUI
    #         # self.controller.set_retransmission_trim(self.control_output, 0, 0, 100, 1)
    #         self.ui.gbox_trim_setup.setDisabled(True)
    #     else:
    #         # Set output trims as they are entered in the GUI -> return to last user state
    #         self.set_output_trim()
    #         self.ui.gbox_trim_setup.setDisabled(False)

    # def set_output_trim(self):
    #     # DONE 23 March 2022: Add limits to retrans values as appropriate
    #     # Check the input values, if not valid reset with current values from controller
    #     readings = [float(self.ui.line_trim_reading1.text()), float(self.ui.line_trim_reading2.text())]
    #     outputs = [float(self.ui.line_trim_output1.text()), float(self.ui.line_trim_output2.text())]
    #
    #     valid = True
    #     try:
    #         for val in readings:
    #             if self.trim_limits[0] <= val <= self.trim_limits[2]:
    #                 pass
    #             else:
    #                 valid = False
    #                 break
    #         for val in outputs:
    #             if self.trim_limits[1] <= val <= self.trim_limits[3]:
    #                 pass
    #             else:
    #                 valid = False
    #                 break
    #     except TypeError:
    #         valid = False
    #
    #     if valid:  # All valid send updated values to controller
    #         # ToDo: Add a messagebox allowing the user to set both trims equal automatically to avoid the output floating without control.
    #         self.controller.set_retransmission_trim(self.control_output, readings[0], outputs[0], readings[1],
    #                                                 outputs[1])
    #     else:
    #         print("Received invalid trim values. Resetting to controller values")
    #
    #     self.update_fields()

    def set_selected_profile(self, profile_num):
        self.controller.set_current_profile_number(profile_num)
        self.ui.profile_editor.ui.spin_profile_num.setValue(profile_num)

    def get_selected_profile(self, ):
        return int(self.controller.get_current_edit_profile_number())

    def set_profile_tracking_mode(self, tracking_mode):
        self.controller.set_ramp_soak_tracking_mode(tracking_mode)

    def handle_furnace_run(self):
        if self.ui.btn_start_run.text() == "Start Furnace Run":
            self.disable_controls(True)
            # Set up for constant load heating + change ui elements to reflect changes
            self.ui.btn_start_run.setText("Stop Furnace")
            self.ui.live_plot.clear_data()
            self.ui.combo_controller_tc.setCurrentText("S")
            self.controller.set_tc_type("S")
            self.controller.set_output_mode(self.control_output, 'Retransmission')
            self.controller.set_retransmission_trim(output_num=self.control_output, reading1=self.preheat_trims[0],
                                                    output1=self.preheat_trims[1],
                                                    reading2=self.preheat_trims[2], output2=self.preheat_trims[3])
            # Start the controller for constant load heating
            self.controller.set_system_state("Run")
            # Start checking every 5 seconds if the external TC reads >=120C to switch over TC type and start normal
            #  operations
            self.heat_init_timer.start(5000)
            if self.ui.check_enable_logging.isChecked() and not self.timer_log_interval.isActive():
                # DONE: Save the settings for the profile to an XML on start of furnace run
                self.check_log_file()
                self.set_logging_state(startonly=True)
            self.furnace_running_timer.start(5000)
        elif self.ui.btn_start_run.text() == 'Stop Furnace':
            self.ui.btn_start_run.setText("Start Furnace Run")
            self.controller.set_system_state("Idle")
            self.disable_controls(False)
            if self.heat_init_timer.isActive():
                self.heat_init_timer.stop()
            if self.timer_log_interval.isActive():
                self.timer_log_interval.stop()
            if self.furnace_running_timer.isActive():
                self.furnace_running_timer.stop()

    def check_heat_init(self):
        # Read temperature from the external T/C
        ext_temp = self.external_tc.read_temp()
        print("Got {} degC from external thermocouple".format(ext_temp), end='\r')

        if ext_temp >= self.heat_init_temp:
            # Stop heating and set controller to TC Mode=B
            print("Stopped heating to change TC Mode")
            self.heat_init_timer.stop()
            self.controller.set_system_state("Idle")
            self.ui.combo_controller_tc.setCurrentText("B")
            self.controller.set_tc_type("B")
            print("Set TC mode to B type")
            sleep(5)
            # Check to make sure that the B type TC reads
            print("Reading system state...")
            state = self.controller.get_system_state()
            print("Got system state: {}".format(state))
            if state in ['Fault']:
                print("System fault state, continuing heating")
                # if the controller goes to fault mode, add a few degrees to the cut off temp and then retry heating.
                self.heat_init_temp += 10
                self.heat_init_timer.start()
                # return self.handle_furnace_run()
            else:
                # Otherwise set retransmission off, change to PID, and restart the program
                print("Clearing trim and setting PID output")
                self.controller.set_retransmission_trim(output_num=self.control_output, reading1=0., output1=0.,
                                                        reading2=100., output2=1.)
                self.controller.set_output_mode(self.control_output, "PID")

            self.controller.set_system_state("Run")

    def check_furnace_running(self):
        runstate = self.controller.get_system_state()
        if runstate == 'Wait' and self.control_temp < 110:
            if self.controller.get_tc_type() != "S":
                self.ui.combo_controller_tc.setCurrentText("S")
                self.controller.set_tc_type("S")
            if self.external_temp < 50:
                if self.timer_log_interval.isActive():
                    print("Stopped logging...")
                    self.timer_log_interval.stop()
                    self.ui.btn_logging_state.setText("Start Logging")
                print("Setting controller state to Idle.")
                self.controller.set_system_state("Idle")
        elif runstate not in ['Idle']:
            return
        else:
            self.ui.btn_start_run.setText("Start Furnace Run")
            self.disable_controls(False)
            self.furnace_running_timer.stop()

    def disable_controls(self, state):
        self.ui.gbox_profile_setup.setDisabled(state)

        # ToDo: Add input masking or input checking to all functions to avoid crashes from being a fuckup at typing
        # ToDo: Add functionality to allow saving of arbitrary values to log
        # ToDo: Add tool that allows setting/reading arbitrary values from controller using register list
        # ToDo: Restructure UI to be just for auto running with popout window for more manual control
        # Done 05 April 2023: Make the box that selects profiles wait until editing is finished to pull profile
        # ToDo: Add button to mpl toolbar to manage data plotting see here:
        #  https://matplotlib.org/3.1.1/gallery/user_interfaces/toolmanager_sgskip.html
        #  https://stackoverflow.com/questions/12695678/how-to-modify-the-navigation-toolbar-easily-in-a-matplotlib-figure-window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FurnaceLogger('COM3')
    window.show()
    sys.exit(app.exec_())
