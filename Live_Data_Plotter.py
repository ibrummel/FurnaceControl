from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import QObject, QSize
from copy import copy
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from numpy import ndarray
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavToolBar

class FurnacePlotWidget(QFrame):
    def __init__(self, lines_info: dict, parent=None, nrows=1, ncols=1, line_width=2,):
        super().__init__(parent)

        # Create child widgets
        self.canvas = FurnacePlotCanvas(lines_info, nrows=1, ncols=1, line_width=2,)
        self.toolbar = NavToolBar(self.canvas, self, coordinates=True)

        self.init_connections()
        self.init_control_setup()
        self.init_layout()

    def init_connections(self):
        pass

    def init_control_setup(self):
        pass

    def init_layout(self):
        # Create a layout to hold the plot and toolbar
        vbox = QVBoxLayout()
        vbox.addWidget(self.toolbar)
        vbox.addWidget(self.canvas)

        # Set layout to be the vbox
        self.setLayout(vbox)

    def update_plot_labels(self, subplot_idx, ax_labels: list):
        self.canvas.change_axes_labels(subplot_idx, ax_labels)

    def add_data(self, line_key: str, point: list, draw_frame=True):
        self.canvas.add_data(line_key, point, draw_frame)

    def remove_line(self, line_key: str, draw_frame=False):
        self.canvas.clear_data(line_key, draw_frame)


class FurnacePlotCanvas(FigCanvas):
    def __init__(self, lines_info: dict, nrows=1, ncols=1, line_width=2,):

        # Save init values to class variables
        self.lines_info = lines_info
        self.line_width = line_width

        # Create figure and first set of axes
        self.figure, self.axes = plt.subplots(nrows=nrows, ncols=ncols, squeeze=False)
        self._check_axes_assignment()
        self._check_init_data()

        self.init_axes()
        FigCanvas.__init__(self, self.figure)
        self.draw()

    def init_axes(self):
        for i, subplot_row in enumerate(self.axes):
            for j, subplot in enumerate(subplot_row):
                # FIXME: Currently does not account for setting axes labels based on data
                self.change_axes_labels([i, j] ['Time', 'Process Value'])

    def _check_axes_assignment(self, check_key=None):
        for key in self.lines_info:
            if check_key is not None and key != check_key:
                continue
            else:
                # If there is a non numerical value or no value stored for the subplot index, move the
                # checked line to the root subplot at [0, 0] and print a message informing the user.
                try:
                    self.lines_info[key]['subplot_row'] = int(self.lines_info[key]['subplot_row'])
                    if self.lines_info[key]['subplot_row'] > self.axes.shape[0] - 1:
                        print("The line labeled {} had subplot row index outside the current number of subplot rows. "
                              "This line has been moved to the plot at [0,0]".format(key))
                        self.lines_info[key]['subplot_row'] = 0
                        self.lines_info[key]['subplot_col'] = 0
                except ValueError as err:
                    print(err, "The line labeled {} had a non-numerical value for subplot row index. "
                          "This line has been moved to the plot at [0,0]".format(key))
                    self.lines_info[key]['subplot_row'] = 0
                    self.lines_info[key]['subplot_col'] = 0
                except KeyError as err:
                    print(err, "The line labeled {} had no subplot row index. "
                          "This line has been moved to the plot at [0,0]".format(key))
                    self.lines_info[key]['subplot_row'] = 0
                    self.lines_info[key]['subplot_col'] = 0

                try:
                    self.lines_info[key]['subplot_col'] = int(self.lines_info[key]['subplot_col'])
                    if self.lines_info[key]['subplot_col'] > self.axes.shape[1] - 1:
                        print("The line labeled {} had subplot column index outside the current number of subplot "
                              "columns. This line has been moved to the plot at [0,0]".format(key))
                        self.lines_info[key]['subplot_row'] = 0
                        self.lines_info[key]['subplot_col'] = 0
                except ValueError as err:
                    print(err, "The line labeled {} had a non-numerical value for subplot column index. "
                          "This line has been moved to the plot at [0,0]".format(key))
                    self.lines_info[key]['subplot_row'] = 0
                    self.lines_info[key]['subplot_col'] = 0
                except KeyError as err:
                    print(err, "The line labeled {} had no subplot column index. "
                          "This line has been moved to the plot at [0,0]".format(key))
                    self.lines_info[key]['subplot_row'] = 0
                    self.lines_info[key]['subplot_col'] = 0

    def _check_init_data(self, check_key=None):
        # for key in self.lines_info:
        #     if check_key is not None and key != check_key:
        #         continue
        #     else:
        #         try:
        #
        pass

    def add_data(self, line_key: str, point: list, draw_frame=False):
        try:
            self.lines_info[line_key]['x'] = point[0]
            self.lines_info[line_key]['y'] = point[1]
        except KeyError as err:
            print(err, 'Attempted to add data to a non-existant line: {}'.format(line_key))

        if draw_frame:
            self._draw_frame()

    def change_line_color(self, line_key: str, color: str):
        try:
            self.lines_info[line_key]['color'] = color
        except KeyError as err:
            print(err, 'Tried to set the color for a non-existant or non-plotted line: {}'.format(line_key))

    def add_line(self, line_key: str, line_info: dict, draw_frame=False):
        self.lines_info[line_key] = line_info

        if draw_frame:
            self._draw_frame()

    def remove_line(self, line_key: str, draw_frame=False):
        try:
            self.lines_info.pop(line_key)
        except KeyError as err:
            print(err, 'KeyError on trying to remove a plotted line: {}'.format(line_key))

        if draw_frame:
            self._draw_frame()

    def change_axes_labels(self, subplot_idx, ax_labels: list, draw_frame=False):
        try:
            ax = self.axes[subplot_idx[0], subplot_idx[1]]
            ax.set_xlabel(ax_labels[0], fontsize=14, weight='bold')
            ax.set_ylabel(ax_labels[1], fontsize=14, weight='bold')
        except IndexError as err:
            print(err, "Attempting to set axes labels on a nonexistant subplot at {}".format(subplot_idx))

        if draw_frame:
            self._draw_frame()

    def _draw_frame(self):
        # Clear all data
        for subplot_row in self.axes:
            for subplot in subplot_row:
                subplot.clear()
        
        try:
            for line_key, line_info in self.lines_info.items():
                ax = self.axes[line_info['subplot_row'], line_info['subplot_col']]
                ax.plot(line_info['x'], line_info['y'], color=line_info['color'], label=line_key)
                ax.legend()
                # Relimit the plot to keep data in view
                self.axes.relim()
                self.axes.autoscale_view(True, True, True)
                # Maybe do this depending on how many things you will have/want to plot
                # self.change_axes_labels([line_info['subplot_row'], line_info['subplot_col']], line_info[''])
        except IndexError as err:
            print(err, 'Likely a result of attempting to replot too quickly after clearing the old data')
        except KeyError as err:
            print(err, "Key error on drawing new frame")

        # Draw the plot with new stuff
        self.draw()
