#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('../')
import datetime
# PyQt library
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
# MarvelmindHedge
from MarvelmindRobotics.src.marvelmind import MarvelmindHedge # Submodule provided by Marvelmind
# GUI window
import GUI_Window as GUI # Created by PyQt5 UI code generator
# scripts
from scripts.live_plotter import LivePlotter
from scripts.origin_plotter import OriginPlotter 
from scripts.waypoint_plotter import WaypointPlotter
from scripts.record_plotter import RecordPlotter 

# Creating MarvelmindHedge thread
hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # "/dev/ttyACM0" is serial port address
hedge.daemon = True # kills thread when main program terminates
hedge.start() # start thread

def save_function(MyGUI):
        content = [0.1, 0.1, 0.1]
        # text box input
        qfd = QFileDialog()
        typed = MyGUI.setorigin_saveorigin_filename.text()
        fname, ok2 = QFileDialog.getSaveFileName(qfd,typed,os.getcwd(),"Text Files (*.txt)")#"All Files (*);;Text Files (*.txt)" "./"
        f = open(fname, "a")
        f.writelines(str(content))
        f.close()
        

def directory_fetch(MyGUI):
        #print("key is pressed")
        qfd = QFileDialog()
        #To open the directory
        fileName1, filetype = QFileDialog.getOpenFileName(qfd,"Select File",os.getcwd(),"All Files (*);;Text Files (*.txt)") 
        #print(fileName1,filetype)
        f = open(fileName1, "r")
        origin = f.read()
        # print(origin)
        f.close()
        # check = "it work"
        # return check
        '''
        Popup window 
        asd = QMessageBox()
        QMessageBox.question(asd, 'Message - pythonspot.com', "You typed: " + typed, QMessageBox.Ok, QMessageBox.Ok)'''

def set_origin(coordinates):
    Origin = coordinates
    # originFig.update_origin(Origin)

def reset_origin():
    Origin = [0.0, 0.0, 0.0]
    # originFig.update_origin(Origin)

if __name__ == "__main__": 
    import sys
    ''' Mainwindow setup '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MyGUI =  GUI.Ui_MainWindow()
    MyGUI.setupUi(MainWindow)

    ''' Interface here '''
    # Live Tab
    liveFig = LivePlotter(hedge,MyGUI)
    MyGUI.live_visualization_window.addWidget(liveFig)
    MyGUI.live_visualization_enable.stateChanged.connect(liveFig.toggle_live_visualization)
    MyGUI.live_buffersize_comboBox.activated[str].connect(liveFig.set_buffersize)
    
    # Set Origin Tab
    originFig = OriginPlotter(hedge,MyGUI)
    MyGUI.setorigin_visualization_window.addWidget(originFig)
    MyGUI.setorigin_visualization_enable.stateChanged.connect(originFig.toggle_live_visualization)
    MyGUI.setorigin_setorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: set_origin(Origin,hedge.position()[1:4],originFig))
    MyGUI.setorigin_setorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(lambda: reset_origin(Origin,originFig))
    MyGUI.setorigin_loadorigin_open_button.clicked.connect(lambda check: directory_fetch(MyGUI))#open button
    MyGUI.setorigin_saveorigin_save_button.clicked.connect(lambda:save_function(MyGUI))#save button
    
    # Waypoint Tab
    waypointFig = WaypointPlotter(hedge,MyGUI)
    MyGUI.waypoint_visualization_window.addWidget(waypointFig)
    MyGUI.waypoint_pinwaypoint_button.clicked.connect(waypointFig.recordstart)
    MyGUI.waypoint_stop_button.clicked.connect(waypointFig.recordstop)

    # Record Tab
    recordFig = RecordPlotter(hedge,MyGUI)
    MyGUI.record_visualization_window.addWidget(recordFig)
    MyGUI.record_recordstart_button.clicked.connect(recordFig.recordstart)
    MyGUI.record_recordstop_button.clicked.connect(recordFig.recordstop)
    MyGUI.record_recordclear_button.clicked.connect(recordFig.clearplot)
    
    # Compare Tab
    
    # Configure Tab
    
    ''' Show window '''
    MainWindow.show()
    sys.exit(app.exec_())