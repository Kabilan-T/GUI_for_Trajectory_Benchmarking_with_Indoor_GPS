#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from datetime import datetime
from matplotlib.backends.qt_compat import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim

class RecordPlotter(FigureCanvas, anim.FuncAnimation):
    '''
    This is the LiveFigure in which the live plot is drawn.
    credits :  https://stackoverflow.com/questions/57891219/how-to-make-a-fast-matplotlib-live-plot-in-a-pyqt5-gui

    '''
    def __init__(self, hedge, MyGUI,Origin) -> None:
        ''' Initialization '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        self.hedge = hedge
        self.MyGUI = MyGUI
        self.Origin = Origin
 
        # Store a figure and ax
        self._ax_  = self.figure.subplots()
        self._ax_.set_xlabel("X - axis")
        self._ax_.set_ylabel("Y - axis")
        self._ax_.axis('equal')
        self._ax_.grid()

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
        self._point_ = self._ax_.scatter(self.x[-1], self.y[-1], marker='X', color = 'red', s= 100)
        # Origin
        self._origin_ = self._ax_.scatter(self.Origin[0], self.Origin[1], marker='P', color = 'blue', s= 100)
        # start Position
        self._start_ = self._ax_.scatter(self.Origin[0], self.Origin[1], marker='P', color = 'blue', s= 100)
        # Initialize animation
        self.animation = anim.FuncAnimation(self.figure, self._update_canvas_, 
                                            fargs=(self.x,self.y,self.z,), 
                                            interval=20, blit=False)
        self.recording = False
        return

    def _update_canvas_(self, i, x, y, z) -> None:
        '''Function to update the elements of the canvas plot'''

        position = self.hedge.position()
        current_x = float(position[1])-float(self.Origin[0]) # index of x
        current_y = float(position[2])-float(self.Origin[1]) # index of y     
        current_z = float(position[3])-float(self.Origin[2]) # index of z    
        
        # update position
        self._point_.remove()
        self._point_ = self._ax_.scatter(current_x, current_y, marker='X', color = 'red', s= 100)
        # update origin
        self._origin_.remove()
        self._origin_ = self._ax_.scatter(self.Origin[0], self.Origin[1], marker='P', color = 'blue', s= 100)

        x.append(round(current_x, 2))       # Add new datapoint
        y.append(round(current_y, 2))
        z.append(round(current_z, 2)) 

        # update axis
        margin = 2
        self._ax_.set_xlim(min(min(x),self.Origin[0])-margin, max(max(x),self.Origin[0])+margin)
        self._ax_.set_ylim(min(min(y),self.Origin[1])-margin, max(max(y),self.Origin[1])+margin)

        if self.recording:
            self.output_file.write(str(position[-1])+'\t'+
                                   str(current_x)+'\t'+
                                   str(current_y)+'\t'+
                                   str(current_z)+'\n')
            self.plot_x.append(x[-1])
            self.plot_y.append(y[-1])
            # update path
            self._line_.set_xdata(self.plot_x)
            self._line_.set_ydata(self.plot_y)
            # start Position
            self._start_.remove()
            self._start_ = self._ax_.scatter(self.plot_x[0], self.plot_y[0], marker='o', color = 'red', s= 100)

        # labels
            # Recorded Coordinates
        timestamp = "Time : "+str(position[-1])
        x_value = "X : "+str(current_x)
        y_value = "Y : "+str(current_y)
        z_value = "Z : "+str(current_z)
        self.MyGUI.record_timestamp.setText(timestamp)
        self.MyGUI.record_coordiantes_x.setText(x_value)
        self.MyGUI.record_coordiantes_y.setText(y_value)
        self.MyGUI.record_coordiantes_z.setText(z_value)

        # return updates
        return self._line_,self._point_,self._origin_
    
    def update_origin(self, Origin):
        '''Function to update origin position the plot'''
        self.Origin = Origin

    def recordstart(self,filename):
        if not self.recording:
            self.clearplot()
            date = datetime.now().strftime("_%Y_%m_%d-%H:%M:%S")
            self.output_file = open(filename+date+'.txt', "w+")
            self.output_file.write('TimeStamp \t X-Value \t Y-Value \t Z-Value \n')
            print('starting to record')
            self.animation.resume()
            self.recording = True

    def recordstop(self):
        if self.recording:
            self.output_file.close()
            self.animation.pause() # pause animation
            print('stop record')
            self.recording = False

    def clearplot(self):
        if not self.recording:
            self.plot_x = []
            self.plot_y = []
            self._line_.remove()
            self._start_.remove()
            self._start_ = self._ax_.scatter(self.Origin[0], self.Origin[1], marker='P', color = 'blue', s= 100)
            self._line_, = self._ax_.plot(self.Origin[0], self.Origin[1], linewidth = 2, color = 'black')
            self.animation.resume()