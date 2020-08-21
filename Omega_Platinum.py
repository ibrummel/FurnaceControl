# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import minimalmodbus_OmegaPt as modbus
import Omega_Platinum_Enum as ENUM
import numpy as np
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class OmegaPlatinumControllerModbus(QWidget):
    temp_ready = pyqtSignal()
    def __init__(self, comport: str, rounding=2):
        super().__init__()

        try:
            self.controller = modbus.Instrument(comport, 1, mode='rtu', close_port_after_each_call=False,
                                                debug=False)
        except Exception as err:
            print(err)
            print("Could not connect to furnace controller, make sure all other control software is closed and you have"
                  " supplied the correct comport (Port Supplied='{}')".format(comport))
        else:
            print('Connected to controller without errors.')

        self._SIGFIGS_AFTER_DECIMAL = rounding

    def get_process_temp(self):
        return np.round(float(self.controller.read_float(640)), self._SIGFIGS_AFTER_DECIMAL)

    def get_system_state(self):
        return ENUM.read.system_state[self.controller.read_register(576)]

    def set_system_state(self, state):
        if state not in ENUM.write.system_state:
            raise ValueError("Cannot set to invalid system state: {}".format(state))
        self.controller.write_register(576, ENUM.write.system_state[state])

    def get_tc_type(self):
        return ENUM.read.tc_type[self.controller.read_register(643)]

    def set_tc_type(self, tc_type):
        if tc_type not in ENUM.write.tc_type:
            raise ValueError("Cannot set thermocouple type to un-enumerated type: {}".format(tc_type))
        self.controller.write_register(643, ENUM.write.tc_type[tc_type])

    def get_output_mode(self, output_num: int):
        if 1 <= output_num < 8:
            datum = 'mode'
            register = ENUM.get_output_register(output_num, datum)
            return ENUM.read.output_mode[self.controller.read_register(register)]

    def set_output_mode(self, output_num: int, mode: str):
        if 1 <= output_num <= 8:
            datum = 'mode'
            register = ENUM.get_output_register(output_num, datum)
            if mode not in ENUM.write.output_mode:
                raise ValueError("Invalid output mode supplied {}. "
                                 "Valid modes are {}".format(mode, ENUM.write.output_mode.keys()))
            self.controller.write_register(register, ENUM.write.output_mode[mode])

    def set_retransmission_trim(self, output_num: int, reading1=0., output1=0.,
                                reading2=100., output2=1.):
        if 1<=output_num<= 8:
            data = ['retran_reading1', 'retran_output1', 'retran_reading2', 'retran_output2']
            trims = [reading1, output1, reading2, output2]
            if not (isinstance(reading1, (int, float)) and isinstance(output1, (int, float))
                    and isinstance(reading2, (int, float)) and isinstance(output2, (int, float))):
                raise TypeError('Retransmission output trim must be set using floats or ints. The following types were'
                                ' supplied {}'.format([type(reading1), type(output1), type(reading2), type(output2)]))

            for i, datum in enumerate(data):
                register = ENUM.get_output_register(output_num, datum)
                self.controller.write_float(register, trims[i])

    def get_retransmission_trim(self, output_num: int):
        if 1<=output_num<= 8:
            data = ['retran_reading1', 'retran_output1', 'retran_reading2', 'retran_output2']
            trims = []

            for i, datum in enumerate(data):
                register = ENUM.get_output_register(output_num, datum)
                trims.append(float(self.controller.read_float(register)))

            return trims

    def set_ramp_soak_tracking(self, mode: str):
        if mode not in ENUM.write.ramp_soak_tracking:
            raise ValueError("Invalid ramp/soak tracking mode supplied: {}".format(mode))
        self.controller.write_register(615, ENUM.write.ramp_soak_tracking[mode])

    # TODO: Add profile editing and selection
