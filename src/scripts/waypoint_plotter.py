#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import *
import csv
from datetime import datetime
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim

class WaypointPlotter(FigureCanvas, anim.FuncAnimation):
    '''
    This is the WaypointPlotter in which the waypoint recording is drawn.
    '''
    def __init__(self, hedge, MyGUI) -> None:
        ''' Initialization '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        self.hedge = hedge
        self.MyGUI = MyGUI
        # Reset Origin
        self.reset_origin()
 
        # Plot setup
        self._ax_  = self.figure.subplots()
        self._ax_.set_xlabel("X - axis")
        self._ax_.set_ylabel("Y - axis")
        self._ax_.axis('equal')
        self._ax_.grid()

        '''Plot elements'''
        # Initial position
        position = self.hedge.position()
        self.x = [float(position[1])-float(self.Origin[0])] # index of x
        self.y = [float(position[2])-float(self.Origin[1])] # index of y     
        self.z = [float(position[3])-float(self.Origin[2])] # index of z
        # Position
        self._robot_ = self._ax_.scatter(self.x[-1], self.y[-1], marker='X', color = 'red', s= 100)
        # Origin
        self._origin_ = self._ax_.scatter(0, 0, marker='P', color = 'blue', s= 100)
        # Annotate
        self._robottxt_ = self._ax_.annotate('Robot', (self.x[-1], self.y[-1]))
        self._origintxt_ = self._ax_.annotate('Origin', (0, 0), ha='right')
        # Waypoints
        self._waypoints_  = list()
        self._waypointstxt_ = list()

        # Initialize animation
        self.animation = anim.FuncAnimation(self.figure, self._update_canvas_, 
                                            fargs=(self.x,self.y,self.z,), 
                                            interval=20, blit=False)
        # Variables
        self.waypoint = list()
        self.datapoints = list()
        self.waypointFileCreated = False
        self.quantile = 0.95
        self.sample_size = 100
        self.recording = False 
        return

    def _update_canvas_(self, i, x, y, z) -> None:
        '''Function to update the elements of the canvas plot'''
        # New data point
        position = self.hedge.position()
        current_x = float(position[1])-float(self.Origin[0]) # index of x
        current_y = float(position[2])-float(self.Origin[1]) # index of y     
        current_z = float(position[3])-float(self.Origin[2]) # index of z    
        x.append(round(current_x, 2))     
        y.append(round(current_y, 2))
        z.append(round(current_z, 2)) 

        '''Plot elements update'''
        # update position
        self._robot_.remove()
        self._robot_ = self._ax_.scatter(current_x, current_y, marker='X', color = 'red', s= 100)
        # update axis
        margin = 2
        self._ax_.set_xlim(min(min(x),self.Origin[0])-margin, max(max(x),self.Origin[0])+margin)
        self._ax_.set_ylim(min(min(y),self.Origin[1])-margin, max(max(y),self.Origin[1])+margin)
        # update annotation
        self._robottxt_.remove()
        self._robottxt_ = self._ax_.annotate('Robot', (current_x, current_y))
        
        if self.recording:
            '''Recording'''
            self.datapoints.append([current_x, current_y, current_z])
            if len(self.datapoints) >= self.sample_size :
                # compute waypoint
                Mean, Std = self.compute_waypoint(self.datapoints)
                self.waypoint.append([Mean, Std])
                
                # plot waypoint Position
                self._waypoints_.append(self._ax_.scatter(Mean[0], Mean[1], marker='v', color = 'green', s= 50))
                self._waypointstxt_.append(self._ax_.annotate(str(len(self.waypoint)), (Mean[0], Mean[1]), ha='right'))

                # write data into file
                data = [len(self.waypoint), Mean[0], Std[0], Mean[1], Std[1], Mean[2], Std[2]]
                self.writer.writerow(data)
                self.datapoints.clear()
                self.recording = False

        '''labels'''
        # Recorded Coordinates
        self.MyGUI.waypoint_timestamp.setText("Time : "+str(position[-1]))
        self.MyGUI.waypoint_coordiantes_x.setText("X : "+str(current_x))
        self.MyGUI.waypoint_coordiantes_y.setText("Y : "+str(current_y))
        self.MyGUI.waypoint_coordiantes_z.setText("Z : "+str(current_z))

    def compute_waypoint(self,datapoints): 
        '''Function to compute a waypoint from a set of recorded datapoints'''
        df = pd.DataFrame(datapoints, columns=['x', 'y', 'z'])
        # Remove datapoints outside 95% quantile (outliers)
        ouliers_idx = set()
        for data in [df['x'],df['y'],df['z']]:
            for i , value in enumerate(data):  
                if (value > data.quantile(1-self.quantile) and value < data.quantile(self.quantile)) : continue
                else : ouliers_idx.add(i)
        df = df.drop(list(ouliers_idx)) #drop outliers
        # Mean and Standard Deviation 
        Mean,Std = list(),list()
        for data in [df['x'],df['y'],df['z']]:
            Mean.append(np.mean(data))
            Std.append(np.std(data))
        return Mean,Std

    def recordstart(self):
        '''Function to initiate recording of a waypoint'''
        if not self.recording:
            if not self.waypointFileCreated : 
                filename = self.get_filename()
                date = datetime.now().strftime("_%Y_%m_%d-%H:%M:%S")
                self.output_file = open(filename+date+'.csv', "w+")
                self.writer = csv.writer(self.output_file)
                header = ['Waypoint No', 'X-Mean', 'X-Standard Deviation', 'Y-Mean', 
                          'Y-Standard Deviation', 'Z-Mean', 'Z-Standard Deviation']
                self.writer.writerow(header)
                self.waypointFileCreated = True
            self.recording = True

    def recordstop(self):
        '''Function to Terminate the recording and clear the plot'''
        self.output_file.close()
        try:
            for waypoint in self._waypoints_ : waypoint.remove()
            for txt in self._waypointstxt_ : txt.remove()
        except: pass
        self._waypoints_ = []
        self._waypointstxt_ = []
        self.waypoint.clear()
        self.waypointFileCreated = False
        print('stop record')

    def set_origin(self, Origin):
        '''Function to set origin position'''
        self.Origin = Origin
    
    def reset_origin(self):
        '''Function to reset the origin position'''
        self.Origin = [.0, .0, .0]
    
    def get_filename(self):
        '''Function to get Filename prefix'''
        path = os.path.join(os.getcwd(),'Waypoint')
        if not os.path.exists(path):
            os.makedirs(path)
        # Robot and Run name selection
        robot_name = str(self.MyGUI.waypoint_robot_comboBox.currentText())
        run_name = str(self.MyGUI.waypoint_run_comboBox.currentText())
        filename = robot_name+'_'+run_name+'_'
        return os.path.join(path, filename)