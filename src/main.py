#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
# MarvelmindHedge
from MarvelmindRobotics.src.marvelmind import MarvelmindHedge # Submodule provided by Marvelmind
# GUI window
import GUI_Window as GUI # Created by PyQt5 UI code generator
# scripts
from scripts.live_plotter import LiveFigure 

# Creating MarvelmindHedge thread
hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # "/dev/ttyACM0" is serial port address
hedge.daemon = True # kills thread when main program terminates
hedge.start() # start thread

if __name__ == "__main__": 
    import sys
    # Mainwindow setup
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MyGUI =  GUI.Ui_MainWindow()
    MyGUI.setupUi(MainWindow)

    # Interface here

    # Live Tab
    myliveFig = LiveFigure(hedge,MyGUI)
    MyGUI.live_visualization_window.addWidget(myliveFig)
    MyGUI.live_visualization_enable.stateChanged.connect(myliveFig.toggle_live_visualization)
    MyGUI.live_buffersize_comboBox.activated[str].connect(myliveFig.set_buffersize)
    
    # Set Origin



    # Record Tab

    # Compare

    # Configure

    # Show window
    MainWindow.show()
    sys.exit(app.exec_())