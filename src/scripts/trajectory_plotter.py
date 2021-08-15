#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import *
import csv
from datetime import datetime
from matplotlib.backends.qt_compat import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim

class TrajectoryPlotter(FigureCanvas, anim.FuncAnimation):
    '''
    This is the TrajectorPlotter in which the trajectory recording plot is drawn.
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
        self.plot_x = list()
        self.plot_y = list()
        # Path
        self._line_, = self._ax_.plot(self.x, self.y, linewidth = 2, color = 'black')
        # Position
        self._robot_ = self._ax_.scatter(self.x[-1], self.y[-1], marker='X', color = 'red', s= 100)
        # Origin
        self._origin_ = self._ax_.scatter(0, 0, marker='P', color = 'blue', s= 100)
        # Annotate
        self._robottxt_ = self._ax_.annotate('Robot', (self.x[-1], self.y[-1]))
        self._origintxt_ = self._ax_.annotate('Origin', (0, 0), ha='right')
        

        # Initialize animation
        self.animation = anim.FuncAnimation(self.figure, self._update_canvas_, 
                                            fargs=(self.x,self.y,self.z,), 
                                            interval=20, blit=False)
        # Variables
        self.recording = False
        self.startplotted = False
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
            # write data into file
            data = [position[-1], current_x, current_y, current_z ]
            self.writer.writerow(data)
            
            # update record path
            self.plot_x.append(x[-1])
            self.plot_y.append(y[-1])
            # update path
            self._line_.set_xdata(self.plot_x)
            self._line_.set_ydata(self.plot_y)
            if not self.startplotted :
                # start Position
                self._start_ = self._ax_.scatter(self.plot_x[0], self.plot_y[0], marker='o', color = 'red', s= 100)
                self._starttxt_ = self._ax_.annotate('Start', (self.plot_x[0], self.plot_y[0]), ha='left')
                self.startplotted = True

        '''labels'''
        # Recorded Coordinates
        self.MyGUI.trajectory_timestamp.setText("Time : "+str(position[-1]))
        self.MyGUI.trajectory_coordiantes_x.setText("X : "+str(current_x))
        self.MyGUI.trajectory_coordiantes_y.setText("Y : "+str(current_y))
        self.MyGUI.trajectory_coordiantes_z.setText("Z : "+str(current_z))

    def recordstart(self):
        '''Function to initiate recording'''
        if not self.recording:
            self.clearplot()
            filename = self.get_filename()
            date = datetime.now().strftime("_%Y_%m_%d-%H:%M:%S")
            self.output_file = open(filename+date+'.csv', "w+")
            self.writer = csv.writer(self.output_file)
            header = ['TimeStamp', 'X-value', 'Y-value', 'Z-value']
            self.writer.writerow(header)
            self.animation.event_source.start() # resume animation
            self.recording = True

    def recordstop(self):
        '''Function to Terminate the recording'''
        if self.recording:
            self.output_file.close()
            self.animation.event_source.stop() # pause animation
            self.recording = False
            self.startplotted = False

    def clearplot(self):
        '''Funtion to clear the plot'''
        if not self.recording:
            self.plot_x.clear()
            self.plot_y.clear()
            try:
                self._line_.remove()
                self._start_.remove()
                self._starttxt_.remove()
            except: pass
            self._line_, = self._ax_.plot(self.Origin[0], self.Origin[1], linewidth = 2, color = 'black')
            self.animation.event_source.start() # resume animation

    def set_origin(self, Origin):
        '''Function to set origin position'''
        self.Origin = Origin
    
    def reset_origin(self):
        '''Function to reset the origin position'''
        self.Origin = [.0, .0, .0]
    
    def get_filename(self):
        '''Function to get Filename prefix'''
        path = os.path.join(os.getcwd(),'Trajectory')
        if not os.path.exists(path):
            os.makedirs(path)
        # Robot and Run name selection
        robot_name = str(self.MyGUI.trajectory_robot_comboBox.currentText())
        run_name = str(self.MyGUI.trajectory_run_comboBox.currentText())
        filename = robot_name+'_'+run_name+'_'
        return os.path.join(path, filename)