#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
import numpy as np
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
# MarvelmindHedge
from MarvelmindRobotics.src.marvelmind import MarvelmindHedge # Submodule provided by Marvelmind
# GUI window
import GUI_Window as GUI # Created by PyQt5 UI code generator
# scripts
from scripts.live_plotter import LiveFigure 

# Creating MarvelmindHedge thread
# hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # "/dev/ttyACM0" is serial port address
# hedge.daemon = True # kills thread when main program terminates
# hedge.start() # start thread

class dummyhedge():
    def __init__(self) -> None:
        self.ite = 0

    def position(self):
        id = 2
        x = np.random.randint(-15,15)+self.ite
        y = np.random.randint(10,20)+self.ite
        z = np.random.randint(10,20)+self.ite
        angle = 0
        timestamp = self.ite
        self.ite = self.ite+0.1
        return [id,x,y,z,angle,timestamp]

class AppContext(ApplicationContext):          
    def run(self):                              
        MainWindow = QMainWindow()
        version = self.build_settings['version']
        # Setup the QT components in the main window
        self.MyGUI =  GUI.Ui_MainWindow()
        self.MyGUI.setupUi(MainWindow)

        # Interface here
        d = dummyhedge() ######
        self.myliveFig = LiveFigure(d) ######
        # self.myliveFig = LiveFigure(hedge)
        self.MyGUI.live_visualization_window.addWidget(self.myliveFig)
        self.MyGUI.live_visualization_enable.stateChanged.connect(self.myliveFig.toggle_live_visualization)
        self.MyGUI.live_buffersize_comboBox.activated[str].connect(self.myliveFig.set_buffersize)

        # Show
        MainWindow.show()
        return self.app.exec_()

if __name__ == "__main__":
    appctxt = AppContext()          # Initialize           
    exit_code = appctxt.run()       # Run           
    sys.exit(exit_code)