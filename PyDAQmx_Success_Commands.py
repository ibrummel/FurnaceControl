# coding: utf-8
from PyDAQmx.DAQmxTypes import *
from PyDAQmx import *
from time import sleep
import numpy as np
# Create Task object with linked TC
tc = Task('External TC')
tc.CreateAIThrmcplChan("Dev1/ai0","tc", 20, 1700, DAQmx_Val_DegC, DAQmx_Val_S_Type_TC, DAQmx_Val_BuiltIn, 0, 0)

# Read TC into data variable
read = int32()
data = np.zeros((1,), dtype=np.float64)
tc.ReadAnalogF64(1, 0.5, DAQmx_Val_GroupByChannel, data, 1, byref(read), None)
data

# Set TC type
tc.SetAIThrmcplType('tc', DAQmx_Val_B_Type_TC)

# Get TC Type and store enumerated value in ret
ret = int32()
tc.GetAIThrmcplType('tc', POINTER(ret))
ret
