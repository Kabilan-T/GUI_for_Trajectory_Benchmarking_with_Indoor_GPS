#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import *
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim

class ComparisonPlotter(FigureCanvas, anim.FuncAnimation):
    '''
    This is the ComparisonPlotter in which the comparison between two path are plotted.
    '''
    def __init__(self, MyGUI) -> None:
        ''' Initialization '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        self.MyGUI = MyGUI
 
        # Plot setup
        self._ax_  = self.figure.subplots()
        self._ax_.set_xlabel("X - axis")
        self._ax_.set_ylabel("Y - axis")
        self._ax_.axis('equal')
        self._ax_.grid()

        '''Plot elements'''
        # Origin
        self._origin_ = self._ax_.scatter(0, 0, marker='P', color = 'blue', s= 100)
        self._origintxt_ = self._ax_.annotate('Origin', (0, 0), ha='center')
        # Waypoints
        self._waypoints1_  = list()
        self._waypoints1txt_ = list()
        self._waypoints2_  = list()
        self._waypoints2txt_ = list()
        self._boundary1_ = list()
        self._boundary2_ = list()

        # Initialize animation
        self.animation = anim.FuncAnimation(self.figure, self._update_canvas_, 
                                            fargs=(), 
                                            interval=20, blit=False)
        # Variables
        self.waypointfile1 = ''
        self.waypointfile2 = ''
        self.waypoints1 = dict()
        self.waypoints2 = dict()
        self.wapoints1_loaded = False
        self.wapoints2_loaded = False
        self.measurement_precision = 2e-2
        return

    def _update_canvas_(self,i) -> None:
        '''Function to update the elements of the canvas plot'''
        if self.wapoints1_loaded:
            x1,y1 = list(),list()
            for no in self.waypoints1:
                x = self.waypoints1[no]['Mean'][0]
                y = self.waypoints1[no]['Mean'][1]
                x1.append(x)
                y1.append(y)
                self._waypoints1_.append(self._ax_.scatter(x, y, marker='v', color = 'red', s= 70))
                self._waypoints1txt_.append(self._ax_.annotate(str(int(no)),(x, y),color='red', ha='right'))
                t = np.linspace(0, 2*np.pi, 100)
                a=self.waypoints1[no]['Std'][0]
                b=self.waypoints1[no]['Std'][1]
                self._boundary1_.append(self._ax_.plot( x+a*np.cos(t) , y+b*np.sin(t), color = 'black', lw =0.5 ))

            # self._path1_ = self._ax_.plot(x1, y1, linewidth = 2, color = 'red')
            self.wapoints1_loaded = False
                                             
        if self.wapoints2_loaded:  
            x2,y2 = list(),list()  
            for no in self.waypoints2:
                x = self.waypoints2[no]['Mean'][0]
                y = self.waypoints2[no]['Mean'][1]
                x2.append(x)
                y2.append(y)
                self._waypoints2_.append(self._ax_.scatter(x, y, marker='v', color = 'orange', s= 40))
                self._waypoints2txt_.append(self._ax_.annotate(str(int(no)),(x, y),color='orange', ha='left'))
                t = np.linspace(0, 2*np.pi, 100)
                a=self.waypoints2[no]['Std'][0]
                b=self.waypoints2[no]['Std'][1]
                self._boundary2_.append(self._ax_.plot( x+a*np.cos(t) , y+b*np.sin(t), color = 'black', lw =0.5 ))

            # self._path2_ = self._ax_.plot(x2, y2, linewidth = 1, color = 'blue')
            self.wapoints1_loaded = False

    def update_plot(self):
        '''updates the plot when new waypoint file is opened'''
        self.clear_plot()
        if self.waypointfile1:
            self.waypoints1 = self.load_waypoints(self.waypointfile1)
            self.waypoints1 = self.induce_measurement_uncertainity(self.waypoints1)
            self.wapoints1_loaded = True
        if self.waypointfile2:
            self.waypoints2 = self.load_waypoints(self.waypointfile2)
            self.waypoints2 = self.induce_measurement_uncertainity(self.waypoints2)
            self.wapoints2_loaded = True

    def clear_plot(self):
        '''Function to clear the plot'''
        self._ax_.clear()
        # Plot re-setup
        self._ax_.grid()
        self._origin_ = self._ax_.scatter(0, 0, marker='P', color = 'blue', s= 100)
        self._origintxt_ = self._ax_.annotate('Origin', (0, 0), ha='center')
        self._waypoints1_ = []
        self._waypoints1txt_ = []
        self._waypoints2_ = []
        self._waypoints2txt_ = []
        self._boundary1_ = []
        self._boundary2_ = []
        self.waypoints1.clear()
        self.waypoints2.clear()
        
    def load_waypoints(self,filepath):
        '''Function to read and return waypoints fron the csv file'''
        waypoints = dict()
        datapoints = np.loadtxt(open(filepath,"rb"), delimiter=",", skiprows=1)
        for data in datapoints:
            waypoints[data[0]] = {'Mean':np.array([data[1],data[3],data[5]]),
                                  'Std':np.array([data[2],data[4],data[6]])}
        return waypoints

    def induce_measurement_uncertainity(self,waypoints):
        '''Function to induce measurement uncertainity into comparision'''
        for no in waypoints:
            waypoints[no]['Std'] =  waypoints[no]['Std'] + self.measurement_precision
        return waypoints

    def compare_wapoints(self):
        '''Function to compare two recorded waypoints'''
        if len(self.waypoints1) == len(self.waypoints2):
            self.result = dict()
            for no in self.waypoints1:
                self.result[no] = self.subtract_uncertainities(self.waypoints1[no],
                                                          self.waypoints2[no])
            print(self.result)
    
    def subtract_uncertainities(self,point1,point2):
        '''Function to subtract two uncertainity coordinates [x,y,z]'''
        Mean = point1['Mean']-point2['Mean']
        Std = point1['Std']+point2['Std']
        return {'Mean': Mean,'Std': Std}

        