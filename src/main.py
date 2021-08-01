#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from time import sleep
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# MarvelmindHedge
from MarvelmindRobotics.src.marvelmind import MarvelmindHedge # Submodule provided by Marvelmind
# GUI window
import GUI_Window as GUI # Created by PyQt5 UI code generator
# scripts
# import scripts.live_plotter
from scripts.live_plotter import LiveFigure 
from scripts.live_plotter import LivePlotter
from scripts.origin_plotter import OriginPlotter 
from scripts.record_plotter import RecordPlotter 

# Creating MarvelmindHedge thread

import datetime

hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # "/dev/ttyACM0" is serial port address
hedge.daemon = True # kills thread when main program terminates
hedge.start() # start thread

def update_livetab_GPSCoordinates():
        '''Function to update GPS Coordinates display in Live tab'''
        position = hedge.position()
        hedge_id = "Hedge ID : "+str(position[0])
        x_value = "X : "+str(position[1])
        y_value = "Y : "+str(position[2])
        z_value = "Z : "+str(position[3])
        MyGUI.live_hedge_id.setText(hedge_id)
        MyGUI.live_coordiantes_x.setText(x_value)
        MyGUI.live_coordiantes_y.setText(y_value)
        MyGUI.live_coordiantes_z.setText(z_value)

def save_function(MyGUI):
        content = [0.0, 0.0, 0.0]
        typed = MyGUI.setorigin_saveorigin_filename.text()
        extension = ".txt"
        file_name = f"src/origin/"+ str(typed) + extension
        f = open(file_name, "a")
        f.writelines(str(content))
        f.close()

def directory_fetch(MyGUI):
        print("key is pressed")
        qfd = QFileDialog()
        fname = QFileDialog.getOpenFileName(qfd, 'Open file', 
         'Home:\\',filter="All files (*)")
        typed = MyGUI.setorigin_saveorigin_filename.text()
        print(typed)
        # asd = QMessageBox()
        # QMessageBox.question(asd, 'Message - pythonspot.com', "You typed: " + typed, QMessageBox.Ok, QMessageBox.Ok)

def recordstart(MyGUI):   
        current_date_and_time = datetime.datetime.now()
        extension = ".txt"
        filename = f"src/trajectories/"+ str(current_date_and_time) + extension
        f = open(filename, "a")
        while(True):
            hedge.dataEvent.wait(1)
            hedge.dataEvent.clear()
            if (hedge.positionUpdated):
                device_ID,x,y,z,angle,TimeStamp = hedge.position()  # BeaconID, X, Y, Z, Angle, Timestamp
                valuelist = []
                valuelist.append(device_ID)
                valuelist.append(x)
                valuelist.append(y)
                valuelist.append(z)
                valuelist.append(angle)
                valuelist.append(TimeStamp)
                f.write(str(valuelist))
                f.write('\n')

 
Origin = [0.0, 0.0, 0.0]

def set_origin(Origin,position,originFig):
    Origin = [float(position[0]), float(position[1]), float(position[2])]
    originFig.update_origin(Origin)

def reset_origin(Origin,originFig):
    Origin = [0.0, 0.0, 0.0]
    originFig.update_origin(Origin)


if __name__ == "__main__": 
    import sys
    # Mainwindow setup
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MyGUI =  GUI.Ui_MainWindow()
    MyGUI.setupUi(MainWindow)
    # Interface here

    # Live Tab
    liveFig = LivePlotter(hedge,MyGUI)
    MyGUI.live_visualization_window.addWidget(liveFig)
    MyGUI.live_visualization_enable.stateChanged.connect(liveFig.toggle_live_visualization)
    MyGUI.live_buffersize_comboBox.activated[str].connect(liveFig.set_buffersize)
    
    # Set Origin
    originFig = OriginPlotter(hedge,MyGUI, Origin)
    MyGUI.setorigin_visualization_window.addWidget(originFig)
    MyGUI.setorigin_visualization_enable.stateChanged.connect(originFig.toggle_live_visualization)
    MyGUI.setorigin_setorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: set_origin(Origin,hedge.position()[1:4],originFig))
    MyGUI.setorigin_setorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(lambda: reset_origin(Origin,originFig))
    MyGUI.setorigin_loadorigin_open_button.clicked.connect(lambda:directory_fetch(MyGUI))
    MyGUI.setorigin_saveorigin_save_button.clicked.connect(lambda:save_function(MyGUI))
    
    # Record Tab
    recordFig = RecordPlotter(hedge,MyGUI,Origin)
    MyGUI.record_visualization_window.addWidget(recordFig)
    MyGUI.record_recordstart_button.clicked.connect(recordFig.recordstart)
    MyGUI.record_recordstop_button.clicked.connect(recordFig.recordstop)
    MyGUI.record_recordstart_button.clicked.connect(lambda:recordstart(MyGUI))
    MyGUI.record_recordstop_button.clicked.connect(lambda:recordstart(MyGUI))
    # Compare
    
    # Configure
    
    # Show window
    MainWindow.show()

    sys.exit(app.exec_())













    
    

    



