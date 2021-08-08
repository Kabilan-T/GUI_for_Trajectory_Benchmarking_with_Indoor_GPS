#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from matplotlib.backends.qt_compat import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim

class LivePlotter(FigureCanvas, anim.FuncAnimation):
    '''
    This is the LiveFigure in which the live plot is drawn.
    credits :  https://stackoverflow.com/questions/57891219/how-to-make-a-fast-matplotlib-live-plot-in-a-pyqt5-gui
    '''
    def __init__(self, hedge, MyGUI) -> None:
        ''' Initialization '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        self.hedge = hedge
        self.MyGUI = MyGUI
        # Set buffersize
        self.set_buffersize(20)

        # Plot setup
        self._ax_  = self.figure.subplots()
        self._ax_.set_xlabel("X - axis")
        self._ax_.set_ylabel("Y - axis")
        self._ax_.axis('equal')
        self._ax_.grid()

        '''Plot elements'''
        # Initial position
        position = self.hedge.position()
        self.x = [float(position[1])] # index of x
        self.y = [float(position[2])] # index of y     
        # Path
        self._line_, = self._ax_.plot(self.x, self.y, linewidth = 2, color = 'black')
        # Position
        self._robot_ = self._ax_.scatter(self.x[-1], self.y[-1], marker='X', color = 'red', s= 100)
        # Annotate
        self._robottxt_ = self._ax_.annotate('Robot', (self.x[-1], self.y[-1]))

        # Initialize animation
        self.animation = anim.FuncAnimation(self.figure, self._update_canvas_, 
                                            fargs=(self.x,self.y,), 
                                            interval=20, blit=False)
        # Variables
        self.paused = False
        return
    
    def _update_canvas_(self, i, x, y) -> None:
        '''Function to update the elements of the canvas plot'''
        # New data point
        position = self.hedge.position()
        current_x = float(position[1]) # index of x
        current_y = float(position[2]) # index of y
        x.append(round(current_x, 2))       
        y.append(round(current_y, 2))     
        x = x[-self.mylen:]                 # Truncate list _x_
        y = y[-self.mylen:]                 # Truncate list _y_

        '''Plot elements update'''
        # update axis
        margin = 2
        self._ax_.set_xlim(min(x)-margin, max(x)+margin)
        self._ax_.set_ylim(min(y)-margin, max(y)+margin)
        # update path
        self._line_.set_xdata(x)
        self._line_.set_ydata(y)
        # update position
        self._robot_.remove()
        self._robot_ = self._ax_.scatter(x[-1], y[-1], marker='X', color = 'red', s= 100)
        self._robottxt_.remove()
        self._robottxt_ = self._ax_.annotate('Robot', (x[-1], y[-1]))

        '''labels'''
        self.MyGUI.live_hedge_id.setText("Hedge ID : "+str(position[0]))
        self.MyGUI.live_coordiantes_x.setText("X : "+str(position[1]))
        self.MyGUI.live_coordiantes_y.setText("Y : "+str(position[2]))
        self.MyGUI.live_coordiantes_z.setText("Z : "+str(position[3]))
    
    def set_buffersize(self, buffersize):
        '''Function to set buffersize'''
        self.mylen = int(buffersize)

    def toggle_live_visualization(self,state):
        '''Function to pause or resume live visualization'''
        if state == QtCore.Qt.Checked:
            # Checked
            if self.paused:
                self.animation.event_source.start() # resume animation
                self.paused = not self.paused
        else:
            # Unchecked
            if not self.paused:
                self.animation.event_source.stop() # pause animation
                self.paused = not self.paused