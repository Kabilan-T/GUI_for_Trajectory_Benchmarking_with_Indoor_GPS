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

# class dummyhedge():
#     def __init__(self) -> None:
#         self.ite = 0

#     def position(self):
#         id = 2
#         x = np.random.randint(-15,15)+self.ite
#         y = np.random.randint(10,20)+self.ite
#         z = np.random.randint(10,20)+self.ite
#         angle = 0
#         timestamp = self.ite
#         self.ite = self.ite+0.1
#         return [id,x,y,z,angle,timestamp]
# hedge = dummyhedge() ######

def update_livetab_GPSCoordinates(MyGUI):
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


if __name__ == "__main__": 
    import sys
    # Mainwindow setup
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MyGUI =  GUI.Ui_MainWindow()
    MyGUI.setupUi(MainWindow)

    # Interface here
    myliveFig = LiveFigure(hedge)
    MyGUI.live_visualization_window.addWidget(myliveFig)
    MyGUI.live_visualization_enable.stateChanged.connect(myliveFig.toggle_live_visualization)
    MyGUI.live_buffersize_comboBox.activated[str].connect(myliveFig.set_buffersize)
    timer = QtCore.QTimer()
    # timer.timeout.connect(update_livetab_GPSCoordinates())
    timer.start(500)

    # Show window
    MainWindow.show()
    sys.exit(app.exec_())