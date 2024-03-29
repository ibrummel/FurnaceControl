# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\main_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 800)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbox_log_setup = QtWidgets.QGroupBox(MainWindow)
        self.gbox_log_setup.setObjectName("gbox_log_setup")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gbox_log_setup)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.check_enable_logging = QtWidgets.QCheckBox(self.gbox_log_setup)
        self.check_enable_logging.setChecked(True)
        self.check_enable_logging.setObjectName("check_enable_logging")
        self.verticalLayout_7.addWidget(self.check_enable_logging)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
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
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.btn_logging_state = QtWidgets.QPushButton(self.gbox_log_setup)
        self.btn_logging_state.setObjectName("btn_logging_state")
        self.verticalLayout_7.addWidget(self.btn_logging_state)
        self.verticalLayout.addWidget(self.gbox_log_setup)
        self.gbox_profile_setup = QtWidgets.QGroupBox(MainWindow)
        self.gbox_profile_setup.setObjectName("gbox_profile_setup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gbox_profile_setup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.profile_editor = ProfileSettingsDialog(self.gbox_profile_setup)
        self.profile_editor.setObjectName("profile_editor")
        self.verticalLayout_5.addWidget(self.profile_editor)
        self.verticalLayout.addWidget(self.gbox_profile_setup)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupbox_controller_temp)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_controller_temp = QtWidgets.QLabel(self.groupbox_controller_temp)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_controller_temp.setFont(font)
        self.lbl_controller_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_controller_temp.setObjectName("lbl_controller_temp")
        self.verticalLayout_4.addWidget(self.lbl_controller_temp)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupbox_controller_temp)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.combo_controller_tc = QtWidgets.QComboBox(self.groupbox_controller_temp)
        self.combo_controller_tc.setObjectName("combo_controller_tc")
        self.horizontalLayout_4.addWidget(self.combo_controller_tc)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9.addWidget(self.groupbox_controller_temp)
        self.groupbox_external_temp = QtWidgets.QGroupBox(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_external_temp.setFont(font)
        self.groupbox_external_temp.setObjectName("groupbox_external_temp")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox_external_temp)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_external_temp = QtWidgets.QLabel(self.groupbox_external_temp)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_external_temp.setFont(font)
        self.lbl_external_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_external_temp.setObjectName("lbl_external_temp")
        self.verticalLayout_3.addWidget(self.lbl_external_temp)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupbox_external_temp)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.combo_monitor_tc = QtWidgets.QComboBox(self.groupbox_external_temp)
        self.combo_monitor_tc.setObjectName("combo_monitor_tc")
        self.horizontalLayout_3.addWidget(self.combo_monitor_tc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9.addWidget(self.groupbox_external_temp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.live_plot = FurnacePlotWidget(MainWindow)
        self.live_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.live_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.live_plot.setObjectName("live_plot")
        self.verticalLayout_2.addWidget(self.live_plot)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(MainWindow)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tbutton_manual_control = QtWidgets.QToolButton(self.groupBox)
        self.tbutton_manual_control.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/img/manual_control.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbutton_manual_control.setIcon(icon)
        self.tbutton_manual_control.setIconSize(QtCore.QSize(50, 50))
        self.tbutton_manual_control.setObjectName("tbutton_manual_control")
        self.horizontalLayout_5.addWidget(self.tbutton_manual_control)
        self.tbutton_manual_readout = QtWidgets.QToolButton(self.groupBox)
        self.tbutton_manual_readout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("src/img/manual_readout.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbutton_manual_readout.setIcon(icon1)
        self.tbutton_manual_readout.setIconSize(QtCore.QSize(50, 50))
        self.tbutton_manual_readout.setObjectName("tbutton_manual_readout")
        self.horizontalLayout_5.addWidget(self.tbutton_manual_readout)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_start_run = QtWidgets.QPushButton(MainWindow)
        self.btn_start_run.setObjectName("btn_start_run")
        self.horizontalLayout.addWidget(self.btn_start_run)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.gbox_log_setup.setTitle(_translate("MainWindow", "Logging Setup:"))
        self.check_enable_logging.setText(_translate("MainWindow", "Enable Temperature Logging"))
        self.lbl_log_interval.setText(_translate("MainWindow", "Interval (s):"))
        self.lbl_log_notes.setText(_translate("MainWindow", "Notes:"))
        self.lbl_log_file.setText(_translate("MainWindow", "Log File:"))
        self.btn_log_file.setText(_translate("MainWindow", "..."))
        self.btn_logging_state.setText(_translate("MainWindow", "Start Logging"))
        self.gbox_profile_setup.setTitle(_translate("MainWindow", "Furnace Profile Setup:"))
        self.groupbox_controller_temp.setTitle(_translate("MainWindow", "Controller Temperature:"))
        self.lbl_controller_temp.setText(_translate("MainWindow", "Temp Not Read"))
        self.label_5.setText(_translate("MainWindow", "Thermocouple Type:"))
        self.combo_controller_tc.setToolTip(_translate("MainWindow", "Set the thermocouple type for the furnace controller"))
        self.groupbox_external_temp.setTitle(_translate("MainWindow", "External Monitor Temperature:"))
        self.lbl_external_temp.setText(_translate("MainWindow", "Temp Not Read"))
        self.label_4.setText(_translate("MainWindow", "Thermocouple Type:"))
        self.combo_monitor_tc.setToolTip(_translate("MainWindow", "Set the thermocouple type for the external thermocouple (connected to NI TC01 reader)"))
        self.groupBox.setTitle(_translate("MainWindow", "Manual Tools:"))
        self.tbutton_manual_control.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open manual furnace control window...</p></body></html>"))
        self.tbutton_manual_readout.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open value readout builder dialog...</p></body></html>"))
        self.btn_start_run.setToolTip(_translate("MainWindow", "Start furnace run with automatic preheat and thermocouple switchover function"))
        self.btn_start_run.setText(_translate("MainWindow", "Start Furnace Run"))

from Furnace_Plot_Widget import FurnacePlotWidget
from Profile_Settings_Dialog import ProfileSettingsDialog
