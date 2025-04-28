from datetime import timedelta
from time import sleep

from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtWidgets import QWidget, QLineEdit, QCheckBox, QGroupBox, QProxyStyle, QStyle, QMessageBox

from main import FurnaceLogger
from src.ui.profile_settings_ui import Ui_ProfileSettingsDialog
import xml.etree.ElementTree as ET
from copy import deepcopy
import Omega_Platinum_Enum as ENUM
import minimalmodbus_OmegaPt as modbus


# Used to prevent the spinbox from changing more than one number per click
class NoRepeatSpinStyle(QProxyStyle):
    # See: https://stackoverflow.com/questions/40746350/why-qspinbox-jumps-twice-the-step-value
    def styleHint(self, hint, option=None, widget=None, returnData=None):
        if hint == QStyle.SH_SpinBox_KeyPressAutoRepeatRate:
            return 10**10
        elif hint == QStyle.SH_SpinBox_ClickAutoRepeatRate:
            return 10**10
        elif hint == QStyle.SH_SpinBox_ClickAutoRepeatThreshold:
            # You can use only this condition to avoid the auto-repeat,
            # but better safe than sorry ;-)
            return 10**10
        else:
            return super().styleHint(hint, option, widget, returnData)


class ProfileSettingsDialog(QWidget):
    profile_num_signal = pyqtSignal(int)
    blank_profile = {
        'number': 1, 'trackingMode': '', 'numSegments': 0, 'linkAction': '', 'linkProfile': 0,
        1: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        2: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        3: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        4: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        5: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        6: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        7: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
        8: {'active': True, 'ramp': True, 'soak': True, 'rTime': 36000, 'sTime': 3600, 'setpoint': 500},
    }

    def __init__(self, parent=None):
        # ToDo: Does this break with promoted widget or does it get the argument automagically? may need to override set
        #  parent function instead of setting in the init
        self.controller = None
        super(ProfileSettingsDialog, self).__init__()

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

        self.current_profile = deepcopy(self.blank_profile)

    def init_fields(self):
        self.ui.spin_profile_num.setRange(1, 99)
        self.ui.spin_profile_num.setStyle(NoRepeatSpinStyle())
        self.ui.combo_tracking_mode.addItems(list(ENUM.Write.ramp_soak_tracking.keys()))
        self.ui.spin_num_segments.setRange(1, 8)
        self.ui.spin_num_segments.setStyle(NoRepeatSpinStyle())
        self.ui.combo_link_action.addItems(list(ENUM.Write.ramp_soak_link_action.keys()))
        self.ui.spin_link_to.setRange(0, 99)
        self.ui.spin_link_to.setStyle(NoRepeatSpinStyle())

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
        self.ui.btn_ok.clicked.connect(self.ok)
        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_reload_profile.clicked.connect(
            lambda: self.load_profile_from_controller(self.ui.spin_profile_num.value()))

    def set_parent(self, parent: FurnaceLogger):
        self.parent = parent
        self.controller = parent.controller
        self.load_profile_from_controller(self.parent.controller.get_current_edit_profile_number())
    def ok(self):
        self.write_profile()
        self.close()

    def apply(self):
        self.write_profile()

    def cancel(self):
        self.load_profile_from_controller(self.ui.spin_profile_num.value())
        self.close()

    def close(self):
        self.profile_num_signal.emit(self.current_profile['number'])
        super(ProfileSettingsDialog, self).close()

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
                self.load_profile_from_controller(self.current_profile['linkProfile'])
                root.append(self._profile_xml(self.current_profile, sequence=sequence))

            self.load_profile_from_controller(execute_profile)

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

    def _read_profile(self, profile: int):
        # print('Loading profile number {}'.format(profile))
        read_profile = deepcopy(self.blank_profile)
        read_profile['number'] = profile
        self.parent.controller.set_current_profile_number(profile)
        read_profile.update(self.controller.read_profile_info())
        for i in range(1, 9):  # Note 1-9 because range does not include last value
            # ToDo: Investigate if this is needed with generalized catch in the modbus code
            try:
                self.controller.set_current_segment_number(i)
                read_profile[i] = dict(
                    active=(True if i <= read_profile['numSegments'] else False), )
                read_profile[i].update(self.controller.read_full_segment())
            except modbus.NoResponseError as err:
                print(err)
                print("Sleeping 0.2s then retrying load of profile {}".format(profile))
                sleep(0.2)
                return self._read_profile(profile)
        return read_profile

    def load_profile_from_controller(self, profile: int):
        self.current_profile = self._read_profile(profile)
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
        # Done 05 April 2023: check for changes to save before reading new profile
        if self.profile_edited():
            save_edited_profile = QMessageBox()
                                                       # "The profile has been edited. Loading a new profile will erase "
                                                       # "any changes that have been made. Would you like to save the "
                                                       # "edited profile?",
                                                       # QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                       # QMessageBox.No)
            save_edited_profile.setIcon(QMessageBox.Question)
            save_edited_profile.setText("Profile has been edited")
            save_edited_profile.setInformativeText("The profile has been edited. Loading a new profile will erase "
                                                   "any changes that have been made. Would you like to save the "
                                                   "edited profile before loading profile #{}?".format(profile_num))
            save_edited_profile.addButton(QMessageBox.Save)
            save_edited_profile.addButton("Revert Changes", QMessageBox.RejectRole)
            ret = save_edited_profile.exec()
            if ret == QMessageBox.Save:
                self.write_profile()
            elif ret == QMessageBox.RejectRole:
                pass
        sleep(0.2)
        self.load_profile_from_controller(profile_num)

    def profile_edited(self):
        controller_profile = self._read_profile(self.current_profile['number'])
        if self.current_profile == controller_profile:
            return False
        else:
            return True

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
        self.load_profile_from_controller(self.current_profile['number'])

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

        td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        hours, remainder = divmod(td.seconds, 3600)
        hours = hours + td.days * 24
        if hours > 99:
            hours = 99
        minutes, seconds = divmod(remainder, 60)

        ret = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
        return ret

    @staticmethod
    def convert_time_to_msec(time_str: str):
        hours, minutes, seconds = time_str.split(':')
        # Note: No exception checking here. I want this to fail if it gets passed an invalid time string.
        #  This should prevent sending junk data to the controller.
        try:
            hours = int(hours)
        except ValueError as err:
            print(err)
            if 'days' in hours:
                days, hours = hours.split(' days, ')
                # print('Got days: {}, hours: {}'.format(days, hours))
                hours = int(days) * 24 + int(hours)
                if hours > 99:
                    hours = 99
                # print('Converted to Hours: {}'.format(hours))
        minutes = int(minutes)
        seconds = int(seconds)

        td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return int((td.seconds + (td.days * 24 * 3600)) * 1000)

    @staticmethod
    def convert_msec_to_time(msec: int):
        td = timedelta(milliseconds=msec)
        hours, remainder = divmod(td.seconds, 3600)
        hours = hours + td.days * 24
        if hours > 99:
            hours = 99
        minutes, seconds = divmod(remainder, 60)

        ret = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
        return ret