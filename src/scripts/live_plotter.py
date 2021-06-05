#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib as mpl
import matplotlib.figure as mpl_fig
import matplotlib.animation as anim
import numpy as np

class LiveFigure(FigureCanvas, anim.FuncAnimation):
    '''
    This is the LiveFigure in which the live plot is drawn.
    credits :  https://stackoverflow.com/questions/57891219/how-to-make-a-fast-matplotlib-live-plot-in-a-pyqt5-gui

    '''
    def __init__(self, x_range:List, y_range:List, func, interval:int) -> None:
        '''
        :param x_len:       The nr of data points shown in one plot.
        :param y_range:     Range on y-axis.
        :param interval:    Get a new datapoint every .. milliseconds.

        '''
        FigureCanvas.__init__(self, mpl_fig.Figure())
        # Range settings
        self._x_range_ = x_range
        self._y_range_ = y_range

        # Store two lists _x_ and _y_
        self.mylen = 200
        x = [0] * self.mylen
        y = [0] * self.mylen

        # Store a figure and ax
        self._ax_  = self.figure.subplots()
        self._ax_.set_xlabel("X - axis")
        self._ax_.set_ylabel("Y - axis")
        self._ax_.axis('equal')
        self._ax_.set_xlim(xmin=self._x_range_[0], xmax=self._x_range_[1])
        self._ax_.set_ylim(ymin=self._y_range_[0], ymax=self._y_range_[1])
        self._line_, = self._ax_.plot(x, y, linewidth = 2, color = 'black')

        # Call superclass constructors
        anim.FuncAnimation.__init__(self, self.figure, self._update_canvas_, fargs=(x,y,func,), interval=interval, blit=True)
        return
    
    def _update_canvas_(self, i,x, y,next_point_func) -> None:
        '''
        This function gets called regularly by the timer.

        '''
        current_x, current_y = next_point_func()
        x.append(round(current_x, 2))       # Add new datapoint
        y.append(round(current_y, 2))       
        x = x[-self.mylen:]                 # Truncate list _x_
        y = y[-self.mylen:]                 # Truncate list _y_
        self._line_.set_xdata(x)
        self._line_.set_ydata(y)
        return self._line_,