from PyDAQmx import (Task, InvalidAttributeValueError, DAQmx_Val_DegC, DAQmx_Val_J_Type_TC,
                     DAQmx_Val_K_Type_TC, DAQmx_Val_T_Type_TC, DAQmx_Val_E_Type_TC,
                     DAQmx_Val_N_Type_TC, DAQmx_Val_R_Type_TC, DAQmx_Val_S_Type_TC,
                     DAQmx_Val_B_Type_TC, DAQmx_Val_GroupByChannel, DAQmx_Val_BuiltIn)
from PyDAQmx.DAQmxTypes import byref, int32
from PyQt5.QtCore import pyqtSignal, QObject
import numpy as np


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