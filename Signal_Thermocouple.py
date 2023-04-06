from PyDAQmx import (Task, InvalidAttributeValueError, DAQmx_Val_DegC, DAQmx_Val_J_Type_TC,
                     DAQmx_Val_K_Type_TC, DAQmx_Val_T_Type_TC, DAQmx_Val_E_Type_TC,
                     DAQmx_Val_N_Type_TC, DAQmx_Val_R_Type_TC, DAQmx_Val_S_Type_TC,
                     DAQmx_Val_B_Type_TC, DAQmx_Val_GroupByChannel, DAQmx_Val_BuiltIn)
from PyDAQmx.DAQmxTypes import byref, int32
from PyQt5.QtCore import pyqtSignal, QObject
import numpy as np
from time import sleep


class SignalThermocouple(QObject):
    ext_temp_ready = pyqtSignal(float)

    def __init__(self, task_name: str, tcdevpath: str, tc_chan_name='tc',
                 units=DAQmx_Val_DegC, tc_type=DAQmx_Val_S_Type_TC, cjc_source=DAQmx_Val_BuiltIn,
                 cjc_val=0, cjc_channel=0):
        super(SignalThermocouple, self).__init__()
        # Dictionaries to act as a translation layer for TC types
        # See: https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermocouples.html
        self.tc_types_rev = {DAQmx_Val_J_Type_TC: ['J', -210, 1200],  # 10072
                             DAQmx_Val_K_Type_TC: ['K', -200, 1372],  # 10073
                             DAQmx_Val_T_Type_TC: ['T', -200, 400],  # 10086
                             DAQmx_Val_E_Type_TC: ['E', -200, 1000],  # 10055
                             DAQmx_Val_N_Type_TC: ['N', -200, 1300],  # 10077
                             DAQmx_Val_R_Type_TC: ['R', -50, 1768],  # 10082
                             DAQmx_Val_S_Type_TC: ['S', -50, 1768],  # 10085
                             DAQmx_Val_B_Type_TC: ['B', 250, 1820],  # 10047
                             }
        self.tc_types = {'J': [DAQmx_Val_J_Type_TC, -210, 1200],
                         'K': [DAQmx_Val_K_Type_TC, -200, 1372],
                         'T': [DAQmx_Val_T_Type_TC, -200, 400],
                         'E': [DAQmx_Val_E_Type_TC, -200, 1000],
                         'N': [DAQmx_Val_N_Type_TC, -200, 1300],
                         'R': [DAQmx_Val_R_Type_TC, -50, 1768],
                         'S': [DAQmx_Val_S_Type_TC, -50, 1768],
                         'B': [DAQmx_Val_B_Type_TC, 250, 1820],
                         }
        # Create task to hold tc read channel
        self.tc = Task(task_name)
        # Create channel that reads tc value
        self.tc_chan_name = tc_chan_name
        tc_type = self.tc_types[tc_type][0] if isinstance(tc_type, str) else tc_type
        min_val = self.tc_types_rev[tc_type][1]
        max_val = self.tc_types_rev[tc_type][2]
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
            tc_type = self.tc_types[tc_type][0]

        try:
            self.tc.SetAIMin(self.tc_chan_name, self.tc_types_rev[tc_type][1])
            self.tc.SetAIMax(self.tc_chan_name, self.tc_types_rev[tc_type][2])
            ret = self.tc.SetAIThrmcplType(self.tc_chan_name, tc_type)
        except InvalidAttributeValueError:
            ret = -1
            print("Tried to set external thermocouple to invalid type. Reverting...")
        return ret

    def get_tc_type(self):
        ret = int32()
        self.tc.GetAIThrmcplType(self.tc_chan_name, byref(ret))

        return self.tc_types_rev[ret.value][0]
