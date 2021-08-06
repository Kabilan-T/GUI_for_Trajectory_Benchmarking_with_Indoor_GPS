#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from matplotlib.backends.qt_compat import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim

class OriginPlotter(FigureCanvas, anim.FuncAnimation):
    '''
    This is the LiveFigure in which the live plot is drawn.
    credits :  https://stackoverflow.com/questions/57891219/how-to-make-a-fast-matplotlib-live-plot-in-a-pyqt5-gui

    '''
    def __init__(self, hedge, MyGUI, Origin) -> None:
        ''' Initialization '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        self.hedge = hedge
        self.MyGUI = MyGUI
        self.Origin = Origin
        # Set buffersize
        self.set_buffersize(500)
        # Store a figure and ax
        self._ax_  = self.figure.subplots()
        self._ax_.set_xlabel("X - axis")
        self._ax_.set_ylabel("Y - axis")
        self._ax_.axis('equal')
        self._ax_.grid()
        # Initial position
        position = self.hedge.position()
        self.x = [float(position[1])] # index of x
        self.y = [float(position[2])] # index of y     
        # Path
        self._line_, = self._ax_.plot(self.x, self.y, linewidth = 1, color = 'black')
        # Position
        self._point_ = self._ax_.scatter(self.x[-1], self.y[-1], marker='X', color = 'red', s= 100)
        # Origin
        self._origin_ = self._ax_.scatter(self.Origin[0], self.Origin[1], marker='P', color = 'green', s= 100)
        # Initialize animation
        self.animation = anim.FuncAnimation(self.figure, self._update_canvas_, 
                                            fargs=(self.x,self.y,), 
                                            interval=20, blit=False)
        self.paused = False
        return
    
    def set_buffersize(self, buffersize):
        '''Function to set buffersize'''
        self.mylen = int(buffersize)

    def _update_canvas_(self, i, x, y) -> None:
        '''Function to update the elements of the canvas plot'''


        position = self.hedge.position()
        current_x = float(position[1]) # index of x
        current_y = float(position[2]) # index of y     

        x.append(round(current_x, 2))       # Add new datapoint
        y.append(round(current_y, 2))     
        x = x[-self.mylen:]                 # Truncate list _x_
        y = y[-self.mylen:]                 # Truncate list _y_
        # update axis
        margin = 2
        self._ax_.set_xlim(min(min(x),self.Origin[0])-margin, max(max(x),self.Origin[0])+margin)
        self._ax_.set_ylim(min(min(y),self.Origin[1])-margin, max(max(y),self.Origin[1])+margin)
        # update path
        self._line_.set_xdata(x)
        self._line_.set_ydata(y)
        # update position
        self._point_.remove()
        self._point_ = self._ax_.scatter(x[-1], y[-1], marker='X', color = 'red', s= 100)
        # update origin
        self._origin_.remove()
        self._origin_ = self._ax_.scatter(self.Origin[0], self.Origin[1], marker='P', color = 'green', s= 100)

        # labels
            # Origin
        x_value = "X : "+str(self.Origin[0])
        y_value = "Y : "+str(self.Origin[1])
        z_value = "Z : "+str(self.Origin[2])
        self.MyGUI.setorigin_origin_coordiantes_x.setText(x_value)
        self.MyGUI.setorigin_origin_coordiantes_y.setText(y_value)
        self.MyGUI.setorigin_origin_coordiantes_z.setText(z_value)
            # Raw
        x_value = "X : "+str(position[1])
        y_value = "Y : "+str(position[2])
        z_value = "Z : "+str(position[3])
        self.MyGUI.setorigin_rawcoordinates_x.setText(x_value)
        self.MyGUI.setorigin_rawcoordinates_y.setText(y_value)
        self.MyGUI.setorigin_rawcoordinates_z.setText(z_value)
            # Transformed
        x_value = "X : "+str(float(position[1])-float(self.Origin[0]))
        y_value = "Y : "+str(float(position[2])-float(self.Origin[1]))
        z_value = "Z : "+str(float(position[3])-float(self.Origin[2]))
        self.MyGUI.setorigin_transformedcoordinates_x.setText(x_value)
        self.MyGUI.setorigin_transformedcoordinates_y.setText(y_value)
        self.MyGUI.setorigin_transformedcoordinates_z.setText(z_value)

        # return updates
        return self._line_,self._point_ ,
    
    def update_origin(self, Origin):
        '''Function to update origin position the plot'''
        self.Origin = Origin

    def toggle_live_visualization(self,state):
        '''Function to pause or resume live visualization'''
        if state == QtCore.Qt.Checked:
            # Checked
            if self.paused:
                # self.animation.resume() # resume animation
                self.animation.event_source.start() # resume animation
                self.paused = not self.paused
        else:
            # Unchecked
            if not self.paused:
                # self.animation.pause() # pause animation
                self.animation.event_source.stop() # pause animation
                self.paused = not self.paused

