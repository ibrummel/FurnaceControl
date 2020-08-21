control = {0: 'Stop',
           1: 'Start',
           2: 'Cancel',
           3: 'Auto On',
           4: 'Continuous'}

control_action = {0: 'Reverse', 1: 'Direct'}

system_state = {0: 'Load', 1: 'Idle', 2: 'Input Adjust',
                3: 'Control Adjust', 4: 'Modify', 5: 'Wait',
                6: 'Run', 7: 'Standby', 8: 'Stop', 9: 'Pause',
                10: 'Fault', 11: 'Shutdown', 12: 'Autotune'}

ramp_soak_state = {0x00: 'Inactive', 0x01: 'Ramping', 0x02: 'Soaking', 0x04: 'Ramp Active',
                   0x08: 'Soak Active', 0x10: 'Ramp Soak Paused', 0x80: 'Ramp Soak Error'}

ramp_soak_tracking = {0: 'Ramp', 1: 'Soak', 2: 'Cycle'}

sensor_type = {0: 'Thermocouple',
               1: 'RTD',
               2: 'Process Input',
               3: 'Thermistor',
               4: 'Remote'}

tc_type = {0: 'J', 1: 'K', 2: 'T',
           3: 'E', 4: 'N', 5: '<Reserved>',
           6: 'R', 7: 'S', 8: 'B', 9: 'C',
           10: '<Reserved>', 11: '<Reserved>'}

output_hw_type = {0x00: 'None', 0x01: 'Single Pole', 0x02: 'Solid State Relay', 0x04: 'Double Pole',
                  0x08: 'DC Pulse', 0x10: 'Analog', 0x20: 'Isolated Analog', 0x20: 'Isolated DC Pulse'}

output_polarity = {0: 'Normally Open', 1: 'Normally Closed'}

output_type = {0: 'Voltage', 1: 'Current'}
