import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QDialog, QWidget, QLineEdit, QCheckBox, \
    QGroupBox, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QRegExp, QObject
import Omega_Platinum_Enum as ENUM
from PyDAQmx import (Task, InvalidAttributeValueError, DAQmx_Val_DegC, DAQmx_Val_J_Type_TC,
                     DAQmx_Val_K_Type_TC, DAQmx_Val_T_Type_TC, DAQmx_Val_E_Type_TC,
                     DAQmx_Val_N_Type_TC, DAQmx_Val_R_Type_TC, DAQmx_Val_S_Type_TC,
                     DAQmx_Val_B_Type_TC, DAQmx_Val_GroupByChannel, DAQmx_Val_BuiltIn)
from PyDAQmx.DAQmxTypes import byref, int32
from time import sleep
import numpy as np
from src.ui.main_ui import Ui_MainWindow
from src.ui.profile_settings_ui import Ui_ProfileSettingsDialog
import sys
import xml.etree.ElementTree as ET
from Omega_Platinum import OmegaPlatinumControllerModbus
from datetime import timedelta, datetime


# Regenerate python ui file on run for testing
# import os
# os.system("pyuic5 -o src/ui/main_ui.py src/ui/main.ui")
# os.system("pyuic5 -o src/ui/profile_settings_ui.py src/ui/profile_settings.ui")

class SignalThermocouple(QObject):
    ext_temp_ready = pyqtSignal(float)

    def __init__(self, task_name: str, tcdevpath: str, tc_chan_name='tc', min_val=-50, max_val=1768,
                 units=DAQmx_Val_DegC, tc_type=DAQmx_Val_S_Type_TC, cjc_source=DAQmx_Val_BuiltIn,
                 cjc_val=0, cjc_channel=0):
        super(SignalThermocouple, self).__init__()
        # Dictionaries to act as a translation layer for TC types
        self.tc_types_rev = {10072: 'J',
                             10073: 'K',
                             10086: 'T',
                             10055: 'E',
                             10077: 'N',
                             10082: 'R',
                             10085: 'S',
                             10047: 'B'}
        self.tc_types = {'J': DAQmx_Val_J_Type_TC,
                         'K': DAQmx_Val_K_Type_TC,
                         'T': DAQmx_Val_T_Type_TC,
                         'E': DAQmx_Val_E_Type_TC,
                         'N': DAQmx_Val_N_Type_TC,
                         'R': DAQmx_Val_R_Type_TC,
                         'S': DAQmx_Val_S_Type_TC,
                         'B': DAQmx_Val_B_Type_TC,
                         }
        # Create task to hold tc read channel
        self.tc = Task(task_name)
        # Create channel that reads tc value
        self.tc_chan_name = tc_chan_name
        self.tc.CreateAIThrmcplChan(tcdevpath, tc_chan_name, min_val, max_val, units, tc_type,
                                    cjc_source, cjc_val, cjc_channel)
        # Create an integer value that will be used to read the temp
        self.temp = int32()
        # Create a 1D, single-point array to hold the last read temp value
        self.data = np.zeros((1,), dtype=np.float64)

    def read_temp(self):
        self.tc.ReadAnalogF64(1, 0.5, DAQmx_Val_GroupByChannel, self.data, 1,
                              byref(self.temp), None)
        self.ext_temp_ready.emit(self.data[0])
        return float(self.data[0])

    def set_tc_type(self, tc_type):
        # if the function gets a string convert it to the matching, enumerated value (int)
        if isinstance(tc_type, str):
            tc_type = self.tc_types[tc_type]

        try:
            ret = self.tc.SetAIThrmcplType(self.tc_chan_name, tc_type)
        except InvalidAttributeValueError:
            ret = -1
            print("Tried to set external thermocouple to invalid type. Reverting...")
        return ret

    def get_tc_type(self):
        ret = int32()
        self.tc.GetAIThrmcplType(self.tc_chan_name, byref(ret))

        return self.tc_types_rev[ret.value]


class FurnaceLogger(QDialog):
    control_output = 3
    heat_init_temp = 120
    profile_number_changed = pyqtSignal(int)

    def __init__(self, comport: str, tcdevpath="Dev1/ai0"):
        super(FurnaceLogger, self).__init__()

        self.controller = OmegaPlatinumControllerModbus(comport)

        self.external_tc = SignalThermocouple('Ext_TC', tcdevpath)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.profile_editor = ProfileSettingsForm(parent=self)
        self.heat_init_timer = QTimer()
        self.live_read_timer = QTimer()
        self.furnace_running_timer = QTimer()
        self.timer_log_interval = QTimer()
        self.log_interval_timeout = 10000
        self.log_file = r"C:\Users\Ian\Documents\Furnace Runs\default_temp_log.csv"
        self.data_thread = QThread()

        self.init_fields()
        self.init_connections()

    def init_fields(self):
        self.ui.combo_monitor_tc.addItems(list(self.external_tc.tc_types.keys()))
        self.ui.combo_controller_tc.addItems(['K', 'J', 'T', 'E', 'N', 'L', 'R', 'S', 'B', 'C'])
        self.ui.combo_output_mode.addItems(list(ENUM.Write.output_mode.keys()))
        self.ui.spin_profile_number.setRange(1, 99)
        self.ui.combo_profile_tracking.addItems(list(ENUM.Write.ramp_soak_tracking.keys()))
        self.update_fields()

    def update_fields(self):
        self.ui.combo_monitor_tc.setCurrentText(self.external_tc.get_tc_type())
        tc_type = self.controller.get_tc_type()
        if tc_type == '<Reserved>':
            raise ValueError('Received invalid enumeration of thermocouple type from furnace controller.')
        self.ui.combo_controller_tc.setCurrentText(tc_type)
        self.ui.line_log_interval.setText(str(self.log_interval_timeout / 1000))
        self.ui.line_log_file.setText(self.log_file)
        self.set_logging_gbox()
        self.ui.combo_output_mode.setCurrentText(self.controller.get_output_mode(self.control_output))
        trims = self.controller.get_retransmission_trim(self.control_output)
        self.ui.line_trim_reading1.setText(str(trims[0]))
        self.ui.line_trim_output1.setText(str(trims[1]))
        self.ui.line_trim_reading2.setText(str(trims[2]))
        self.ui.line_trim_output2.setText(str(trims[3]))
        if self.ui.combo_output_mode.currentText() != 'Retransmission':
            self.ui.gbox_trim_setup.setDisabled(True)
        self.ui.spin_profile_number.setValue(self.controller.get_current_edit_profile_number())
        self.controller.set_current_profile_number(self.ui.spin_profile_number.value())
        self.ui.combo_profile_tracking.setCurrentText(self.controller.get_ramp_soak_tracking_mode())

    def init_connections(self):
        self.ui.combo_monitor_tc.currentTextChanged.connect(self.external_tc.set_tc_type)
        self.ui.combo_controller_tc.currentTextChanged.connect(self.set_controller_tc_type)
        self.ui.check_enable_logging.clicked.connect(self.set_logging_gbox)
        self.ui.line_log_interval.editingFinished.connect(self.set_log_interval)
        self.ui.line_log_file.editingFinished.connect(self.set_log_file_path_by_line)
        self.ui.btn_log_file.clicked.connect(self.set_log_file_path_by_dialog)
        self.ui.btn_logging_state.clicked.connect(self.set_logging_state)
        self.ui.combo_output_mode.currentTextChanged.connect(self.set_output_mode)
        self.ui.line_trim_reading1.editingFinished.connect(self.set_output_trim)
        self.ui.line_trim_reading2.editingFinished.connect(self.set_output_trim)
        self.ui.line_trim_output1.editingFinished.connect(self.set_output_trim)
        self.ui.line_trim_output2.editingFinished.connect(self.set_output_trim)
        self.ui.spin_profile_number.valueChanged.connect(self.set_selected_profile)
        self.ui.combo_profile_tracking.currentTextChanged.connect(self.controller.set_ramp_soak_tracking_mode)
        self.ui.btn_edit_profile.clicked.connect(self.profile_editor.show)
        self.profile_editor.profile_num_signal.connect(self.ui.spin_profile_number.setValue)
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

    def set_logging_state(self, startonly=False):
        if self.ui.btn_logging_state.text() == "Start Logging":
            self.check_log_file()
            if os.path.exists(self.log_file):
                raise UserWarning("Error deleting log file that already exists, new furnace run data will be appended.")
                mode = 'a'
            else:
                mode = 'w'

            with open(self.log_file, mode) as log_file:
                log_file.write("Furnace Run Notes:,{}".format(self.ui.text_log_notes.toPlainText()))
                log_file.write("\nTimestamp,Controller Temp,External Temp\n")
            # Get the element tree with the profile information and write it to a modified version of the log file name
            profile_tree = self.profile_editor.generate_profile_xml()
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
            # Fixme: maybe add more file save path checking i.e. blank or default location.

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
        self.ui.lbl_external_temp.setText("{:.2f} C".format(self.external_tc.read_temp()))
        self.ui.lbl_controller_temp.setText("{:.2f} C".format(self.controller.get_process_temp()))

    def write_log(self):
        # print("Opening {} to write log entry".format(self.log_file))

        with open(self.log_file, 'a') as logfile:
            ext_temp = self.external_tc.read_temp()
            ctrl_temp = self.controller.get_process_temp()
            timestamp = datetime.now()
            logfile.write('{timestamp},{ctrl_temp},{ext_temp}\n'.format(timestamp=timestamp.__str__(),
                                                                        ctrl_temp=ctrl_temp, ext_temp=ext_temp))

        self.update_temps()

    def set_controller_tc_type(self, tc_type):
        self.controller.set_tc_type(tc_type)

    def set_output_mode(self, output_mode: str):
        self.controller.set_output_mode(self.control_output, output_mode)
        if output_mode != 'Retransmission':
            # Reset output trims on controller, preserve values in GUI
            # self.controller.set_retransmission_trim(self.control_output, 0, 0, 100, 1)
            self.ui.gbox_trim_setup.setDisabled(True)
        else:
            # Set output trims as they are entered in the GUI -> return to last user state
            self.set_output_trim()
            self.ui.gbox_trim_setup.setDisabled(False)

    def set_output_trim(self):
        self.controller.set_retransmission_trim(self.control_output, float(self.ui.line_trim_reading1.text()),
                                                float(self.ui.line_trim_output1.text()),
                                                float(self.ui.line_trim_reading2.text()),
                                                float(self.ui.line_trim_output2.text()))

    def set_selected_profile(self, profile_num):
        self.controller.set_current_profile_number(profile_num)
        self.ui.combo_profile_tracking.setCurrentText(self.controller.get_ramp_soak_tracking_mode())
        self.profile_number_changed.emit(profile_num)

    def get_selected_profile(self, ):
        return int(self.controller.get_current_edit_profile_number())

    def set_profile_tracking_mode(self, tracking_mode):
        self.controller.set_ramp_soak_tracking_mode(tracking_mode)

    def handle_furnace_run(self):
        if self.ui.btn_start_run.text() == "Start Furnace Run":
            self.disable_controls(True)
            # Set up for constant load heating + change ui elements to reflect changes
            self.ui.btn_start_run.setText("Stop Furnace")
            self.ui.combo_controller_tc.setCurrentText("S")
            self.controller.set_tc_type("S")
            self.ui.combo_output_mode.setCurrentText('Retransmission')
            self.controller.set_output_mode(self.control_output, 'Retransmission')
            self.ui.line_trim_reading1.setText('0')
            self.ui.line_trim_output1.setText('10')
            self.ui.line_trim_reading2.setText('100')
            self.ui.line_trim_output2.setText('1')
            self.controller.set_retransmission_trim(0, 10, 100, 1)
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
                self.ui.line_trim_reading1.setText('0')
                self.ui.line_trim_output1.setText('0')
                self.ui.line_trim_reading2.setText('100')
                self.ui.line_trim_output2.setText('1')
                self.controller.set_retransmission_trim(0, 0, 100, 1)
                self.ui.combo_output_mode.setCurrentText('PID')
                self.controller.set_output_mode(self.control_output, "PID")

            self.controller.set_system_state("Run")
            print("Set controller state to run")

            # DONE:
            #  -> Disable all controls except stop and edit profile -- check
            #  -> Set Controller TC=S -- check
            #  -> Set retrans mode with 0->10, 100->1 trim -- check (long term make this self adjust to be ~5C/min)
            #  -> Start heating -- check
            #  -> Monitor for ~105-110C then -- check
            #  -> Switch to TC=B, set output to PID, restart run -- check

    def check_furnace_running(self):
        runstate = self.controller.get_system_state()
        if runstate not in ['Idle']:
            return
        else:
            self.ui.btn_start_run.setText("Start Furnace Run")
            self.disable_controls(False)
            self.furnace_running_timer.stop()

    def disable_controls(self, state):
        self.ui.gbox_temp.setDisabled(state)
        self.ui.gbox_output.setDisabled(state)
        self.ui.gbox_profile.setDisabled(state)

        # FixMe: Add input masking or input checking to all functions to avoid crashes from being a fuckup at typing
        # ToDo: Add limits to retrans values as appropriate
        # FIXME: Check that outputs are 1 indexed not 0 indexed.
        # ToDo: Add button to mpl toolbar to manage data plotting see here:
        #  https://matplotlib.org/3.1.1/gallery/user_interfaces/toolmanager_sgskip.html
        #  https://stackoverflow.com/questions/12695678/how-to-modify-the-navigation-toolbar-easily-in-a-matplotlib-figure-window

    # FIXME: Add plotting capability


class ProfileSettingsForm(QWidget):
    profile_num_signal = pyqtSignal(int)
    current_profile = {
        'number': 1, 'trackingMode': '', 'numSegments': 0, 'linkAction': '', 'linkProfile': 0, 'edited': False,
        1: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        2: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        3: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        4: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        5: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        6: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        7: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        8: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
    }

    def __init__(self, parent: FurnaceLogger):
        self.parent = parent
        self.controller = parent.controller
        super(ProfileSettingsForm, self).__init__()

        self.ui = Ui_ProfileSettingsDialog()
        self.ui.setupUi(self)

        # Define dicts for setpoint, ramp event, ramp time, soak event, and soak time
        #  controls for easier setting with for loops
        self.setpoint_lines = {int(widget.objectName().split("_")[-1]): widget
                               for widget in self.findChildren(QLineEdit, QRegExp("line_stpt_*"))}
        self.ramp_event_checks = {int(widget.objectName().split("_")[-1]): widget
                                  for widget in self.findChildren(QCheckBox, QRegExp("check_ramp_*"))}
        self.ramp_time_lines = {int(widget.objectName().split("_")[-1]): widget
                                for widget in self.findChildren(QLineEdit, QRegExp("line_ramp_*"))}
        self.dwell_event_checks = {int(widget.objectName().split("_")[-1]): widget
                                   for widget in self.findChildren(QCheckBox, QRegExp("check_dwell_*"))}
        self.dwell_time_lines = {int(widget.objectName().split("_")[-1]): widget
                                 for widget in self.findChildren(QLineEdit, QRegExp("line_dwell_*"))}
        self.segment_gboxes = {int(widget.objectName().split("_")[-1]): widget
                               for widget in self.findChildren(QGroupBox, QRegExp("gbox_segment_*"))}

        self.init_fields()
        self.init_connections()

        self.read_profile(self.parent.controller.get_current_edit_profile_number())

    def init_fields(self):
        self.ui.spin_profile_num.setRange(1, 99)
        self.ui.combo_tracking_mode.addItems(list(ENUM.Write.ramp_soak_tracking.keys()))
        self.ui.spin_num_segments.setRange(1, 8)
        self.ui.combo_link_action.addItems(list(ENUM.Write.ramp_soak_link_action.keys()))
        self.ui.spin_link_to.setRange(0, 99)

    def init_connections(self):
        self.ui.spin_profile_num.valueChanged.connect(self.change_profile)
        self.ui.combo_tracking_mode.currentTextChanged.connect(self.update_tracking_mode)
        self.ui.spin_num_segments.valueChanged.connect(self.update_num_segments)
        self.ui.combo_link_action.currentTextChanged.connect(self.update_link_action)
        self.ui.spin_link_to.valueChanged.connect(self.update_link_profile)
        for key, widget in self.setpoint_lines.items():
            widget.editingFinished.connect(self.read_segment_fields)
        for key, widget in self.ramp_event_checks.items():
            widget.clicked.connect(self.read_segment_fields)
        for key, widget in self.ramp_time_lines.items():
            widget.editingFinished.connect(self.read_segment_fields)
        for key, widget in self.dwell_event_checks.items():
            widget.clicked.connect(self.read_segment_fields)
        for key, widget in self.dwell_time_lines.items():
            widget.editingFinished.connect(self.read_segment_fields)
        self.parent.profile_number_changed.connect(self.read_profile)
        self.ui.btn_ok.clicked.connect(self.ok)
        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_refresh_profile.clicked.connect(lambda: self.read_profile(self.ui.spin_profile_num.value()))

    def ok(self):
        self.write_profile()
        self.close()

    def apply(self):
        self.write_profile()

    def cancel(self):
        self.read_profile(self.ui.spin_profile_num.value())
        self.close()

    def close(self):
        self.profile_num_signal.emit(self.current_profile['number'])
        super(ProfileSettingsForm, self).close()

    def generate_profile_xml(self):
        root = ET.Element('PlatinumProfileGroup')
        root.append(self._profile_xml(self.current_profile, sequence=1))

        # Save profile number to execute so we can go back to it later.
        if self.current_profile['linkAction'] == 'Link':
            execute_profile = self.current_profile['number']

            # Cycle through linked profiles, adding 1 to their sequence value and appending them to
            #  the root element
            sequence = 1
            while self.current_profile['linkAction'] == 'Link':
                sequence += 1
                self.read_profile(self.current_profile['linkProfile'])
                root.append(self._profile_xml(self.current_profile, sequence=sequence))

            self.read_profile(execute_profile)

        return ET.ElementTree(root)

    @staticmethod
    def _profile_xml(profile: dict, sequence: int):
        profile_xml = ET.Element("PlatinumProfile")
        for key, item in profile.items():
            if isinstance(item, dict):
                element = ET.SubElement(profile_xml, 'ProfileSegment')
                element.set('segmentNum', str(key))
                element.set('active', str(item['active']))
                element.set('ramp', str(item['ramp']))
                element.set('soak', str(item['soak']))
                element.set('rTime', str(item['rTime']))
                element.set('sTime', str(item['sTime']))
                element.set('setpoint', str(item['setpoint']))

        profile_xml.set('number', str(profile['number']))
        profile_xml.set('sequence', str(sequence))
        profile_xml.set('trackingMode', str(profile['trackingMode']))
        profile_xml.set('numSegments', str(profile['numSegments']))
        profile_xml.set('linkAction', str(profile['linkAction']))
        profile_xml.set('linkProfile', str(profile['linkProfile']))

        return profile_xml

    def load_xml_profile(self):
        # FIXME: Write loader for xml files to load profiles (including linked) back into the controller.
        pass

    def read_profile(self, profile: int):
        self.current_profile['number'] = profile
        self.parent.controller.set_current_profile_number(profile)
        self.current_profile.update(self.controller.read_profile_info())
        for i in range(1, 9):  # Note 1-9 because range does not include last value
            self.controller.set_current_segment_number(i)
            self.current_profile[i] = dict(
                active=(True if i <= self.current_profile['numSegments'] else False), )
            self.current_profile[i].update(self.controller.read_full_segment())
        self.current_profile['edited'] = False
        self.update_fields()

    def read_segment_fields(self):
        for i in range(1, self.current_profile['numSegments'] + 1):
            fixed_ramp_time = self.handle_time_input(self.ramp_time_lines[i].text())
            if fixed_ramp_time is not None:
                self.ramp_time_lines[i].setText(fixed_ramp_time)
            else:
                self.ramp_time_lines[i].setText(self.convert_msec_to_time(self.current_profile[i]['rTime']))

            fixed_dwell_time = self.handle_time_input(self.dwell_time_lines[i].text())
            if fixed_dwell_time is not None:
                self.dwell_time_lines[i].setText(fixed_dwell_time)
            else:
                self.dwell_time_lines[i].setText(self.convert_msec_to_time(self.current_profile[i]['dTime']))

            new_segment = {
                'active': True,
                'ramp': self.ramp_event_checks[i].isChecked(),
                'soak': self.dwell_event_checks[i].isChecked(),
                'rTime': self.convert_time_to_msec(self.ramp_time_lines[i].text()),
                'sTime': self.convert_time_to_msec(self.dwell_time_lines[i].text()),
                'setpoint': float(self.setpoint_lines[i].text())
            }
            self.current_profile[i] = new_segment

    def change_profile(self, profile_num: int):
        # Fixme: check for changes to save before reading new profile
        # if self.current_profile['edited']:
        #     QMessageBox
        self.read_profile(profile_num)

    def update_tracking_mode(self, tracking_mode: str):
        self.controller.set_ramp_soak_tracking_mode(tracking_mode)
        self.current_profile['trackingMode'] = tracking_mode
        sleep(0.1)
        self.update_fields()

    def update_num_segments(self, num_segments: int):
        self.controller.set_segments_per_profile(num_segments)
        self.current_profile['numSegments'] = num_segments
        sleep(0.1)
        self.update_fields()

    def update_link_action(self, link_action: str):
        self.controller.set_link_action(link_action)
        self.current_profile['linkAction'] = link_action
        sleep(0.1)
        self.update_fields()

    def update_link_profile(self, link_profile: int):
        self.controller.set_link_profile(link_profile)
        self.current_profile['linkProfile'] = link_profile
        sleep(0.1)
        self.update_fields()

    def update_fields(self):
        self.ui.spin_profile_num.setValue(self.current_profile['number'])
        self.ui.combo_tracking_mode.setCurrentText(self.current_profile['trackingMode'])
        self.ui.spin_num_segments.setValue(self.current_profile['numSegments'])
        self.ui.combo_link_action.setCurrentText(self.current_profile['linkAction'])
        self.ui.spin_link_to.setValue(self.current_profile['linkProfile'])

        for i in range(1, 9):
            segment = self.current_profile[i]
            self.segment_gboxes[i].setEnabled(segment['active'])
            self.setpoint_lines[i].setText('{:.1f}'.format(segment['setpoint']))
            self.ramp_event_checks[i].setChecked(segment['ramp'])
            self.ramp_time_lines[i].setText(self.convert_msec_to_time(segment['rTime']))
            self.dwell_event_checks[i].setChecked(segment['soak'])
            self.dwell_time_lines[i].setText(self.convert_msec_to_time(segment['sTime']))

    def write_profile(self):
        self.controller.set_current_profile_number(self.current_profile['number'])
        self.controller.write_profile_info(numSegments=self.current_profile['numSegments'],
                                           linkAction=self.current_profile['linkAction'],
                                           linkProfile=self.current_profile['linkProfile'],
                                           trackingMode=self.current_profile['trackingMode'])
        for i in range(1, 9):  # Note 1-9 because range does not include last value
            self.controller.set_current_segment_number(i)
            if self.current_profile[i]['active']:
                self.controller.write_full_segment(ramp=self.current_profile[i]['ramp'],
                                                   soak=self.current_profile[i]['soak'],
                                                   rTime=self.current_profile[i]['rTime'],
                                                   sTime=self.current_profile[i]['sTime'],
                                                   setpoint=self.current_profile[i]['setpoint'])
        self.current_profile['edited'] = False
        self.read_profile(self.current_profile['number'])

    @staticmethod
    def handle_time_input(time_input: str):
        try:
            hours, minutes, seconds = time_input.split(':')
        except ValueError:
            return None

        try:
            hours = int(hours)
        except ValueError:
            if hours == '':
                hours = 0
            else:
                return None
        try:
            minutes = int(minutes)
        except ValueError:
            if minutes == '':
                minutes = 0
            else:
                return None
        try:
            seconds = int(seconds)
        except ValueError:
            if seconds == '':
                seconds = 0
            else:
                return None

        return timedelta(hours=hours, minutes=minutes, seconds=seconds).__str__()

    @staticmethod
    def convert_time_to_msec(time_str: str):
        hours, minutes, seconds = time_str.split(':')
        # Note: No exception checking here. I want this to fail if it gets passed an invalid time string.
        #  This should prevent sending junk data to the controller.
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        return int(timedelta(hours=hours, minutes=minutes, seconds=seconds).seconds * 1000)

    @staticmethod
    def convert_msec_to_time(msec: int):
        return timedelta(milliseconds=msec).__str__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FurnaceLogger('COM3')
    window.show()
    sys.exit(app.exec_())
