#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

from matplotlib import animation
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
        self.MyGUI.setorigin_saveorigin_save_button.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.save_origin)
        self.MyGUI.setorigin_loadorigin_open_button.button(QtWidgets.QDialogButtonBox.Open).clicked.connect(self.load_origin)
        self.MyGUI.setorigin_loadorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.apply_origin)
        self.MyGUI.setorigin_loadorigin_dialogbuttons.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.reset_origin)
        
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

    def set_origin(self, origin = []):
        '''Makes the current or given coordinates as Origin'''
        if not origin:
            origin = self.hedge.position()[1:4] # Current x,y,z
        self.originplot.set_origin(origin)
        self.waypointplot.set_origin(origin)
        self.trajectoryplot.set_origin(origin)
    
    def reset_origin(self):
        '''Reset robot origin to world origin (0,0,0)'''
        self.originplot.reset_origin()
        self.waypointplot.reset_origin()
        self.trajectoryplot.reset_origin()
    
    def save_origin(self):
        '''Save origin to a file'''
        filename = self.get_SavefileName("Save Origin","Origin Files (*.origin)")
        filename = filename+'.origin'
        file = open(filename, 'w+')
        [file.write(str(coordinate)+' ') for coordinate in self.originplot.Origin]
        file.close()
    
    def load_origin(self):
        '''Load origin from a existing file'''
        filename = self.get_OpenfileName("Load Origin","Origin Files (*.origin)")
        file = open(filename, "r")
        self.originplot.loaded_origin = [float(coordinate) for row in file for coordinate in row.split()]
        self.originplot.new_origin_loaded = True
        file.close()
    
    def apply_origin(self):
        '''Apply the loaded origin to all the plots'''
        if self.originplot.new_origin_loaded:
            self.set_origin(self.originplot.loaded_origin)
            self.originplot.new_origin_loaded = False
    
    def get_OpenfileName(self,dialog,filter):
        '''Opens a dialog box to get a file name'''
        self.pause_animations()
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(None, dialog, '',filter)
        self.resume_animations()
        return filename
    
    def get_SavefileName(self,dialog,filter):
        '''Opens a dialog box to get a save file name'''
        self.pause_animations()
        filename,_ = QtWidgets.QFileDialog.getSaveFileName(None, dialog, '',filter)
        self.resume_animations()
        return filename
    
    def pause_animations(self):
        '''This pause all the animation in the GUI'''
        self.liveplot.animation.event_source.stop()
        self.originplot.animation.event_source.stop()
        self.waypointplot.animation.event_source.stop()
        self.trajectoryplot.animation.event_source.stop()
    
    def resume_animations(self):
        '''This resumes all the animation in the GUI'''
        self.liveplot.animation.event_source.start()
        self.originplot.animation.event_source.start()
        self.waypointplot.animation.event_source.start()
        self.trajectoryplot.animation.event_source.start()


if __name__ == "__main__": 
    myGUI_app = MyGUI_Application()