# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1323, 761)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbox_temp = QtWidgets.QGroupBox(MainWindow)
        self.gbox_temp.setObjectName("gbox_temp")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gbox_temp)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.gbox_temp)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.combo_monitor_tc = QtWidgets.QComboBox(self.gbox_temp)
        self.combo_monitor_tc.setObjectName("combo_monitor_tc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_monitor_tc)
        self.label_5 = QtWidgets.QLabel(self.gbox_temp)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.combo_controller_tc = QtWidgets.QComboBox(self.gbox_temp)
        self.combo_controller_tc.setObjectName("combo_controller_tc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_controller_tc)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.gbox_log_setup = QtWidgets.QGroupBox(self.gbox_temp)
        self.gbox_log_setup.setObjectName("gbox_log_setup")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gbox_log_setup)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.check_enable_logging = QtWidgets.QCheckBox(self.gbox_log_setup)
        self.check_enable_logging.setChecked(True)
        self.check_enable_logging.setObjectName("check_enable_logging")
        self.verticalLayout_7.addWidget(self.check_enable_logging)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.lbl_log_file = QtWidgets.QLabel(self.gbox_log_setup)
        self.lbl_log_file.setObjectName("lbl_log_file")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_log_file)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_log_file = QtWidgets.QLineEdit(self.gbox_log_setup)
        self.line_log_file.setObjectName("line_log_file")
        self.horizontalLayout_6.addWidget(self.line_log_file)
        self.btn_log_file = QtWidgets.QPushButton(self.gbox_log_setup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_log_file.sizePolicy().hasHeightForWidth())
        self.btn_log_file.setSizePolicy(sizePolicy)
        self.btn_log_file.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_log_file.setObjectName("btn_log_file")
        self.horizontalLayout_6.addWidget(self.btn_log_file)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.lbl_log_interval = QtWidgets.QLabel(self.gbox_log_setup)
        self.lbl_log_interval.setObjectName("lbl_log_interval")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_log_interval)
        self.line_log_interval = QtWidgets.QLineEdit(self.gbox_log_setup)
        self.line_log_interval.setObjectName("line_log_interval")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_log_interval)
        self.lbl_log_notes = QtWidgets.QLabel(self.gbox_log_setup)
        self.lbl_log_notes.setObjectName("lbl_log_notes")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_log_notes)
        self.text_log_notes = QtWidgets.QTextEdit(self.gbox_log_setup)
        self.text_log_notes.setObjectName("text_log_notes")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.text_log_notes)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.verticalLayout_6.addWidget(self.gbox_log_setup)
        self.btn_logging_state = QtWidgets.QPushButton(self.gbox_temp)
        self.btn_logging_state.setObjectName("btn_logging_state")
        self.verticalLayout_6.addWidget(self.btn_logging_state)
        self.verticalLayout.addWidget(self.gbox_temp)
        self.gbox_output = QtWidgets.QGroupBox(MainWindow)
        self.gbox_output.setObjectName("gbox_output")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbox_output)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.gbox_output)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.combo_output_mode = QtWidgets.QComboBox(self.gbox_output)
        self.combo_output_mode.setObjectName("combo_output_mode")
        self.horizontalLayout_5.addWidget(self.combo_output_mode)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gbox_trim_setup = QtWidgets.QGroupBox(self.gbox_output)
        self.gbox_trim_setup.setObjectName("gbox_trim_setup")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.gbox_trim_setup)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_trim_reading1 = QtWidgets.QLineEdit(self.gbox_trim_setup)
        self.line_trim_reading1.setObjectName("line_trim_reading1")
        self.horizontalLayout_4.addWidget(self.line_trim_reading1)
        self.label = QtWidgets.QLabel(self.gbox_trim_setup)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.line_trim_output1 = QtWidgets.QLineEdit(self.gbox_trim_setup)
        self.line_trim_output1.setObjectName("line_trim_output1")
        self.horizontalLayout_4.addWidget(self.line_trim_output1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_trim_reading2 = QtWidgets.QLineEdit(self.gbox_trim_setup)
        self.line_trim_reading2.setObjectName("line_trim_reading2")
        self.horizontalLayout_3.addWidget(self.line_trim_reading2)
        self.label_2 = QtWidgets.QLabel(self.gbox_trim_setup)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_trim_output2 = QtWidgets.QLineEdit(self.gbox_trim_setup)
        self.line_trim_output2.setObjectName("line_trim_output2")
        self.horizontalLayout_3.addWidget(self.line_trim_output2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.gbox_trim_setup)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout.addWidget(self.gbox_output)
        self.gbox_profile = QtWidgets.QGroupBox(MainWindow)
        self.gbox_profile.setObjectName("gbox_profile")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gbox_profile)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.gbox_profile)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spin_profile_number = QtWidgets.QSpinBox(self.gbox_profile)
        self.spin_profile_number.setObjectName("spin_profile_number")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_profile_number)
        self.label_7 = QtWidgets.QLabel(self.gbox_profile)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.combo_profile_tracking = QtWidgets.QComboBox(self.gbox_profile)
        self.combo_profile_tracking.setObjectName("combo_profile_tracking")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_profile_tracking)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_edit_profile = QtWidgets.QPushButton(self.gbox_profile)
        self.btn_edit_profile.setObjectName("btn_edit_profile")
        self.horizontalLayout_7.addWidget(self.btn_edit_profile)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.gbox_profile)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 10)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupbox_controller_temp = QtWidgets.QGroupBox(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_controller_temp.setFont(font)
        self.groupbox_controller_temp.setFlat(False)
        self.groupbox_controller_temp.setObjectName("groupbox_controller_temp")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupbox_controller_temp)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_controller_temp = QtWidgets.QLabel(self.groupbox_controller_temp)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_controller_temp.setFont(font)
        self.lbl_controller_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_controller_temp.setObjectName("lbl_controller_temp")
        self.horizontalLayout_10.addWidget(self.lbl_controller_temp)
        self.horizontalLayout_9.addWidget(self.groupbox_controller_temp)
        self.groupbox_external_temp = QtWidgets.QGroupBox(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_external_temp.setFont(font)
        self.groupbox_external_temp.setObjectName("groupbox_external_temp")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupbox_external_temp)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbl_external_temp = QtWidgets.QLabel(self.groupbox_external_temp)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_external_temp.setFont(font)
        self.lbl_external_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_external_temp.setObjectName("lbl_external_temp")
        self.horizontalLayout_11.addWidget(self.lbl_external_temp)
        self.horizontalLayout_9.addWidget(self.groupbox_external_temp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.live_plot = FurnacePlotWidget(MainWindow)
        self.live_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.live_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.live_plot.setObjectName("live_plot")
        self.verticalLayout_2.addWidget(self.live_plot)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_start_run = QtWidgets.QPushButton(MainWindow)
        self.btn_start_run.setObjectName("btn_start_run")
        self.horizontalLayout.addWidget(self.btn_start_run)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.gbox_temp.setTitle(_translate("MainWindow", "Temperature Input Setup:"))
        self.label_4.setText(_translate("MainWindow", "Monitoring TC Type:"))
        self.label_5.setText(_translate("MainWindow", "Process Control TC Type: "))
        self.gbox_log_setup.setTitle(_translate("MainWindow", "Loging Setup:"))
        self.check_enable_logging.setText(_translate("MainWindow", "Enable Temperature Logging"))
        self.lbl_log_file.setText(_translate("MainWindow", "Log File:"))
        self.btn_log_file.setText(_translate("MainWindow", "..."))
        self.lbl_log_interval.setText(_translate("MainWindow", "Interval (s):"))
        self.lbl_log_notes.setText(_translate("MainWindow", "Notes:"))
        self.btn_logging_state.setText(_translate("MainWindow", "Start Logging"))
        self.gbox_output.setTitle(_translate("MainWindow", "Output Setup:"))
        self.label_3.setText(_translate("MainWindow", "Output Mode: "))
        self.gbox_trim_setup.setTitle(_translate("MainWindow", "Retransmission Output Trim:"))
        self.label.setText(_translate("MainWindow", "-->"))
        self.label_2.setText(_translate("MainWindow", "-->"))
        self.gbox_profile.setTitle(_translate("MainWindow", "Furnace Profile:"))
        self.label_6.setText(_translate("MainWindow", "Select Furnace Profile: "))
        self.label_7.setText(_translate("MainWindow", "Profile Tracking Mode: "))
        self.btn_edit_profile.setText(_translate("MainWindow", "Edit Profile"))
        self.groupbox_controller_temp.setTitle(_translate("MainWindow", "Controller T/C Temperature:"))
        self.lbl_controller_temp.setText(_translate("MainWindow", "Temp Not Read"))
        self.groupbox_external_temp.setTitle(_translate("MainWindow", "External T/C Temperature:"))
        self.lbl_external_temp.setText(_translate("MainWindow", "Temp Not Read"))
        self.btn_start_run.setText(_translate("MainWindow", "Start Furnace Run"))

from Furnace_Plot_Widget import FurnacePlotWidget
