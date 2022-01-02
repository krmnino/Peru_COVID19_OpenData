import sys
from math import e, pi, sqrt
import random
import numpy as np
from numpy.core.numeric import Infinity

sys.path.insert(0, '../utilities')

import PlottingUtility as pu

# === Region Colors ===
# 0 : Red
# 1 : Orange
# 2 : Yellow
# 3 : Green 

class Stats:
    def __init__(self, input_vect, region_colors):
        self.data = input_vect
        self.size = len(self.data)
        self.mean = np.average(self.data)

        # Calculate stdev
        acc = 0
        for i in range(0, self.size):
            acc += (self.data[i] - self.mean) ** 2
        acc = acc / self.size
        self.stdev = sqrt(acc)

        self.regions = {
            0 : (-float('inf'), self.mean - (3 * self.stdev)),
            1 : (self.mean - (3 * self.stdev), self.mean - (2 * self.stdev)),
            2 : (self.mean - (2 * self.stdev), self.mean - (self.stdev)),
            3 : (self.mean - (self.stdev), self.mean),
            4 : (self.mean, self.mean + (self.stdev)),
            5 : (self.mean + (self.stdev), self.mean + (2 * self.stdev)),
            6 : (self.mean + (2 * self.stdev), self.mean + (3 * self.stdev)),
            7 : (self.mean + (3 * self.stdev), float('inf')),
        }

        if(len(region_colors) != 8):
            sys.exit('region_colors parameter must be a list of 8 integers')
        self.region_colors = region_colors

    def display_dataset(self):
        for i in range(0, len(self.data)):
            print(i, ':', self.data[i])

    def plot_gauss_bell(self, ofile, title):
        xbell = np.array([])
        xdata = np.array([])
        ybell = np.array([])
        ydata = np.array([])
    
        low_range = self.mean - (self.stdev * 4)
        high_range = self.mean + (self.stdev * 4)
        increments = (high_range - low_range) / 1000
        count = low_range
        while (count < high_range):
            val = (1.0 / (self.stdev * sqrt(2 * pi))) * e ** (-0.5 * ((count - self.mean) / self.stdev) ** 2)
            xbell = np.append(xbell, count)
            ybell = np.append(ybell, val)
            count += increments
        
        max_y_curve = np.max(ybell)

        for i in range(0, len(self.data)):
            xdata = np.append(xdata, self.data[i])
            max_y = (1.0 / (self.stdev * sqrt(2 * pi))) * e ** (-0.5 * ((self.data[i] - self.mean) / self.stdev) ** 2)
            ydata = np.append(ydata, random.uniform(0, max_y))

        xmean = np.array([self.mean, self.mean])
        ymean = np.array([0, max_y_curve])
        xsd1 = np.array([self.mean - (self.stdev * 3), self.mean - (self.stdev * 3)])
        ysd1 = np.array([0, max_y_curve])
        xsd2 = np.array([self.mean - (self.stdev * 2), self.mean - (self.stdev * 2)])
        ysd2 = np.array([0, max_y_curve])
        xsd3 = np.array([self.mean - (self.stdev), self.mean - (self.stdev)])
        ysd3 = np.array([0, max_y_curve])
        xsd4 = np.array([self.mean + (self.stdev), self.mean + (self.stdev)])
        ysd4 = np.array([0, max_y_curve])
        xsd5 = np.array([self.mean + (self.stdev * 2), self.mean + (self.stdev * 2)])
        ysd5 = np.array([0, max_y_curve])
        xsd6 = np.array([self.mean + (self.stdev * 3), self.mean + (self.stdev * 3)])
        ysd6 = np.array([0, max_y_curve])

        n_datasets = 9
        colors_ds = ['#0743E8', '#E80730', '#009E1A', '#000000', '#000000',
                     '#000000', '#000000', '#000000', '#000000', '#000000']
        linestyle_ds = ['-', '', '-', '--', '--', '--', '--', '--', '--']
        markers_ds = ['', 'o', '', '', '', '', '', '', '']
        title_plot = title
        enable_rolling_avg_ds = [False, False, False, False, False, False, False, False, False]
        x_label = ''
        y_label = ''
        stitle = ''
        out_file = ofile
        ravg_days_ds = [None, None, None, None, None, None, None, None, None]
        ravg_labels_ds = [False, False, False, False, False, False, False, False, False]
        ravg_ydata_ds = [None, None, None, None, None, None, None, None, None]

        self.plot = pu.LayeredScatterPlot(
            n_datasets,
            colors_ds,
            linestyle_ds,
            markers_ds,
            title_plot,
            enable_rolling_avg_ds,
            x_label,
            y_label,
            [xbell, xdata, xmean, xsd1, xsd2, xsd3, xsd4, xsd5, xsd6],
            [ybell, ydata, ymean, ysd1, ysd2, ysd3, ysd4, ysd5, ysd6],
            stitle,
            out_file,
            ravg_days_ds,
            ravg_labels_ds,
            ravg_ydata_ds
        )
        self.plot.export()

    def plot_gauss_bell_datapoint(self, ofile, title, idx):
        xbell = np.array([])
        xdata = np.array([])
        ybell = np.array([])
        ydata = np.array([])
    
        low_range = self.mean - (self.stdev * 4)
        high_range = self.mean + (self.stdev * 4)
        increments = (high_range - low_range) / 1000
        count = low_range
        while (count < high_range):
            val = (1.0 / (self.stdev * sqrt(2 * pi))) * e ** (-0.5 * ((count - self.mean) / self.stdev) ** 2)
            xbell = np.append(xbell, count)
            ybell = np.append(ybell, val)
            count += increments
        
        max_y_curve = np.max(ybell)

        for i in range(0, len(self.data)):
            xdata = np.append(xdata, self.data[i])
            max_y = (1.0 / (self.stdev * sqrt(2 * pi))) * e ** (-0.5 * ((self.data[i] - self.mean) / self.stdev) ** 2)
            ydata = np.append(ydata, random.uniform(0, max_y))

        xmean = np.array([self.mean, self.mean])
        ymean = np.array([0, max_y_curve])
        xsd1 = np.array([self.mean - (self.stdev * 3), self.mean - (self.stdev * 3)])
        ysd1 = np.array([0, max_y_curve])
        xsd2 = np.array([self.mean - (self.stdev * 2), self.mean - (self.stdev * 2)])
        ysd2 = np.array([0, max_y_curve])
        xsd3 = np.array([self.mean - (self.stdev), self.mean - (self.stdev)])
        ysd3 = np.array([0, max_y_curve])
        xsd4 = np.array([self.mean + (self.stdev), self.mean + (self.stdev)])
        ysd4 = np.array([0, max_y_curve])
        xsd5 = np.array([self.mean + (self.stdev * 2), self.mean + (self.stdev * 2)])
        ysd5 = np.array([0, max_y_curve])
        xsd6 = np.array([self.mean + (self.stdev * 3), self.mean + (self.stdev * 3)])
        ysd6 = np.array([0, max_y_curve])

        xdatapoint = np.array([xdata[idx]])
        ydatapoint = np.array([ydata[idx]])

        n_datasets = 10
        colors_ds = ['#0743E8', '#E80730', '#009E1A', '#000000', '#000000',
                     '#000000', '#000000', '#000000', '#000000', '#000000']
        linestyle_ds = ['-', '', '', '-', '--', '--', '--', '--', '--', '--']
        markers_ds = ['', 'o', 'o', '', '', '', '', '', '', '']
        enable_rolling_avg_ds = [False, False, False, False, False, False, False, False, False, False]
        title = 'Datapoint x:' + str(xdata[idx])
        x_label = ''
        y_label = ''
        stitle = ''
        out_file = ofile
        ravg_days_ds = [None, None, None, None, None, None, None, None, None, None]
        ravg_labels_ds = [False, False, False, False, False, False, False, False, False, False]
        ravg_ydata_ds = [None, None, None, None, None, None, None, None, None, None]

        self.plot = pu.LayeredScatterPlot(
            n_datasets,
            colors_ds,
            linestyle_ds,
            markers_ds,
            title,
            enable_rolling_avg_ds,
            x_label,
            y_label,
            [xbell, xdata, xdatapoint, xmean, xsd1, xsd2, xsd3, xsd4, xsd5, xsd6],
            [ybell, ydata, ydatapoint, ymean, ysd1, ysd2, ysd3, ysd4, ysd5, ysd6],
            stitle,
            out_file,
            ravg_days_ds,
            ravg_labels_ds,
            ravg_ydata_ds
        )
        self.plot.export()

    def get_indicator(self, idx):
        if(idx < 0 or idx >= len(self.data)):
            sys.exit('idx cannot be < 0 or >= len(self.data) ->', str(len(self.data)))
        datapoint = self.data[idx]
        color_val = 0
        for i in range(0, len(self.regions)):
            if(datapoint >= self.regions[i][0] and datapoint < self.regions[i][1]):
                color_val = self.region_colors[i]
                break
        indicator = 0
        # return red circle
        if(color_val == 0):
            indicator = u'\U0001F534'
        # return orange circle
        elif(color_val == 1):
            indicator = u'\U0001F7E0'
        # return yellow circle
        elif(color_val == 2):
            indicator = u'\U0001F7E1'
        # return green circle
        elif(color_val == 3):
            indicator = u'\U0001F7E2'
        return indicator