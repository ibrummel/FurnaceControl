# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import minimalmodbus_OmegaPt as modbus
from time import sleep
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class OmegaPlatinumControllerModbus(QWidget):
    data_ready = pyqtSignal()
    def __init__(self, comport: str):
        super().__init__()

        try:
            self.instrument = modbus.Instrument(comport, 1, mode='MODE_RTU', close_port_after_each_call=False,
                                                debug=False)
        except Exception as err:
            print(err)
        finally:
            print("Could not connect to furnace controller, make sure all other control software is closed and you have"
                  " supplied the correct comport (Port Supplied='{}')".format(comport))

        self.instrument.read_register(628)



def print_hi():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
