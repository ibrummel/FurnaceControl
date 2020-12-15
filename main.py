from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QDialog
from PyQt5.QtCore import QThread, pyqtSignal
import Omega_Platinum_Enum as ENUM
import nidaqmx
import numpy as np
import sys
from Omega_Platinum import OmegaPlatinumControllerModbus

class SignalTask(nidaqmx.Task):
    read_ready = pyqtSignal()
    def __init__(self):
        super().__init__()

    def read(self, number_of_samples_per_channel=nidaqmx.task.NUM_SAMPLES_UNSET,
             timeout=10.0):

        data = super().read(number_of_samples_per_channel, timeout)
        self.read_ready.emit(data)
        return data


class FurnaceLogger(QDialog):
    def __init__(self, comport: str, tcdevpath="Dev1/ai0"):
        super().__init__()

        self.controller = OmegaPlatinumControllerModbus(comport)

        self.tc_types = {'J': nidaqmx.constants.ThermocoupleType.J,
                         'K': nidaqmx.constants.ThermocoupleType.K,
                         'T': nidaqmx.constants.ThermocoupleType.T,
                         'E': nidaqmx.constants.ThermocoupleType.E,
                         'N': nidaqmx.constants.ThermocoupleType.N,
                         'R': nidaqmx.constants.ThermocoupleType.R,
                         'S': nidaqmx.constants.ThermocoupleType.S,
                         'B': nidaqmx.constants.ThermocoupleType.B,
                         # 'C': nidaqmx.constants.ThermocoupleType.C,
                         }

        self.external_tc = self.init_external_tc(tcdevpath)

        self.ui = uic.loadUi("./src/ui/main.ui", self)

        self.data_thread = QThread()

        # FIXME: Uncomment these while writing code, provides useful intellisense,
        #  but will break the actual UI if left uncommented on run. 
        # self.combo_monitor_tc = QComboBox()
        # self.combo_controller_tc = QComboBox()
        # self.combo_output_mode = QComboBox()
        # self.combo_profile_tracking = QComboBox()
        # self.combo_profile_number = QComboBox()

        self.init_fields()
        self.init_connections()

    def init_fields(self):
        self.combo_monitor_tc.addItems(list(self.tc_types.keys()))
        self.combo_controller_tc.addItems(['K', 'J', 'T', 'E', 'N', 'L', 'R', 'S', 'B', 'C'])
        self.combo_output_mode.addItems(list(ENUM.write.output_mode.keys()))
        self.combo_profile_number.addItems([str(x) for x in np.linspace(1, 99, 99)])
        self.combo_profile_tracking.addItems(list(ENUM.write.ramp_soak_tracking.keys()))
        self.update_fields()

    def update_fields(self):
        if not self.combo_monitor_tc.hasFocus():
            self.combo_monitor_tc.setCurrentText(self.external_tc.ai_thrmcpl_type.name)

        if not self.combo_controller_tc.hasFocus():
            tc_type = self.controller.get_tc_type()
            if tc_type == '<Reserved>':
                raise ValueError('Received invalid enumeration of thermocouple type from furnace controller.')
            self.combo_controller_tc.setCurrentText(tc_type)

        if not self.combo_output_mode.hasFocus():
            self.combo_output_mode.setCurrentText(self.controller.get_output_mode(3))

        if not self.combo_profile_number.hasFocus():
            self.combo_profile_number.setCurrentText(str(self.controller.get_current_profile_number()))

        if not self.combo_profile_tracking.hasFocus():
            self.combo_profile_tracking.setCurrentText(self.controller.get_ramp_soak_tracking_mode())

    def init_connections(self):
        self.combo_monitor_tc.currentTextChanged.connect(self.set_external_tc_type)
        #FIXME: Finish out connections to other controls

    def init_external_tc(self, tcdevpath):
        tc = SignalTask()
        tc.ai_channels.add_ai_thrmcpl_chan(tcdevpath)
        tc.ai_thrmcpl_type = self.tc_types['S']
        tc.ai_temp_units = nidaqmx.constants.TemperatureUnits.DEG_C
        return tc

    def set_external_tc_type(self, type):
        self.external_tc.ai_thrmcpl_type.tc_types[type]

    # FIXME: Add plotting capability


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FurnaceLogger('COM3')
    window.show()
    sys.exit(app.exec_())