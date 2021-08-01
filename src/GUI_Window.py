# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/Qt_design/GUI_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.live_tab = QtWidgets.QWidget()
        self.live_tab.setObjectName("live_tab")
        self.live_label_visualization_window = QtWidgets.QLabel(self.live_tab)
        self.live_label_visualization_window.setGeometry(QtCore.QRect(720, 70, 161, 25))
        self.live_label_visualization_window.setObjectName("live_label_visualization_window")
        self.live_buffersize_comboBox = QtWidgets.QComboBox(self.live_tab)
        self.live_buffersize_comboBox.setGeometry(QtCore.QRect(270, 180, 93, 33))
        self.live_buffersize_comboBox.setEditable(True)
        self.live_buffersize_comboBox.setObjectName("live_buffersize_comboBox")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_buffersize_comboBox.addItem("")
        self.live_visualization_enable = QtWidgets.QCheckBox(self.live_tab)
        self.live_visualization_enable.setGeometry(QtCore.QRect(50, 80, 231, 31))
        self.live_visualization_enable.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.live_visualization_enable.setChecked(False)
        self.live_visualization_enable.setObjectName("live_visualization_enable")
        self.live_label_buffersize = QtWidgets.QLabel(self.live_tab)
        self.live_label_buffersize.setGeometry(QtCore.QRect(60, 180, 111, 25))
        self.live_label_buffersize.setObjectName("live_label_buffersize")
        self.live_coordinates_groupBox = QtWidgets.QGroupBox(self.live_tab)
        self.live_coordinates_groupBox.setGeometry(QtCore.QRect(80, 410, 231, 171))
        self.live_coordinates_groupBox.setObjectName("live_coordinates_groupBox")
        self.live_hedge_id = QtWidgets.QLabel(self.live_coordinates_groupBox)
        self.live_hedge_id.setGeometry(QtCore.QRect(10, 40, 221, 25))
        self.live_hedge_id.setObjectName("live_hedge_id")
        self.live_coordiantes_x = QtWidgets.QLabel(self.live_coordinates_groupBox)
        self.live_coordiantes_x.setGeometry(QtCore.QRect(10, 70, 221, 25))
        self.live_coordiantes_x.setObjectName("live_coordiantes_x")
        self.live_coordiantes_y = QtWidgets.QLabel(self.live_coordinates_groupBox)
        self.live_coordiantes_y.setGeometry(QtCore.QRect(10, 100, 221, 25))
        self.live_coordiantes_y.setObjectName("live_coordiantes_y")
        self.live_coordiantes_z = QtWidgets.QLabel(self.live_coordinates_groupBox)
        self.live_coordiantes_z.setGeometry(QtCore.QRect(10, 130, 221, 25))
        self.live_coordiantes_z.setObjectName("live_coordiantes_z")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.live_tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(430, 110, 741, 471))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.live_visualization_window = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.live_visualization_window.setContentsMargins(0, 0, 0, 0)
        self.live_visualization_window.setObjectName("live_visualization_window")
        self.tabWidget.addTab(self.live_tab, "")
        self.set_origin_tab = QtWidgets.QWidget()
        self.set_origin_tab.setObjectName("set_origin_tab")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.set_origin_tab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(610, 40, 611, 351))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.setorigin_visualization_window = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.setorigin_visualization_window.setContentsMargins(0, 0, 0, 0)
        self.setorigin_visualization_window.setObjectName("setorigin_visualization_window")
        self.setorigin_label_visualization_window = QtWidgets.QLabel(self.set_origin_tab)
        self.setorigin_label_visualization_window.setGeometry(QtCore.QRect(840, 10, 161, 25))
        self.setorigin_label_visualization_window.setObjectName("setorigin_label_visualization_window")
        self.setorigin_origincoordinates_groupBox = QtWidgets.QGroupBox(self.set_origin_tab)
        self.setorigin_origincoordinates_groupBox.setGeometry(QtCore.QRect(610, 410, 401, 61))
        self.setorigin_origincoordinates_groupBox.setObjectName("setorigin_origincoordinates_groupBox")
        self.setorigin_orgin_coordiantes_x = QtWidgets.QLabel(self.setorigin_origincoordinates_groupBox)
        self.setorigin_orgin_coordiantes_x.setGeometry(QtCore.QRect(10, 30, 81, 25))
        self.setorigin_orgin_coordiantes_x.setObjectName("setorigin_orgin_coordiantes_x")
        self.setorigin_orgin_coordiantes_y = QtWidgets.QLabel(self.setorigin_origincoordinates_groupBox)
        self.setorigin_orgin_coordiantes_y.setGeometry(QtCore.QRect(150, 30, 81, 25))
        self.setorigin_orgin_coordiantes_y.setObjectName("setorigin_orgin_coordiantes_y")
        self.setorigin_orgin_coordiantes_z = QtWidgets.QLabel(self.setorigin_origincoordinates_groupBox)
        self.setorigin_orgin_coordiantes_z.setGeometry(QtCore.QRect(290, 30, 81, 25))
        self.setorigin_orgin_coordiantes_z.setObjectName("setorigin_orgin_coordiantes_z")
        self.setorigin_transformedcoordinates_groupBox = QtWidgets.QGroupBox(self.set_origin_tab)
        self.setorigin_transformedcoordinates_groupBox.setGeometry(QtCore.QRect(990, 490, 221, 121))
        self.setorigin_transformedcoordinates_groupBox.setObjectName("setorigin_transformedcoordinates_groupBox")
        self.setorigin_transformedcoordinates_x = QtWidgets.QLabel(self.setorigin_transformedcoordinates_groupBox)
        self.setorigin_transformedcoordinates_x.setGeometry(QtCore.QRect(10, 30, 81, 25))
        self.setorigin_transformedcoordinates_x.setObjectName("setorigin_transformedcoordinates_x")
        self.setorigin_transformedcoordinates_y = QtWidgets.QLabel(self.setorigin_transformedcoordinates_groupBox)
        self.setorigin_transformedcoordinates_y.setGeometry(QtCore.QRect(10, 60, 81, 25))
        self.setorigin_transformedcoordinates_y.setObjectName("setorigin_transformedcoordinates_y")
        self.setorigin_transformedcoordinates_z = QtWidgets.QLabel(self.setorigin_transformedcoordinates_groupBox)
        self.setorigin_transformedcoordinates_z.setGeometry(QtCore.QRect(10, 90, 81, 25))
        self.setorigin_transformedcoordinates_z.setObjectName("setorigin_transformedcoordinates_z")
        self.setorigin_rawcoordinates_groupBox = QtWidgets.QGroupBox(self.set_origin_tab)
        self.setorigin_rawcoordinates_groupBox.setGeometry(QtCore.QRect(610, 490, 211, 121))
        self.setorigin_rawcoordinates_groupBox.setObjectName("setorigin_rawcoordinates_groupBox")
        self.setorigin_rawcoordinates_x = QtWidgets.QLabel(self.setorigin_rawcoordinates_groupBox)
        self.setorigin_rawcoordinates_x.setGeometry(QtCore.QRect(10, 30, 81, 25))
        self.setorigin_rawcoordinates_x.setObjectName("setorigin_rawcoordinates_x")
        self.setorigin_rawcoordinates_y = QtWidgets.QLabel(self.setorigin_rawcoordinates_groupBox)
        self.setorigin_rawcoordinates_y.setGeometry(QtCore.QRect(10, 60, 81, 25))
        self.setorigin_rawcoordinates_y.setObjectName("setorigin_rawcoordinates_y")
        self.setorigin_rawcoordinates_z = QtWidgets.QLabel(self.setorigin_rawcoordinates_groupBox)
        self.setorigin_rawcoordinates_z.setGeometry(QtCore.QRect(10, 90, 81, 25))
        self.setorigin_rawcoordinates_z.setObjectName("setorigin_rawcoordinates_z")
        self.setorigin_setorigin_groupBox = QtWidgets.QGroupBox(self.set_origin_tab)
        self.setorigin_setorigin_groupBox.setGeometry(QtCore.QRect(70, 100, 491, 131))
        self.setorigin_setorigin_groupBox.setObjectName("setorigin_setorigin_groupBox")
        self.setorigin_label_setorigin = QtWidgets.QLabel(self.setorigin_setorigin_groupBox)
        self.setorigin_label_setorigin.setGeometry(QtCore.QRect(10, 50, 291, 25))
        self.setorigin_label_setorigin.setObjectName("setorigin_label_setorigin")
        self.setorigin_setorigin_dialogbuttons = QtWidgets.QDialogButtonBox(self.setorigin_setorigin_groupBox)
        self.setorigin_setorigin_dialogbuttons.setGeometry(QtCore.QRect(0, 80, 491, 31))
        self.setorigin_setorigin_dialogbuttons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setorigin_setorigin_dialogbuttons.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.setorigin_setorigin_dialogbuttons.setCenterButtons(True)
        self.setorigin_setorigin_dialogbuttons.setObjectName("setorigin_setorigin_dialogbuttons")
        self.setorigin_saveorigin_groupBox = QtWidgets.QGroupBox(self.set_origin_tab)
        self.setorigin_saveorigin_groupBox.setGeometry(QtCore.QRect(70, 260, 491, 131))
        self.setorigin_saveorigin_groupBox.setObjectName("setorigin_saveorigin_groupBox")
        self.setorigin_saveorigin_filename = QtWidgets.QLineEdit(self.setorigin_saveorigin_groupBox)
        self.setorigin_saveorigin_filename.setGeometry(QtCore.QRect(160, 80, 171, 31))
        self.setorigin_saveorigin_filename.setObjectName("setorigin_saveorigin_filename")
        self.setorigin_label_filename = QtWidgets.QLabel(self.setorigin_saveorigin_groupBox)
        self.setorigin_label_filename.setGeometry(QtCore.QRect(20, 80, 121, 25))
        self.setorigin_label_filename.setObjectName("setorigin_label_filename")
        self.setorigin_saveorigin_save_button = QtWidgets.QDialogButtonBox(self.setorigin_saveorigin_groupBox)
        self.setorigin_saveorigin_save_button.setGeometry(QtCore.QRect(385, 80, 81, 33))
        self.setorigin_saveorigin_save_button.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.setorigin_saveorigin_save_button.setObjectName("setorigin_saveorigin_save_button")
        self.setorigin_label_saveorigin = QtWidgets.QLabel(self.setorigin_saveorigin_groupBox)
        self.setorigin_label_saveorigin.setGeometry(QtCore.QRect(20, 40, 291, 25))
        self.setorigin_label_saveorigin.setObjectName("setorigin_label_saveorigin")
        self.setorigin_visualization_enable = QtWidgets.QCheckBox(self.set_origin_tab)
        self.setorigin_visualization_enable.setGeometry(QtCore.QRect(70, 60, 231, 31))
        self.setorigin_visualization_enable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setorigin_visualization_enable.setObjectName("setorigin_visualization_enable")
        self.setorigin_loadorigin_groupBox = QtWidgets.QGroupBox(self.set_origin_tab)
        self.setorigin_loadorigin_groupBox.setGeometry(QtCore.QRect(70, 430, 491, 131))
        self.setorigin_loadorigin_groupBox.setObjectName("setorigin_loadorigin_groupBox")
        self.setorigin_label_loadorigin = QtWidgets.QLabel(self.setorigin_loadorigin_groupBox)
        self.setorigin_label_loadorigin.setGeometry(QtCore.QRect(20, 40, 291, 25))
        self.setorigin_label_loadorigin.setObjectName("setorigin_label_loadorigin")
        self.setorigin_loadorigin_open_button = QtWidgets.QDialogButtonBox(self.setorigin_loadorigin_groupBox)
        self.setorigin_loadorigin_open_button.setGeometry(QtCore.QRect(390, 40, 81, 33))
        self.setorigin_loadorigin_open_button.setStandardButtons(QtWidgets.QDialogButtonBox.Open)
        self.setorigin_loadorigin_open_button.setObjectName("setorigin_loadorigin_open_button")
        self.setorigin_loadorigin_dialogbuttons = QtWidgets.QDialogButtonBox(self.setorigin_loadorigin_groupBox)
        self.setorigin_loadorigin_dialogbuttons.setGeometry(QtCore.QRect(310, 90, 166, 33))
        self.setorigin_loadorigin_dialogbuttons.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.setorigin_loadorigin_dialogbuttons.setObjectName("setorigin_loadorigin_dialogbuttons")
        self.setorigin_restore_button = QtWidgets.QDialogButtonBox(self.set_origin_tab)
        self.setorigin_restore_button.setGeometry(QtCore.QRect(1060, 440, 166, 33))
        self.setorigin_restore_button.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.setorigin_restore_button.setObjectName("setorigin_restore_button")
        self.tabWidget.addTab(self.set_origin_tab, "")
        self.waypoint_tab = QtWidgets.QWidget()
        self.waypoint_tab.setObjectName("waypoint_tab")
        self.tabWidget.addTab(self.waypoint_tab, "")
        self.record_tab = QtWidgets.QWidget()
        self.record_tab.setObjectName("record_tab")
        self.record_robot_comboBox = QtWidgets.QComboBox(self.record_tab)
        self.record_robot_comboBox.setGeometry(QtCore.QRect(290, 100, 91, 33))
        self.record_robot_comboBox.setEditable(True)
        self.record_robot_comboBox.setObjectName("record_robot_comboBox")
        self.record_robot_comboBox.addItem("")
        self.record_robot_comboBox.addItem("")
        self.record_robot_comboBox.addItem("")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.record_tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(500, 50, 741, 471))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.record_visualization_window = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.record_visualization_window.setContentsMargins(0, 0, 0, 0)
        self.record_visualization_window.setObjectName("record_visualization_window")
        self.record_label_visualization_window = QtWidgets.QLabel(self.record_tab)
        self.record_label_visualization_window.setGeometry(QtCore.QRect(830, 20, 161, 25))
        self.record_label_visualization_window.setObjectName("record_label_visualization_window")
        self.record_label_robot_select = QtWidgets.QLabel(self.record_tab)
        self.record_label_robot_select.setGeometry(QtCore.QRect(70, 110, 111, 25))
        self.record_label_robot_select.setObjectName("record_label_robot_select")
        self.record_run_comboBox = QtWidgets.QComboBox(self.record_tab)
        self.record_run_comboBox.setGeometry(QtCore.QRect(290, 160, 93, 33))
        self.record_run_comboBox.setEditable(True)
        self.record_run_comboBox.setObjectName("record_run_comboBox")
        self.record_run_comboBox.addItem("")
        self.record_run_comboBox.addItem("")
        self.record_run_comboBox.addItem("")
        self.record_label_run_select = QtWidgets.QLabel(self.record_tab)
        self.record_label_run_select.setGeometry(QtCore.QRect(70, 170, 111, 25))
        self.record_label_run_select.setObjectName("record_label_run_select")
        self.record_coordinates_groupBox = QtWidgets.QGroupBox(self.record_tab)
        self.record_coordinates_groupBox.setGeometry(QtCore.QRect(70, 300, 231, 171))
        self.record_coordinates_groupBox.setObjectName("record_coordinates_groupBox")
        self.record_timestamp = QtWidgets.QLabel(self.record_coordinates_groupBox)
        self.record_timestamp.setGeometry(QtCore.QRect(10, 40, 101, 25))
        self.record_timestamp.setObjectName("record_timestamp")
        self.record_coordiantes_x = QtWidgets.QLabel(self.record_coordinates_groupBox)
        self.record_coordiantes_x.setGeometry(QtCore.QRect(10, 70, 81, 25))
        self.record_coordiantes_x.setObjectName("record_coordiantes_x")
        self.record_coordiantes_y = QtWidgets.QLabel(self.record_coordinates_groupBox)
        self.record_coordiantes_y.setGeometry(QtCore.QRect(10, 100, 81, 25))
        self.record_coordiantes_y.setObjectName("record_coordiantes_y")
        self.record_coordiantes_z = QtWidgets.QLabel(self.record_coordinates_groupBox)
        self.record_coordiantes_z.setGeometry(QtCore.QRect(10, 130, 81, 25))
        self.record_coordiantes_z.setObjectName("record_coordiantes_z")
        self.record_recordstart_button = QtWidgets.QPushButton(self.record_tab)
        self.record_recordstart_button.setGeometry(QtCore.QRect(660, 580, 96, 33))
        self.record_recordstart_button.setObjectName("record_recordstart_button")
        self.record_recordstop_button = QtWidgets.QPushButton(self.record_tab)
        self.record_recordstop_button.setGeometry(QtCore.QRect(780, 580, 96, 33))
        self.record_recordstop_button.setObjectName("record_recordstop_button")
        self.record_timer_enable = QtWidgets.QCheckBox(self.record_tab)
        self.record_timer_enable.setGeometry(QtCore.QRect(40, 570, 221, 31))
        self.record_timer_enable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.record_timer_enable.setObjectName("record_timer_enable")
        self.record_timer_value = QtWidgets.QDoubleSpinBox(self.record_tab)
        self.record_timer_value.setGeometry(QtCore.QRect(260, 570, 74, 34))
        self.record_timer_value.setObjectName("record_timer_value")
        self.tabWidget.addTab(self.record_tab, "")
        self.compare_tab = QtWidgets.QWidget()
        self.compare_tab.setObjectName("compare_tab")
        self.compare_firsttrajectory_comboBox = QtWidgets.QComboBox(self.compare_tab)
        self.compare_firsttrajectory_comboBox.setGeometry(QtCore.QRect(300, 10, 601, 33))
        self.compare_firsttrajectory_comboBox.setEditable(False)
        self.compare_firsttrajectory_comboBox.setObjectName("compare_firsttrajectory_comboBox")
        self.compare_label_firsttrajectory = QtWidgets.QLabel(self.compare_tab)
        self.compare_label_firsttrajectory.setGeometry(QtCore.QRect(90, 20, 161, 25))
        self.compare_label_firsttrajectory.setObjectName("compare_label_firsttrajectory")
        self.compare_secondtrajectory_comboBox = QtWidgets.QComboBox(self.compare_tab)
        self.compare_secondtrajectory_comboBox.setGeometry(QtCore.QRect(300, 60, 601, 33))
        self.compare_secondtrajectory_comboBox.setEditable(False)
        self.compare_secondtrajectory_comboBox.setObjectName("compare_secondtrajectory_comboBox")
        self.compare_label_secondtrajectory = QtWidgets.QLabel(self.compare_tab)
        self.compare_label_secondtrajectory.setGeometry(QtCore.QRect(90, 60, 161, 25))
        self.compare_label_secondtrajectory.setObjectName("compare_label_secondtrajectory")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.compare_tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(480, 150, 741, 471))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.compare_visualization_window = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.compare_visualization_window.setContentsMargins(0, 0, 0, 0)
        self.compare_visualization_window.setObjectName("compare_visualization_window")
        self.compare_label_visualization_window = QtWidgets.QLabel(self.compare_tab)
        self.compare_label_visualization_window.setGeometry(QtCore.QRect(770, 110, 161, 25))
        self.compare_label_visualization_window.setObjectName("compare_label_visualization_window")
        self.comapare_comparetrajectories_button = QtWidgets.QPushButton(self.compare_tab)
        self.comapare_comparetrajectories_button.setGeometry(QtCore.QRect(1000, 60, 96, 33))
        self.comapare_comparetrajectories_button.setObjectName("comapare_comparetrajectories_button")
        self.compare_comparisonresult_groupBox = QtWidgets.QGroupBox(self.compare_tab)
        self.compare_comparisonresult_groupBox.setGeometry(QtCore.QRect(90, 240, 351, 261))
        self.compare_comparisonresult_groupBox.setObjectName("compare_comparisonresult_groupBox")
        self.compare_metrics = QtWidgets.QLabel(self.compare_comparisonresult_groupBox)
        self.compare_metrics.setGeometry(QtCore.QRect(20, 40, 81, 25))
        self.compare_metrics.setObjectName("compare_metrics")
        self.tabWidget.addTab(self.compare_tab, "")
        self.configure_tab = QtWidgets.QWidget()
        self.configure_tab.setObjectName("configure_tab")
        self.tabWidget.addTab(self.configure_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.live_buffersize_comboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.live_label_visualization_window.setText(_translate("MainWindow", "Mobile Beacon path"))
        self.live_buffersize_comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.live_buffersize_comboBox.setItemText(1, _translate("MainWindow", "10"))
        self.live_buffersize_comboBox.setItemText(2, _translate("MainWindow", "20"))
        self.live_buffersize_comboBox.setItemText(3, _translate("MainWindow", "50"))
        self.live_buffersize_comboBox.setItemText(4, _translate("MainWindow", "100"))
        self.live_buffersize_comboBox.setItemText(5, _translate("MainWindow", "1000"))
        self.live_buffersize_comboBox.setItemText(6, _translate("MainWindow", "2000"))
        self.live_buffersize_comboBox.setItemText(7, _translate("MainWindow", "5000"))
        self.live_buffersize_comboBox.setItemText(8, _translate("MainWindow", "10000"))
        self.live_visualization_enable.setText(_translate("MainWindow", "Show live Trajectory"))
        self.live_label_buffersize.setText(_translate("MainWindow", "Buffer Size"))
        self.live_coordinates_groupBox.setTitle(_translate("MainWindow", "GPS Coordinates"))
        self.live_hedge_id.setText(_translate("MainWindow", "Hedge ID"))
        self.live_coordiantes_x.setText(_translate("MainWindow", "X Value"))
        self.live_coordiantes_y.setText(_translate("MainWindow", "Y Value"))
        self.live_coordiantes_z.setText(_translate("MainWindow", "Z Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.live_tab), _translate("MainWindow", "Live"))
        self.setorigin_label_visualization_window.setText(_translate("MainWindow", "Mobile Beacon path"))
        self.setorigin_origincoordinates_groupBox.setTitle(_translate("MainWindow", "Current Origin Coordinates"))
        self.setorigin_orgin_coordiantes_x.setText(_translate("MainWindow", "X Value"))
        self.setorigin_orgin_coordiantes_y.setText(_translate("MainWindow", "Y Value"))
        self.setorigin_orgin_coordiantes_z.setText(_translate("MainWindow", "Z Value"))
        self.setorigin_transformedcoordinates_groupBox.setTitle(_translate("MainWindow", "Transformed Coordinates"))
        self.setorigin_transformedcoordinates_x.setText(_translate("MainWindow", "X Value"))
        self.setorigin_transformedcoordinates_y.setText(_translate("MainWindow", "Y Value"))
        self.setorigin_transformedcoordinates_z.setText(_translate("MainWindow", "Z Value"))
        self.setorigin_rawcoordinates_groupBox.setTitle(_translate("MainWindow", "Raw Coordinates"))
        self.setorigin_rawcoordinates_x.setText(_translate("MainWindow", "X Value"))
        self.setorigin_rawcoordinates_y.setText(_translate("MainWindow", "Y Value"))
        self.setorigin_rawcoordinates_z.setText(_translate("MainWindow", "Z Value"))
        self.setorigin_setorigin_groupBox.setTitle(_translate("MainWindow", "Set Origin"))
        self.setorigin_label_setorigin.setText(_translate("MainWindow", "Set Current Coordinates as origin"))
        self.setorigin_saveorigin_groupBox.setTitle(_translate("MainWindow", "Save Origin"))
        self.setorigin_label_filename.setText(_translate("MainWindow", "Enter Filename"))
        self.setorigin_label_saveorigin.setText(_translate("MainWindow", "Save Current origin as a file"))
        self.setorigin_visualization_enable.setText(_translate("MainWindow", "Show live Trajectory"))
        self.setorigin_loadorigin_groupBox.setTitle(_translate("MainWindow", "Load Origin"))
        self.setorigin_label_loadorigin.setText(_translate("MainWindow", "Load origin from a file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_origin_tab), _translate("MainWindow", "Set Origin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.waypoint_tab), _translate("MainWindow", "Waypoint"))
        self.record_robot_comboBox.setItemText(0, _translate("MainWindow", "Test Robot 1"))
        self.record_robot_comboBox.setItemText(1, _translate("MainWindow", "Test Robot 2"))
        self.record_robot_comboBox.setItemText(2, _translate("MainWindow", "Test Robot 3"))
        self.record_label_visualization_window.setText(_translate("MainWindow", "Mobile Beacon path"))
        self.record_label_robot_select.setText(_translate("MainWindow", "Select Robot"))
        self.record_run_comboBox.setCurrentText(_translate("MainWindow", "Test Run 1"))
        self.record_run_comboBox.setItemText(0, _translate("MainWindow", "Test Run 1"))
        self.record_run_comboBox.setItemText(1, _translate("MainWindow", "Test Run 2"))
        self.record_run_comboBox.setItemText(2, _translate("MainWindow", "Test Run 3"))
        self.record_label_run_select.setText(_translate("MainWindow", "Select Run"))
        self.record_coordinates_groupBox.setTitle(_translate("MainWindow", "GPS Coordinates"))
        self.record_timestamp.setText(_translate("MainWindow", "Time Stamp"))
        self.record_coordiantes_x.setText(_translate("MainWindow", "X Value"))
        self.record_coordiantes_y.setText(_translate("MainWindow", "Y Value"))
        self.record_coordiantes_z.setText(_translate("MainWindow", "Z Value"))
        self.record_recordstart_button.setText(_translate("MainWindow", "Record"))
        self.record_recordstop_button.setText(_translate("MainWindow", "Stop"))
        self.record_timer_enable.setText(_translate("MainWindow", "Auto stop Timer (sec)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.record_tab), _translate("MainWindow", "Record"))
        self.compare_label_firsttrajectory.setText(_translate("MainWindow", "First Trajectory"))
        self.compare_label_secondtrajectory.setText(_translate("MainWindow", "Second Trajectory"))
        self.compare_label_visualization_window.setText(_translate("MainWindow", "Mobile Beacon path"))
        self.comapare_comparetrajectories_button.setText(_translate("MainWindow", "Compare"))
        self.compare_comparisonresult_groupBox.setTitle(_translate("MainWindow", "Comparison Result"))
        self.compare_metrics.setText(_translate("MainWindow", "Metrics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.compare_tab), _translate("MainWindow", "Compare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configure_tab), _translate("MainWindow", "Configure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())