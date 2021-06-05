#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
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

def get_next_datapoint():
    '''Returns current x and y of the mobile beacon'''
    while True:
        try:
            hedge.dataEvent.wait(1)
            hedge.dataEvent.clear()
            if (hedge.positionUpdated):
                _,x,y,z,_,TimeStamp = hedge.position()  # BeaconID, X, Y, Z, Angle, Timestamp
                # hedge.print_position()
                return float(x),float(y)
        except KeyboardInterrupt:
            hedge.stop()  
            sys.exit()

if __name__ == "__main__":
    import sys
    # Mainwindow setup
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MyGUI =  GUI.Ui_MainWindow()
    MyGUI.setupUi(MainWindow)

    # Interface here
    myFig = LiveFigure(x_range=[0, 5], y_range=[0, 5], func=get_next_datapoint, interval=20)
    MyGUI.live_visualization_window.addWidget(myFig)

    # show
    MainWindow.show()
    sys.exit(app.exec_())