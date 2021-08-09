#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('../')
import datetime
# PyQt library
from PyQt5 import QtWidgets
# MarvelmindHedge
from MarvelmindRobotics.src.marvelmind import MarvelmindHedge # Submodule provided by Marvelmind
# GUI window
import GUI_Window as GUI # Created by PyQt5 UI code generator
# scripts
from scripts.live_plotter import LivePlotter
from scripts.origin_plotter import OriginPlotter 
from scripts.waypoint_plotter import WaypointPlotter
from scripts.trajectory_plotter import TrajectoryPlotter 

class MyGUI_Application():
    '''
    This is the Main application of the GUI
    '''
    def __init__(self) -> None:
        '''Initialize'''
        self.Mainwindow_setup()
        self.Hedge_start()
        self.Initiate_plot_objects()
        self.Interface_widgets()
        self.Show_window()
    
    def Mainwindow_setup(self):
        ''' GUI Mainwindow setup '''
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.MyGUI =  GUI.Ui_MainWindow()
        self.MyGUI.setupUi(self.MainWindow)

    def Hedge_start(self):
        ''' Creating MarvelmindHedge thread '''
        self.hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # "/dev/ttyACM0" is serial port address
        self.hedge.daemon = True # kills thread when main program terminates
        self.hedge.start() # start thread
    
    def Initiate_plot_objects(self):
        ''' Initialize the objects for all the plotters in the GUI'''
        self.liveplot = LivePlotter(self.hedge,self.MyGUI)
        self.originplot = OriginPlotter(self.hedge,self.MyGUI)
        self.waypointplot = WaypointPlotter(self.hedge,self.MyGUI)
        self.trajectoryplot = TrajectoryPlotter(self.hedge,self.MyGUI)
    
    def Show_window(self):
        ''' Show GUI window and exit on close'''
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def Interface_widgets(self):
        ''' Interface all the components of GUI'''
        self.live_tab()
        self.set_origin_tab()
        self.waypoint_tab()
        self.trajectory_tab()

    def live_tab(self):
        '''Live Tab Interfaces'''
        self.MyGUI.live_visualization_window.addWidget(self.liveplot)
        self.MyGUI.live_visualization_enable.stateChanged.connect(self.liveplot.toggle_live_visualization)
        self.MyGUI.live_buffersize_comboBox.activated[str].connect(self.liveplot.set_buffersize)
    
    def set_origin_tab(self):
        '''Set Origin Tab Interfaces'''
        self.MyGUI.setorigin_visualization_window.addWidget(self.originplot)
        self.MyGUI.setorigin_visualization_enable.stateChanged.connect(self.originplot.toggle_live_visualization)
        self.MyGUI.setorigin_setorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.set_origin)
        self.MyGUI.setorigin_setorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.reset_origin)
        # self.MyGUI.setorigin_loadorigin_open_button.clicked.connect(lambda check: directory_fetch(self.MyGUI))#open button
        # self.MyGUI.setorigin_saveorigin_save_button.clicked.connect(lambda:save_function(self.MyGUI))#save button

    def waypoint_tab(self):
        '''Waypoint record Tab Interfaces'''
        self.MyGUI.waypoint_visualization_window.addWidget(self.waypointplot)
        self.MyGUI.waypoint_recordstart_button.clicked.connect(self.waypointplot.recordstart)
        self.MyGUI.waypoint_recordstop_button.clicked.connect(self.waypointplot.recordstop)

    def trajectory_tab(self):
        '''Trajectory record Tab '''
        self.MyGUI.trajectory_visualization_window.addWidget(self.trajectoryplot)
        self.MyGUI.trajectory_recordstart_button.clicked.connect(self.trajectoryplot.recordstart)
        self.MyGUI.trajectory_recordstop_button.clicked.connect(self.trajectoryplot.recordstop)
        self.MyGUI.trajectory_recordclear_button.clicked.connect(self.trajectoryplot.clearplot)

    def set_origin(self):
        '''Makes the current coordinates of the Robot as Origin'''
        origin = self.hedge.position()[1:4] # Current x,y,z
        self.originplot.set_origin(origin)
        self.waypointplot.set_origin(origin)
        self.trajectoryplot.set_origin(origin)
    
    def reset_origin(self):
        '''Reset robot origin to world origin (0,0,0)'''
        self.originplot.reset_origin()
        self.waypointplot.reset_origin()
        self.trajectoryplot.reset_origin()

def save_function(MyGUI):
        content = 0.1
        # text box input
        qfd = QtWidgets.QFileDialog()
        # typed = MyGUI.setorigin_saveorigin_filename.text()
        typed = 'my'
        fname, ok2 = QtWidgets.QFileDialog.getSaveFileName(qfd,typed,os.getcwd(),"Text Files (*.txt)")#"All Files (*);;Text Files (*.txt)" "./"
        print(fname,ok2)
        f = open(fname, "w")
        f.writelines(str(content))
        f.close()
        
def directory_fetch(MyGUI):
        #print("key is pressed")
        qfd = QtWidgets.QFileDialog()
        #To open the directory
        fileName1, filetype = QtWidgets.QFileDialog.getOpenFileName(qfd,"Select File",os.getcwd(),"All Files (*);;Text Files (*.txt)") 
        print(fileName1, filetype)
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

if __name__ == "__main__": 
    myGUI_app = MyGUI_Application()