# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/profile_settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProfileSettingsDialog(object):
    def setupUi(self, ProfileSettingsDialog):
        ProfileSettingsDialog.setObjectName("ProfileSettingsDialog")
        ProfileSettingsDialog.resize(758, 759)
        font = QtGui.QFont()
        font.setPointSize(8)
        ProfileSettingsDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProfileSettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbox_profile_settings = QtWidgets.QGroupBox(ProfileSettingsDialog)
        self.gbox_profile_settings.setObjectName("gbox_profile_settings")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbox_profile_settings)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.combo_tracking_mode = QtWidgets.QComboBox(self.gbox_profile_settings)
        self.combo_tracking_mode.setObjectName("combo_tracking_mode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_tracking_mode)
        self.lbl_num_segments = QtWidgets.QLabel(self.gbox_profile_settings)
        self.lbl_num_segments.setObjectName("lbl_num_segments")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_num_segments)
        self.spin_num_segments = QtWidgets.QSpinBox(self.gbox_profile_settings)
        self.spin_num_segments.setKeyboardTracking(False)
        self.spin_num_segments.setObjectName("spin_num_segments")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_num_segments)
        self.lbl_tracking_mode = QtWidgets.QLabel(self.gbox_profile_settings)
        self.lbl_tracking_mode.setObjectName("lbl_tracking_mode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_tracking_mode)
        self.lbl_profile_num = QtWidgets.QLabel(self.gbox_profile_settings)
        self.lbl_profile_num.setObjectName("lbl_profile_num")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_profile_num)
        self.spin_profile_num = QtWidgets.QSpinBox(self.gbox_profile_settings)
        self.spin_profile_num.setKeyboardTracking(False)
        self.spin_profile_num.setObjectName("spin_profile_num")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_profile_num)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl_link_action = QtWidgets.QLabel(self.gbox_profile_settings)
        self.lbl_link_action.setObjectName("lbl_link_action")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_link_action)
        self.combo_link_action = QtWidgets.QComboBox(self.gbox_profile_settings)
        self.combo_link_action.setObjectName("combo_link_action")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_link_action)
        self.lbl_link_to = QtWidgets.QLabel(self.gbox_profile_settings)
        self.lbl_link_to.setObjectName("lbl_link_to")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_link_to)
        self.spin_link_to = QtWidgets.QSpinBox(self.gbox_profile_settings)
        self.spin_link_to.setKeyboardTracking(False)
        self.spin_link_to.setObjectName("spin_link_to")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_link_to)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.gbox_profile_settings)
        self.scrollArea = QtWidgets.QScrollArea(ProfileSettingsDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 842, 872))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gbox_segment_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_1.setObjectName("gbox_segment_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbox_segment_1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_stpt_1 = QtWidgets.QLabel(self.gbox_segment_1)
        self.lbl_stpt_1.setObjectName("lbl_stpt_1")
        self.horizontalLayout_2.addWidget(self.lbl_stpt_1)
        self.line_stpt_1 = QtWidgets.QLineEdit(self.gbox_segment_1)
        self.line_stpt_1.setObjectName("line_stpt_1")
        self.horizontalLayout_2.addWidget(self.line_stpt_1)
        self.line = QtWidgets.QFrame(self.gbox_segment_1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.check_ramp_1 = QtWidgets.QCheckBox(self.gbox_segment_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_1.sizePolicy().hasHeightForWidth())
        self.check_ramp_1.setSizePolicy(sizePolicy)
        self.check_ramp_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_1.setObjectName("check_ramp_1")
        self.horizontalLayout_2.addWidget(self.check_ramp_1)
        self.line_ramp_1 = QtWidgets.QLineEdit(self.gbox_segment_1)
        self.line_ramp_1.setObjectName("line_ramp_1")
        self.horizontalLayout_2.addWidget(self.line_ramp_1)
        self.line_2 = QtWidgets.QFrame(self.gbox_segment_1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.check_dwell_1 = QtWidgets.QCheckBox(self.gbox_segment_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_1.sizePolicy().hasHeightForWidth())
        self.check_dwell_1.setSizePolicy(sizePolicy)
        self.check_dwell_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_1.setObjectName("check_dwell_1")
        self.horizontalLayout_2.addWidget(self.check_dwell_1)
        self.line_dwell_1 = QtWidgets.QLineEdit(self.gbox_segment_1)
        self.line_dwell_1.setObjectName("line_dwell_1")
        self.horizontalLayout_2.addWidget(self.line_dwell_1)
        self.verticalLayout_2.addWidget(self.gbox_segment_1)
        self.gbox_segment_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_2.setObjectName("gbox_segment_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.gbox_segment_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_stpt_2 = QtWidgets.QLabel(self.gbox_segment_2)
        self.lbl_stpt_2.setObjectName("lbl_stpt_2")
        self.horizontalLayout_3.addWidget(self.lbl_stpt_2)
        self.line_stpt_2 = QtWidgets.QLineEdit(self.gbox_segment_2)
        self.line_stpt_2.setObjectName("line_stpt_2")
        self.horizontalLayout_3.addWidget(self.line_stpt_2)
        self.line_3 = QtWidgets.QFrame(self.gbox_segment_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.check_ramp_2 = QtWidgets.QCheckBox(self.gbox_segment_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_2.sizePolicy().hasHeightForWidth())
        self.check_ramp_2.setSizePolicy(sizePolicy)
        self.check_ramp_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_2.setObjectName("check_ramp_2")
        self.horizontalLayout_3.addWidget(self.check_ramp_2)
        self.line_ramp_2 = QtWidgets.QLineEdit(self.gbox_segment_2)
        self.line_ramp_2.setObjectName("line_ramp_2")
        self.horizontalLayout_3.addWidget(self.line_ramp_2)
        self.line_4 = QtWidgets.QFrame(self.gbox_segment_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_3.addWidget(self.line_4)
        self.check_dwell_2 = QtWidgets.QCheckBox(self.gbox_segment_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_2.sizePolicy().hasHeightForWidth())
        self.check_dwell_2.setSizePolicy(sizePolicy)
        self.check_dwell_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_2.setObjectName("check_dwell_2")
        self.horizontalLayout_3.addWidget(self.check_dwell_2)
        self.line_dwell_2 = QtWidgets.QLineEdit(self.gbox_segment_2)
        self.line_dwell_2.setObjectName("line_dwell_2")
        self.horizontalLayout_3.addWidget(self.line_dwell_2)
        self.verticalLayout_2.addWidget(self.gbox_segment_2)
        self.gbox_segment_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_3.setObjectName("gbox_segment_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gbox_segment_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_stpt_3 = QtWidgets.QLabel(self.gbox_segment_3)
        self.lbl_stpt_3.setObjectName("lbl_stpt_3")
        self.horizontalLayout_4.addWidget(self.lbl_stpt_3)
        self.line_stpt_3 = QtWidgets.QLineEdit(self.gbox_segment_3)
        self.line_stpt_3.setObjectName("line_stpt_3")
        self.horizontalLayout_4.addWidget(self.line_stpt_3)
        self.line_5 = QtWidgets.QFrame(self.gbox_segment_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.check_ramp_3 = QtWidgets.QCheckBox(self.gbox_segment_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_3.sizePolicy().hasHeightForWidth())
        self.check_ramp_3.setSizePolicy(sizePolicy)
        self.check_ramp_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_3.setObjectName("check_ramp_3")
        self.horizontalLayout_4.addWidget(self.check_ramp_3)
        self.line_ramp_3 = QtWidgets.QLineEdit(self.gbox_segment_3)
        self.line_ramp_3.setObjectName("line_ramp_3")
        self.horizontalLayout_4.addWidget(self.line_ramp_3)
        self.line_6 = QtWidgets.QFrame(self.gbox_segment_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_4.addWidget(self.line_6)
        self.check_dwell_3 = QtWidgets.QCheckBox(self.gbox_segment_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_3.sizePolicy().hasHeightForWidth())
        self.check_dwell_3.setSizePolicy(sizePolicy)
        self.check_dwell_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_3.setObjectName("check_dwell_3")
        self.horizontalLayout_4.addWidget(self.check_dwell_3)
        self.line_dwell_3 = QtWidgets.QLineEdit(self.gbox_segment_3)
        self.line_dwell_3.setObjectName("line_dwell_3")
        self.horizontalLayout_4.addWidget(self.line_dwell_3)
        self.verticalLayout_2.addWidget(self.gbox_segment_3)
        self.gbox_segment_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_4.setObjectName("gbox_segment_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.gbox_segment_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_stpt_4 = QtWidgets.QLabel(self.gbox_segment_4)
        self.lbl_stpt_4.setObjectName("lbl_stpt_4")
        self.horizontalLayout_5.addWidget(self.lbl_stpt_4)
        self.line_stpt_4 = QtWidgets.QLineEdit(self.gbox_segment_4)
        self.line_stpt_4.setObjectName("line_stpt_4")
        self.horizontalLayout_5.addWidget(self.line_stpt_4)
        self.line_7 = QtWidgets.QFrame(self.gbox_segment_4)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_5.addWidget(self.line_7)
        self.check_ramp_4 = QtWidgets.QCheckBox(self.gbox_segment_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_4.sizePolicy().hasHeightForWidth())
        self.check_ramp_4.setSizePolicy(sizePolicy)
        self.check_ramp_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_4.setObjectName("check_ramp_4")
        self.horizontalLayout_5.addWidget(self.check_ramp_4)
        self.line_ramp_4 = QtWidgets.QLineEdit(self.gbox_segment_4)
        self.line_ramp_4.setObjectName("line_ramp_4")
        self.horizontalLayout_5.addWidget(self.line_ramp_4)
        self.line_8 = QtWidgets.QFrame(self.gbox_segment_4)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_5.addWidget(self.line_8)
        self.check_dwell_4 = QtWidgets.QCheckBox(self.gbox_segment_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_4.sizePolicy().hasHeightForWidth())
        self.check_dwell_4.setSizePolicy(sizePolicy)
        self.check_dwell_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_4.setObjectName("check_dwell_4")
        self.horizontalLayout_5.addWidget(self.check_dwell_4)
        self.line_dwell_4 = QtWidgets.QLineEdit(self.gbox_segment_4)
        self.line_dwell_4.setObjectName("line_dwell_4")
        self.horizontalLayout_5.addWidget(self.line_dwell_4)
        self.verticalLayout_2.addWidget(self.gbox_segment_4)
        self.gbox_segment_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_5.setObjectName("gbox_segment_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.gbox_segment_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_stpt_5 = QtWidgets.QLabel(self.gbox_segment_5)
        self.lbl_stpt_5.setObjectName("lbl_stpt_5")
        self.horizontalLayout_6.addWidget(self.lbl_stpt_5)
        self.line_stpt_5 = QtWidgets.QLineEdit(self.gbox_segment_5)
        self.line_stpt_5.setObjectName("line_stpt_5")
        self.horizontalLayout_6.addWidget(self.line_stpt_5)
        self.line_9 = QtWidgets.QFrame(self.gbox_segment_5)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_6.addWidget(self.line_9)
        self.check_ramp_5 = QtWidgets.QCheckBox(self.gbox_segment_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_5.sizePolicy().hasHeightForWidth())
        self.check_ramp_5.setSizePolicy(sizePolicy)
        self.check_ramp_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_5.setObjectName("check_ramp_5")
        self.horizontalLayout_6.addWidget(self.check_ramp_5)
        self.line_ramp_5 = QtWidgets.QLineEdit(self.gbox_segment_5)
        self.line_ramp_5.setObjectName("line_ramp_5")
        self.horizontalLayout_6.addWidget(self.line_ramp_5)
        self.line_10 = QtWidgets.QFrame(self.gbox_segment_5)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_6.addWidget(self.line_10)
        self.check_dwell_5 = QtWidgets.QCheckBox(self.gbox_segment_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_5.sizePolicy().hasHeightForWidth())
        self.check_dwell_5.setSizePolicy(sizePolicy)
        self.check_dwell_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_5.setObjectName("check_dwell_5")
        self.horizontalLayout_6.addWidget(self.check_dwell_5)
        self.line_dwell_5 = QtWidgets.QLineEdit(self.gbox_segment_5)
        self.line_dwell_5.setObjectName("line_dwell_5")
        self.horizontalLayout_6.addWidget(self.line_dwell_5)
        self.verticalLayout_2.addWidget(self.gbox_segment_5)
        self.gbox_segment_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_6.setObjectName("gbox_segment_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.gbox_segment_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_stpt_6 = QtWidgets.QLabel(self.gbox_segment_6)
        self.lbl_stpt_6.setObjectName("lbl_stpt_6")
        self.horizontalLayout_7.addWidget(self.lbl_stpt_6)
        self.line_stpt_6 = QtWidgets.QLineEdit(self.gbox_segment_6)
        self.line_stpt_6.setObjectName("line_stpt_6")
        self.horizontalLayout_7.addWidget(self.line_stpt_6)
        self.line_11 = QtWidgets.QFrame(self.gbox_segment_6)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_7.addWidget(self.line_11)
        self.check_ramp_6 = QtWidgets.QCheckBox(self.gbox_segment_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_6.sizePolicy().hasHeightForWidth())
        self.check_ramp_6.setSizePolicy(sizePolicy)
        self.check_ramp_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_6.setObjectName("check_ramp_6")
        self.horizontalLayout_7.addWidget(self.check_ramp_6)
        self.line_ramp_6 = QtWidgets.QLineEdit(self.gbox_segment_6)
        self.line_ramp_6.setObjectName("line_ramp_6")
        self.horizontalLayout_7.addWidget(self.line_ramp_6)
        self.line_12 = QtWidgets.QFrame(self.gbox_segment_6)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_7.addWidget(self.line_12)
        self.check_dwell_6 = QtWidgets.QCheckBox(self.gbox_segment_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_6.sizePolicy().hasHeightForWidth())
        self.check_dwell_6.setSizePolicy(sizePolicy)
        self.check_dwell_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_6.setObjectName("check_dwell_6")
        self.horizontalLayout_7.addWidget(self.check_dwell_6)
        self.line_dwell_6 = QtWidgets.QLineEdit(self.gbox_segment_6)
        self.line_dwell_6.setObjectName("line_dwell_6")
        self.horizontalLayout_7.addWidget(self.line_dwell_6)
        self.verticalLayout_2.addWidget(self.gbox_segment_6)
        self.gbox_segment_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_7.setObjectName("gbox_segment_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.gbox_segment_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_stpt_7 = QtWidgets.QLabel(self.gbox_segment_7)
        self.lbl_stpt_7.setObjectName("lbl_stpt_7")
        self.horizontalLayout_8.addWidget(self.lbl_stpt_7)
        self.line_stpt_7 = QtWidgets.QLineEdit(self.gbox_segment_7)
        self.line_stpt_7.setObjectName("line_stpt_7")
        self.horizontalLayout_8.addWidget(self.line_stpt_7)
        self.line_13 = QtWidgets.QFrame(self.gbox_segment_7)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_8.addWidget(self.line_13)
        self.check_ramp_7 = QtWidgets.QCheckBox(self.gbox_segment_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_7.sizePolicy().hasHeightForWidth())
        self.check_ramp_7.setSizePolicy(sizePolicy)
        self.check_ramp_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_7.setObjectName("check_ramp_7")
        self.horizontalLayout_8.addWidget(self.check_ramp_7)
        self.line_ramp_7 = QtWidgets.QLineEdit(self.gbox_segment_7)
        self.line_ramp_7.setObjectName("line_ramp_7")
        self.horizontalLayout_8.addWidget(self.line_ramp_7)
        self.line_14 = QtWidgets.QFrame(self.gbox_segment_7)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout_8.addWidget(self.line_14)
        self.check_dwell_7 = QtWidgets.QCheckBox(self.gbox_segment_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_7.sizePolicy().hasHeightForWidth())
        self.check_dwell_7.setSizePolicy(sizePolicy)
        self.check_dwell_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_7.setObjectName("check_dwell_7")
        self.horizontalLayout_8.addWidget(self.check_dwell_7)
        self.line_dwell_7 = QtWidgets.QLineEdit(self.gbox_segment_7)
        self.line_dwell_7.setObjectName("line_dwell_7")
        self.horizontalLayout_8.addWidget(self.line_dwell_7)
        self.verticalLayout_2.addWidget(self.gbox_segment_7)
        self.gbox_segment_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gbox_segment_8.setObjectName("gbox_segment_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.gbox_segment_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_stpt_8 = QtWidgets.QLabel(self.gbox_segment_8)
        self.lbl_stpt_8.setObjectName("lbl_stpt_8")
        self.horizontalLayout_9.addWidget(self.lbl_stpt_8)
        self.line_stpt_8 = QtWidgets.QLineEdit(self.gbox_segment_8)
        self.line_stpt_8.setObjectName("line_stpt_8")
        self.horizontalLayout_9.addWidget(self.line_stpt_8)
        self.line_15 = QtWidgets.QFrame(self.gbox_segment_8)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayout_9.addWidget(self.line_15)
        self.check_ramp_8 = QtWidgets.QCheckBox(self.gbox_segment_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ramp_8.sizePolicy().hasHeightForWidth())
        self.check_ramp_8.setSizePolicy(sizePolicy)
        self.check_ramp_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_ramp_8.setObjectName("check_ramp_8")
        self.horizontalLayout_9.addWidget(self.check_ramp_8)
        self.line_ramp_8 = QtWidgets.QLineEdit(self.gbox_segment_8)
        self.line_ramp_8.setObjectName("line_ramp_8")
        self.horizontalLayout_9.addWidget(self.line_ramp_8)
        self.line_16 = QtWidgets.QFrame(self.gbox_segment_8)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.horizontalLayout_9.addWidget(self.line_16)
        self.check_dwell_8 = QtWidgets.QCheckBox(self.gbox_segment_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_dwell_8.sizePolicy().hasHeightForWidth())
        self.check_dwell_8.setSizePolicy(sizePolicy)
        self.check_dwell_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dwell_8.setObjectName("check_dwell_8")
        self.horizontalLayout_9.addWidget(self.check_dwell_8)
        self.line_dwell_8 = QtWidgets.QLineEdit(self.gbox_segment_8)
        self.line_dwell_8.setObjectName("line_dwell_8")
        self.horizontalLayout_9.addWidget(self.line_dwell_8)
        self.verticalLayout_2.addWidget(self.gbox_segment_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_reload_profile = QtWidgets.QPushButton(ProfileSettingsDialog)
        self.btn_reload_profile.setObjectName("btn_reload_profile")
        self.horizontalLayout_11.addWidget(self.btn_reload_profile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(ProfileSettingsDialog)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_11.addWidget(self.btn_ok)
        self.btn_apply = QtWidgets.QPushButton(ProfileSettingsDialog)
        self.btn_apply.setObjectName("btn_apply")
        self.horizontalLayout_11.addWidget(self.btn_apply)
        self.btn_cancel = QtWidgets.QPushButton(ProfileSettingsDialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_11.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(ProfileSettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(ProfileSettingsDialog)
        ProfileSettingsDialog.setTabOrder(self.spin_profile_num, self.combo_tracking_mode)
        ProfileSettingsDialog.setTabOrder(self.combo_tracking_mode, self.spin_num_segments)
        ProfileSettingsDialog.setTabOrder(self.spin_num_segments, self.combo_link_action)
        ProfileSettingsDialog.setTabOrder(self.combo_link_action, self.spin_link_to)
        ProfileSettingsDialog.setTabOrder(self.spin_link_to, self.line_stpt_1)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_1, self.check_ramp_1)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_1, self.line_ramp_1)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_1, self.check_dwell_1)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_1, self.line_dwell_1)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_1, self.line_stpt_2)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_2, self.check_ramp_2)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_2, self.line_ramp_2)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_2, self.check_dwell_2)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_2, self.line_dwell_2)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_2, self.line_stpt_3)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_3, self.check_ramp_3)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_3, self.line_ramp_3)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_3, self.check_dwell_3)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_3, self.line_dwell_3)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_3, self.line_stpt_4)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_4, self.check_ramp_4)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_4, self.line_ramp_4)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_4, self.check_dwell_4)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_4, self.line_dwell_4)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_4, self.line_stpt_5)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_5, self.check_ramp_5)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_5, self.line_ramp_5)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_5, self.check_dwell_5)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_5, self.line_dwell_5)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_5, self.line_stpt_6)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_6, self.check_ramp_6)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_6, self.line_ramp_6)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_6, self.check_dwell_6)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_6, self.line_dwell_6)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_6, self.line_stpt_7)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_7, self.check_ramp_7)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_7, self.line_ramp_7)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_7, self.check_dwell_7)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_7, self.line_dwell_7)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_7, self.line_stpt_8)
        ProfileSettingsDialog.setTabOrder(self.line_stpt_8, self.check_ramp_8)
        ProfileSettingsDialog.setTabOrder(self.check_ramp_8, self.line_ramp_8)
        ProfileSettingsDialog.setTabOrder(self.line_ramp_8, self.check_dwell_8)
        ProfileSettingsDialog.setTabOrder(self.check_dwell_8, self.line_dwell_8)
        ProfileSettingsDialog.setTabOrder(self.line_dwell_8, self.btn_reload_profile)
        ProfileSettingsDialog.setTabOrder(self.btn_reload_profile, self.btn_ok)
        ProfileSettingsDialog.setTabOrder(self.btn_ok, self.btn_apply)
        ProfileSettingsDialog.setTabOrder(self.btn_apply, self.btn_cancel)

    def retranslateUi(self, ProfileSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        ProfileSettingsDialog.setWindowTitle(_translate("ProfileSettingsDialog", "Form"))
        self.gbox_profile_settings.setTitle(_translate("ProfileSettingsDialog", "Profile Settings:"))
        self.lbl_num_segments.setText(_translate("ProfileSettingsDialog", "# of Segments:"))
        self.lbl_tracking_mode.setText(_translate("ProfileSettingsDialog", "Tracking Mode:"))
        self.lbl_profile_num.setText(_translate("ProfileSettingsDialog", "Profile Number:"))
        self.lbl_link_action.setText(_translate("ProfileSettingsDialog", "After Profile:"))
        self.lbl_link_to.setText(_translate("ProfileSettingsDialog", "Link To:"))
        self.gbox_segment_1.setTitle(_translate("ProfileSettingsDialog", "Segment 1:"))
        self.lbl_stpt_1.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_1.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_1.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_2.setTitle(_translate("ProfileSettingsDialog", "Segment 2:"))
        self.lbl_stpt_2.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_2.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_2.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_3.setTitle(_translate("ProfileSettingsDialog", "Segment 3:"))
        self.lbl_stpt_3.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_3.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_3.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_4.setTitle(_translate("ProfileSettingsDialog", "Segment 4:"))
        self.lbl_stpt_4.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_4.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_4.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_5.setTitle(_translate("ProfileSettingsDialog", "Segment 5"))
        self.lbl_stpt_5.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_5.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_5.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_6.setTitle(_translate("ProfileSettingsDialog", "Segment 6:"))
        self.lbl_stpt_6.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_6.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_6.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_7.setTitle(_translate("ProfileSettingsDialog", "Segment 7:"))
        self.lbl_stpt_7.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_7.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_7.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.gbox_segment_8.setTitle(_translate("ProfileSettingsDialog", "Segment 8:"))
        self.lbl_stpt_8.setText(_translate("ProfileSettingsDialog", "Setpoint:"))
        self.check_ramp_8.setText(_translate("ProfileSettingsDialog", "Ramp Time:"))
        self.check_dwell_8.setText(_translate("ProfileSettingsDialog", "Dwell Time:"))
        self.btn_reload_profile.setText(_translate("ProfileSettingsDialog", "Reload Profile"))
        self.btn_ok.setText(_translate("ProfileSettingsDialog", "Ok"))
        self.btn_apply.setText(_translate("ProfileSettingsDialog", "Apply"))
        self.btn_cancel.setText(_translate("ProfileSettingsDialog", "Cancel"))

