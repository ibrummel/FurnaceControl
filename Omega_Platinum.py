# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import minimalmodbus_OmegaPt as modbus
import Omega_Platinum_Enum as ENUM
import numpy as np
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
import struct
from datetime import timedelta


class OmegaPlatinumControllerModbus(QWidget):
    temp_ready = pyqtSignal(float)

    def __init__(self, comport: str, rounding=2):
        super(OmegaPlatinumControllerModbus, self).__init__()

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
        temp = np.round(float(self.controller.read_float(640)), self._SIGFIGS_AFTER_DECIMAL)
        self.temp_ready.emit(temp)
        return temp

    def get_system_state(self):
        return ENUM.Read.system_state[self.controller.read_register(576)]

    def set_system_state(self, state: str):
        if state not in ENUM.Write.system_state:
            raise ValueError("Cannot set to invalid system state: {}".format(state))
        self.controller.write_register(576, ENUM.Write.system_state[state])

    def get_tc_type(self):
        return ENUM.Read.tc_type[self.controller.read_register(643)]

    def set_tc_type(self, tc_type):
        if tc_type not in ENUM.Write.tc_type:
            raise ValueError("Cannot set thermocouple type to un-enumerated type: {}".format(tc_type))
        self.controller.write_register(643, ENUM.Write.tc_type[tc_type])

    def get_output_mode(self, output_num: int):
        if 1 <= output_num < 8:
            datum = 'mode'
            register = ENUM.get_output_register(output_num, datum)
            return ENUM.Read.output_mode[self.controller.read_register(register)]

    def set_output_mode(self, output_num: int, mode: str):
        if 1 <= output_num <= 8:
            datum = 'mode'
            register = ENUM.get_output_register(output_num, datum)
            if mode not in ENUM.Write.output_mode:
                raise ValueError("Invalid output mode supplied {}. "
                                 "Valid modes are {}".format(mode, ENUM.Write.output_mode.keys()))
            self.controller.write_register(register, ENUM.Write.output_mode[mode])

    def set_retransmission_trim(self, output_num: int, reading1=0., output1=0.,
                                reading2=100., output2=1.):
        if 1 <= output_num <= 8:
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
        if 1 <= output_num <= 8:
            data = ['retran_reading1', 'retran_output1', 'retran_reading2', 'retran_output2']
            trims = []

            for i, datum in enumerate(data):
                register = ENUM.get_output_register(output_num, datum)
                trims.append(float(self.controller.read_float(register)))

            return trims

    ###############################################################################################
    # PROFILE SPECIFIC SETTINGS
    ###############################################################################################
    def get_current_profile_number(self):
        return int(self.controller.read_register(610))

    def set_current_profile_number(self, profile_num: int):
        if not isinstance(profile_num, (int, float)):
            raise TypeError("Cannot set profile to a value with type {}".format(type(profile_num)))
        elif 1 <= profile_num <= 99:
            self.controller.write_register(610, int(profile_num))
        else:
            raise ValueError("Cannot set a profile number outside the range 1-99. "
                             "Profile number supplied: {}".format(profile_num))

    # Note: The following get/set functions rely on the user setting the current profile number
    #  before accessing them in order to return/set the desired information.
    # Fixme: Maybe add helper functions that take the desired profile number too. But
    #  might add a lot of overhead on repeated calls.

    def get_segments_per_profile(self):
        return int(self.controller.read_register(612))

    def set_segments_per_profile(self, num_segments: int):
        self.controller.write_register(612, num_segments)

    def get_link_action(self):
        return ENUM.Read.ramp_soak_link_action[self.controller.read_register(613)]

    def set_link_action(self, link_action: str):
        self.controller.write_register(613, ENUM.Write.ramp_soak_link_action[link_action])

    def get_link_profile(self):
        return int(self.controller.read_register(614))

    def set_link_profile(self, link_profile: int):
        self.controller.write_register(614, link_profile)

    def get_ramp_soak_tracking_mode(self):
        return ENUM.Read.ramp_soak_tracking[self.controller.read_register(615)]

    def set_ramp_soak_tracking_mode(self, mode: str):
        if mode not in ENUM.Write.ramp_soak_tracking.keys():
            raise ValueError('Invalid ramp/soak profile tracking mode supplied: {}.'.format(mode))
        self.controller.write_register(615, ENUM.Write.ramp_soak_tracking[mode])

    ###############################################################################################
    # SEGMENT SPECIFIC SETTINGS
    ###############################################################################################
    def get_current_segment_number(self):
        return int(self.controller.read_register(611))

    def set_current_segment_number(self, segment_num: int):
        if not isinstance(segment_num, (int, float)):
            raise TypeError("Cannot set segment to a value with type {}".format(type(segment_num)))
        elif 1 <= segment_num <= 8:
            self.controller.write_register(611, int(segment_num))
        else:
            raise ValueError("Cannot set a segment number outside the range 1-8. "
                             "Segment number supplied: {}".format(segment_num))

    # Note: The following get/set functions rely on the user setting the current segment number
    #  before accessing them in order to return/set the desired information.
    def get_ramp_event_flag(self):
        return bool(self.controller.read_register(616))

    def set_ramp_event_flag(self, ramp_event: bool):
        self.controller.write_register(616, ramp_event)

    def get_soak_event_flag(self):
        return bool(self.controller.read_register(617))

    def set_soak_event_flag(self, soak_event: bool):
        self.controller.write_register(617, soak_event)

    def get_segment_setpoint(self):
        return self.read_multi_register(618, 'float')

    def set_segment_setpoint(self, setpoint: float):
        self.write_multi_register(618, 'float', setpoint)

    def get_ramp_time_msec(self):
        return self.read_multi_register(620, 'int')

    def get_ramp_time_formatted(self):
        return timedelta(milliseconds=self.get_ramp_time_msec()).__str__()

    def set_ramp_time_msec(self, ramp_time_msec: float):
        self.write_multi_register(620, 'int', ramp_time_msec)

    def get_soak_time_msec(self):
        return self.read_multi_register(622, 'int')

    def get_soak_time_formatted(self):
        return timedelta(milliseconds=self.get_soak_time_msec()).__str__()

    def set_soak_time_msec(self, dwell_time_msec: float):
        self.write_multi_register(622, 'int', dwell_time_msec)

    ###############################################################################################
    # MULTI REGISTER VALUE HELPER FUNCTIONS
    ###############################################################################################
    def read_multi_register(self, start_register: int, value_type: str):
        data = self.controller.read_registers(start_register, 2)
        packed = struct.pack('>HH', data[0], data[1])

        if value_type == 'float':
            return struct.unpack('>f', packed)[0]
        elif value_type == 'int':
            return struct.unpack('>L', packed)[0]
        else:
            raise TypeError("Invalid return type requested: {}".format(value_type))

    def write_multi_register(self, start_register: int, value_type: type, value):
        if value_type == 'float':
            packed = struct.pack('>f', value)
        elif value_type == 'int':
            packed = struct.pack('>L', value)
        else:
            raise TypeError("Invalid conversion type requested: {}".format(value_type))

        values = list(struct.unpack('>HH', packed))
        self.controller.write_registers(start_register, values)

    # TODO: Add profile editing and selection
