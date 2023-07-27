class Read:
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

    ramp_soak_tracking = {0: 'Ramp', 1: 'Soak', 2: 'Cycle'}

    ramp_soak_control = {0: "Disabled", 1: "Front Panel", 2: "Front Panel/D.Input"}

    ramp_soak_link_action = {0: "Stop", 1: "Hold", 2: "Link"}

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
                      0x08: 'DC Pulse', 0x10: 'Analog', 0x20: 'Isolated Analog', 0x40: 'Isolated DC Pulse'}

    output_polarity = {0: 'Normally Open', 1: 'Normally Closed'}

    output_type = {0: 'Voltage', 1: 'Current'}

    output_mode = {0: 'Off', 1: 'PID', 2: 'On/Off',
                   3: 'Retransmission', 4: 'Alarm 1',
                   5: 'Alarm 2', 6: 'Ramp Event',
                   7: 'Soak Event', }

    output_process_range = {0: '0-10 Vdc', 1: '0-5 Vdc', 2: '0-20 mA',
                            3: '4-20 mA', 4: '0-24 mA', }


class Write:
    control = {v: k for k, v in Read.control.items()}

    control_action = {v: k for k, v in Read.control_action.items()}

    system_state = {v: k for k, v in Read.system_state.items()}

    ramp_soak_tracking = {v: k for k, v in Read.ramp_soak_tracking.items()}

    ramp_soak_control = {v: k for k, v in Read.ramp_soak_control.items()}

    ramp_soak_link_action = {v: k for k, v in Read.ramp_soak_link_action.items()}

    sensor_type = {v: k for k, v in Read.sensor_type.items()}

    tc_type = {v: k for k, v in Read.tc_type.items()}

    output_hw_type = {v: k for k, v in Read.output_hw_type.items()}

    output_polarity = {v: k for k, v in Read.output_polarity.items()}

    output_type = {v: k for k, v in Read.output_type.items()}

    output_mode = {v: k for k, v in Read.output_mode.items()}

    output_process_range = {v: k for k, v in Read.output_process_range.items()}


class ReadOnly():
    readonly_ramp_soak_state = {0x00: 'Inactive', 0x01: 'Ramping', 0x02: 'Soaking', 0x04: 'Ramp Active',
                                0x08: 'Soak Active', 0x05: 'Ramping, Ramp Active', 0x0a: 'Soaking, Soak Active',
                                0x10: 'Ramp Soak Paused', 0x80: 'Ramp Soak Error'}


def get_output_register(output: int, datum: str):
    output_registers_start = {1: 1024, 2: 1056, 3: 1088, 4: 1120,
                              5: 1152, 6: 1184, 7: 1216, 8: 1248}
    output_registers_offset = {"hw_type": 0,
                               'mode': 1,
                               'on_off_action': 2,
                               'setpoint': 3,
                               'pulse_length': 4,
                               'on_off_deadband': 6,
                               'output_range': 8,
                               'retran_reading1': 10,
                               'retran_output1': 12,
                               'retran_reading2': 14,
                               'retran_output2': 16}

    if datum not in output_registers_offset:
        raise ValueError("Datum label supplied ({}) is not available for controller ouputs. "
                         "Valid data labels {}".format(datum, output_registers_offset.keys()))
    return output_registers_start[output] + output_registers_offset[datum]
