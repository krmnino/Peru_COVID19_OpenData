import sys
from math import e, pi, sqrt
import random
import numpy as np
from numpy.lib.shape_base import tile

sys.path.insert(0, '../utilities')

import PlottingUtility as pu

class Stats:
    def __init__(self, input_vect):
        self.data = input_vect
        self.size = len(self.data)
        self.mean = np.average(self.data)

        # Calculate stdev
        acc = 0
        for i in range(0, self.size):
            acc += (self.data[i] - self.mean) ** 2
        acc = acc / self.size
        self.stdev = sqrt(acc)

    def display_dataset(self):
        for i in range(0, len(self.data)):
            print(i, ':', self.data[i])

    def plot_gauss_bell(self, ofile):
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
        colors_ds = ['b', 'r', 'k', 'k', 'k', 'k', 'k', 'k', 'k']
        linestyle_ds = ['-', '', '-', '--', '--', '--', '--', '--', '--']
        markers_ds = ['', 'o', '', '', '', '', '', '', '']
        title = 'Stats Analysis Gaussian Bell'
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
            title,
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

    def plot_gauss_bell_datapoint(self, ofile, idx):
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
        colors_ds = ['b', 'r', 'g', 'k', 'k', 'k', 'k', 'k', 'k', 'k']
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


data = np.array([])
for i in range(0, 100):
    data = np.append(data, random.uniform(-100.0, 50.0))
tmp = Stats(data)
tmp.display_dataset()
tmp.plot_gauss_bell('test1.png')
tmp.plot_gauss_bell_datapoint('test2.png', 99)
