from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import warnings
import numpy as np
import sys

from numpy.lib.arraysetops import isin

warnings.filterwarnings('ignore')

class ScatterPlot:
    # x_dataset -> array
    # y_dataset -> array
    # linestyle -> string
    # marker -> string
    # color -> string
    # label -> string
    # linewidth -> string
    # legend -> boolean
    # rolling_avg -> boolean
    # n_rolling_avg -> integer
    # x_axis_label -> string
    # x_axis_labelsize -> integer
    # x_axis_orientation -> integer
    # x_ticks_size -> integer
    # title -> string
    # title_size -> integer
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # digit_font -> string
    # filename -> string
    def __init__(self, x_dataset, y_dataset, linestyle, marker, color, label, linewidth, legend, rolling_avg, n_rolling_avg,
                 rolling_avg_label, x_axis_label, x_axis_labelsize, x_axis_orientation, x_ticks_size, y_axis_label,
                 y_axis_labelsize, title, title_size, super_title, super_title_size, text_font, digit_font, filename):
        self.x_dataset  = x_dataset
        self.y_dataset = y_dataset
        self.linestyle = linestyle
        self.marker = marker
        self.color = color
        self.label = label
        self.linewidth = linewidth
        self.legend = legend
        self.rolling_avg = rolling_avg
        self.n_rolling_avg = n_rolling_avg
        self.rolling_avg_label = rolling_avg_label
        self.x_axis_label = x_axis_label
        self.x_axis_labelsize = x_axis_labelsize
        self.x_axis_orientation = x_axis_orientation
        self.x_ticks_size = x_ticks_size
        self.y_axis_label = y_axis_label
        self.y_axis_labelsize = y_axis_labelsize
        self.title = title
        self.title_size = title_size
        self.super_title = super_title
        self.super_title_size = super_title_size
        self.text_font = {'fontname': text_font}
        self.digit_font = {'fontname': digit_font}
        self.filename = filename
        self.validate()

    def validate(self):
        # Validate len(x_dataset) = len(y_dataset)
        if(len(self.x_dataset) != len(self.y_dataset)):
            sys.exit('Error: x_dataset size does not equal y_dataset size.')

        # Validate if rolling_avg is True and n_rolling_avg is an integer type
        if(self.rolling_avg and (not isinstance(self.n_rolling_avg, int))):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')

        # Validate if rolling_avg is True and 0 <= n_rolling_avg < len(x_dataset) - 1
        if(self.rolling_avg and (self.n_rolling_avg < 0 or self.n_rolling_avg > len(self.x_dataset) - 1)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be greater than 0 and less than', str(len(self.x_dataset) - 1) + '.')
            
        # Validate if color is a string type
        if(not isinstance(self.color, str)):
            sys.exit('Error: color is must be a str type.')

        # Validate first char of color is a pound sign (#)
        if(self.color[0] != '#'):
            sys.exit('Error: color is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that the following 6 chars of color are alphanumeric
        for i in range(1, len(self.color)):
            if(not self.color[i].isalnum()):
                sys.exit('Error: color is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that x_axis_orientation is an integer type
        if(not isinstance(self.x_axis_orientation, int)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')

        # Validate that x_axis_orientation value is either 0, 90, 180, 270, 360
        if(self.x_axis_orientation != 0 and self.x_axis_orientation != 90 and 
           self.x_axis_orientation != 180 and self.x_axis_orientation != 270 and
           self.x_axis_orientation != 360):
            sys.exit('Error: x_axis_orientation must be either 0, 90, 180, 270, 360.')
        
    def __rgb_threshold(self, color, min=0, max=255):
        if (color < min):
            return min
        if (color > max):
            return max
        return color
    
    def __export_generate_rolling_avg(self):
        avgd_data = np.array([])
        for i in range(len(self.y_dataset) - (len(self.x_dataset) + self.n_rolling_avg), len(self.y_dataset)):
            sum_data = 0
            for j in range(i - self.n_rolling_avg, i):
                sum_data += self.y_dataset[j]
            sum_data /= self.n_rolling_avg
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.color[1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.__rgb_threshold(r * 0.6))
        g = int(self.__rgb_threshold(g * 0.6))
        b = int(self.__rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        self.axis.plot(self.x_dataset, avgd_data[self.n_rolling_avg:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.rolling_avg_label)
        self.axis.legend(loc='upper left')

    def __setup_generate_rolling_avg(self, ax):
        avgd_data = np.array([])
        for i in range(len(self.y_dataset) - (len(self.x_dataset) + self.n_rolling_avg), len(self.y_dataset)):
            sum_data = 0
            for j in range(i - self.n_rolling_avg, i):
                sum_data += self.y_dataset[j]
            sum_data /= self.n_rolling_avg
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.color[1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.__rgb_threshold(r * 0.6))
        g = int(self.__rgb_threshold(g * 0.6))
        b = int(self.__rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        ax.plot(self.x_dataset, avgd_data[self.n_rolling_avg:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.rolling_avg_label)
        ax.legend(loc='upper left')

    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axis = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(left=0.07, bottom=0.12, right=0.98, top=0.92, wspace=0.15, hspace=0.38)
        
        if(self.legend):
            self.axis.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth, label=self.label)
            self.axis.legend(loc='upper left')
        else:
            self.axis.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth)
        
        self.axis.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        self.axis.set_xticklabels(labels=self.x_dataset, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        self.axis.set_xlabel(self.x_axis_label, **self.text_font, fontsize=self.x_axis_labelsize)
        self.axis.set_ylabel(self.y_axis_label, **self.text_font, fontsize=self.y_axis_labelsize)
        
        if(self.rolling_avg):
            self.__export_generate_rolling_avg()

        self.axis.grid()

        self.axis.set_title(self.title, fontsize=self.title_size, **self.text_font)
        self.fig.suptitle(self.super_title, fontsize=self.super_title_size, **self.text_font)
        self.fig.savefig(self.filename)

    def set_up_axis(self, ax):
        if(self.legend):
            ax.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth, label=self.label)
            ax.legend(loc='upper left')
        else:
            ax.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth)

        ax.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        ax.set_xticklabels(labels=self.x_dataset, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in ax.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        ax.set_xlabel(self.x_axis_label, **self.text_font, fontsize=self.x_axis_labelsize)
        ax.set_ylabel(self.y_axis_label, **self.text_font, fontsize=self.y_axis_labelsize)
        
        if(self.rolling_avg):
            self.__setup_generate_rolling_avg(ax)
        ax.grid()
        ax.set_title(self.title, fontsize=self.title_size, **self.text_font)
        
class BarPlot:
    # x_dataset -> array
    # y_dataset -> array
    # color -> string
    # label -> string
    # legend -> boolean
    # rolling_avg -> boolean
    # rolling_avg_data -> array
    # n_rolling_avg -> integer
    # rolling_avg_label -> string
    # x_axis_label -> string
    # x_axis_labelsize -> integer
    # x_axis_orientation -> integer
    # x_ticks_size -> integer
    # y_axis_label -> string
    # y_axis_labelsize -> integer
    # title -> string
    # title_size -> integer
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # digit_font -> string
    # filename -> string
    def __init__(self, x_dataset, y_dataset, color, label, legend, rolling_avg, rolling_avg_data, n_rolling_avg,
                 rolling_avg_label, x_axis_label, x_axis_labelsize, x_axis_orientation, x_ticks_size, y_axis_label,
                 y_axis_labelsize, title, title_size, super_title, super_title_size, text_font, digit_font, filename):
            self.x_dataset = x_dataset
            self.y_dataset = y_dataset
            self.color = color
            self.label = label
            self.legend = legend
            self.rolling_avg = rolling_avg
            self.rolling_avg_data = rolling_avg_data
            self.n_rolling_avg = n_rolling_avg
            self.rolling_avg_label = rolling_avg_label
            self.x_axis_label = x_axis_label
            self.x_axis_labelsize = x_axis_labelsize
            self.x_axis_orientation = x_axis_orientation
            self.x_ticks_size = x_ticks_size
            self.y_axis_label = y_axis_label
            self.y_axis_labelsize = y_axis_labelsize
            self.title = title
            self.title_size = title_size
            self.super_title = super_title
            self.super_title_size = super_title_size
            self.text_font = {'fontname': text_font}
            self.digit_font = {'fontname': digit_font}
            self.filename = filename
            self.validate()
    
    def validate(self):
        # Validate len(x_dataset) = len(y_dataset)
        if(len(self.x_dataset) != len(self.y_dataset)):
            sys.exit('Error: x_dataset size does not equal y_dataset size.')

        # Validate if rolling_avg is True and n_rolling_avg is an integer type
        if(self.rolling_avg and (not isinstance(self.n_rolling_avg, int))):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')

        # Validate if rolling_avg is True and 0 <= n_rolling_avg < len(x_dataset) - 1
        if(self.rolling_avg and (self.n_rolling_avg < 0 or self.n_rolling_avg > len(self.x_dataset) - 1)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be greater than 0 and less than', str(len(self.x_dataset) - 1) + '.')

        if(self.rolling_avg and self.n_rolling_avg != len(self.rolling_avg_data) - len(self.y_dataset)):
            sys.exit('Error: rolling_avg is True -> the size of rolling_avg_data must be equal to len(y_dataset) + n_rolling_avg.')
            
        # Validate if color is a string type
        if(not isinstance(self.color, str)):
            sys.exit('Error: color is must be a str type.')

        # Validate first char of color is a pound sign (#)
        if(self.color[0] != '#'):
            sys.exit('Error: color is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that the following 6 chars of color are alphanumeric
        for i in range(1, len(self.color)):
            if(not self.color[i].isalnum()):
                sys.exit('Error: color is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that x_axis_orientation is an integer type
        if(not isinstance(self.x_axis_orientation, int)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')

        # Validate that x_axis_orientation value is either 0, 90, 180, 270, 360
        if(self.x_axis_orientation != 0 and self.x_axis_orientation != 90 and 
           self.x_axis_orientation != 180 and self.x_axis_orientation != 270 and
           self.x_axis_orientation != 360):
            sys.exit('Error: x_axis_orientation must be either 0, 90, 180, 270, 360.')

    def __rgb_threshold(self, color, min=0, max=255):
        if (color < min):
            return min
        if (color > max):
            return max
        return color
    
    def __export_generate_rolling_avg(self):
        avgd_data = np.array([])
        for i in range(len(self.rolling_avg_data) - (len(self.x_dataset) + self.n_rolling_avg), len(self.rolling_avg_data)):
            sum_data = 0
            for j in range(i - self.n_rolling_avg, i):
                sum_data += self.rolling_avg_data[j]
            sum_data /= self.n_rolling_avg
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.color[1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.__rgb_threshold(r * 0.6))
        g = int(self.__rgb_threshold(g * 0.6))
        b = int(self.__rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        self.axis.plot(self.x_dataset, avgd_data[self.n_rolling_avg:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.rolling_avg_label)
        self.axis.legend(loc='upper left')

    def __setup_generate_rolling_avg(self, ax):
        avgd_data = np.array([])
        for i in range(len(self.rolling_avg_data) - (len(self.x_dataset) + self.n_rolling_avg), len(self.rolling_avg_data)):
            sum_data = 0
            for j in range(i - self.n_rolling_avg, i):
                sum_data += self.rolling_avg_data[j]
            sum_data /= self.n_rolling_avg
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.color[1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.__rgb_threshold(r * 0.6))
        g = int(self.__rgb_threshold(g * 0.6))
        b = int(self.__rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        ax.plot(self.x_dataset, avgd_data[self.n_rolling_avg:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.rolling_avg_label)
        ax.legend(loc='upper left')
        
    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axis = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(left=0.07, bottom=0.12, right=0.98, top=0.92, wspace=0.15, hspace=0.38)

        if(self.legend):
            self.axis.legend(loc='upper left')
            self.axis.bar(self.x_dataset, self.y_dataset, color=self.color, label=self.label, zorder=2)
        else:
            self.axis.bar(self.x_dataset, self.y_dataset, color=self.color, zorder=2)
            

        self.axis.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        self.axis.set_xticklabels(labels=self.x_dataset, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        self.axis.set_xlabel(self.x_axis_label, **self.text_font, fontsize=self.x_axis_labelsize)
        self.axis.set_ylabel(self.y_axis_label, **self.text_font, fontsize=self.y_axis_labelsize)

        if(self.rolling_avg):
            self.__export_generate_rolling_avg()

        self.axis.grid(zorder=0)

        self.axis.set_title(self.title, fontsize=self.title_size, **self.text_font)
        self.fig.suptitle(self.super_title, fontsize=self.super_title_size, **self.text_font)
        self.fig.savefig(self.filename)

    def set_up_axis(self, ax):
        if(self.legend):
            ax.legend(loc='upper left')
            ax.bar(self.x_dataset, self.y_dataset, color=self.color, label=self.label, zorder=2)
        else:
            ax.bar(self.x_dataset, self.y_dataset, color=self.color, zorder=2)

        ax.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        ax.set_xticklabels(labels=self.x_dataset, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in ax.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        ax.set_xlabel(self.x_axis_label, **self.text_font, fontsize=self.x_axis_labelsize)
        ax.set_ylabel(self.y_axis_label, **self.text_font, fontsize=self.y_axis_labelsize)

        if(self.rolling_avg):
            self.__setup_generate_rolling_avg(ax)
        ax.grid(zorder=0)
        ax.set_title(self.title, fontsize=self.title_size, **self.text_font)
        

class LayeredScatterPlot:
    # n_datasets -> integer
    # x_dataset -> array
    # y_datasets -> array of arrays
    # linestyles -> array of strings
    # markers -> array of strings
    # colors -> array of strings
    # labels -> array of strings
    # linewidths -> array of strings
    # rolling_avgs -> array of booleans
    # n_rolling_avgs -> array of integers
    # x_axis_label -> string
    # x_axis_labelsize -> integer
    # x_axis_orientation -> integer
    # x_ticks_size -> integer
    # title -> string
    # title_size -> integer
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # digit_font -> string
    # filename -> string
    def __init__(self, n_datasets, x_dataset, y_datasets, linestyles, markers, colors, labels, linewidths, rolling_avgs,
                 n_rolling_avgs, rolling_avg_labels, x_axis_label, x_axis_labelsize, x_axis_orientation, x_ticks_size,
                 y_axis_label, y_axis_labelsize, title, title_size, super_title, super_title_size, text_font, digit_font, filename):
        self.n_datasets = n_datasets
        self.x_dataset  = x_dataset
        self.y_datasets = y_datasets
        self.linestyles = linestyles
        self.markers = markers
        self.colors = colors
        self.labels = labels
        self.linewidths = linewidths
        self.rolling_avgs = rolling_avgs
        self.n_rolling_avgs = n_rolling_avgs
        self.rolling_avg_labels = rolling_avg_labels
        self.x_axis_label = x_axis_label
        self.x_axis_labelsize = x_axis_labelsize
        self.x_axis_orientation = x_axis_orientation
        self.x_ticks_size = x_ticks_size
        self.y_axis_label = y_axis_label
        self.y_axis_labelsize = y_axis_labelsize
        self.title = title
        self.title_size = title_size
        self.super_title = super_title
        self.super_title_size = super_title_size
        self.text_font = {'fontname': text_font}
        self.digit_font = {'fontname': digit_font}
        self.filename = filename
        self.validate()

    def validate(self):
        # Validate n_datasets = len(y_datasets)
        if(self.n_datasets != len(self.y_datasets[i])):
            sys.exit('Error: y_datasets size does not equal n_datasets.')    

        # Validate n_datasets = len(linestyles)
        if(self.n_datasets != len(self.linestyles)): 
            sys.exit('Error: linestyles size does not equal n_datasets.') 

        # Validate n_datasets = len(markers)
        if(self.n_datasets != len(self.markers)): 
            sys.exit('Error: markers size does not equal n_datasets.') 

        # Validate n_datasets = len(colors)
        if(self.n_datasets != len(self.colors)): 
            sys.exit('Error: colors size does not equal n_datasets.') 

        # Validate n_datasets = len(labels)
        if(self.n_datasets != len(self.labels)): 
            sys.exit('Error: labels size does not equal n_datasets.') 

        # Validate n_datasets = len(linewidths)
        if(self.n_datasets != len(self.linewidths)): 
            sys.exit('Error: linewidths size does not equal n_datasets.') 

        # Validate len(x_dataset) = len(y_dataset)
        for i in range(0, self.n_datasets):
            if(len(self.x_dataset) != len(self.y_datasets[i])):
                sys.exit('Error: y_datasets[' + str(i) + '] size does not equal x_dataset size.')   

        # Validate if rolling_avgs[i] is True and n_rolling_avgs[i] is an integer type
        for i in range(0, self.n_datasets):
            if(self.rolling_avgs[i] and (not isinstance(self.n_rolling_avgs[i], int))):    
                sys.exit('Error: rolling_avgs[' + str(i) + '] is True -> n_rolling_avgs[' + str(i) + '] must be an integer.')

        # Validate if rolling_avgs[i] is True and 0 <= n_rolling_avgs[i] < len(x_dataset) - 1
        for i in range(0, self.n_datasets):
            if(self.rolling_avgs[i] and (self.n_rolling_avgs[i] < 0 or self.n_rolling_avgs[i] > len(self.x_dataset) - 1)):
                sys.exit('Error: rolling_avgs[' + str(i) + '] is True -> n_rolling_avg must be greater than 0 and less than', str(len(self.x_dataset) - 1) + '.')
            
        # Validate if colors[i] is a string type
        for i in range(0, self.n_datasets):
            if(not isinstance(self.colors[i], str)):
                sys.exit('Error: colors[' + str(i) + '] is must be a str type.')

        # Validate first char of color is a pound sign (#)
        for i in range(0, self.n_datasets):
            if(self.color[0] != '#'):
               sys.exit('Error: colors[' + str(i) + '] is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that the following 6 chars of color are alphanumeric
        for i in range(0, self.n_datasets):
            for j in range(1, len(self.color)):
                if(not self.colors[i][j].isalnum()):
                    sys.exit('Error: colors[' + str(i) + '] is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that x_axis_orientation is an integer type
        if(not isinstance(self.x_axis_orientation, int)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')

        # Validate that x_axis_orientation value is either 0, 90, 180, 270, 360
        if(self.x_axis_orientation != 0 and self.x_axis_orientation != 90 and 
           self.x_axis_orientation != 180 and self.x_axis_orientation != 270 and
           self.x_axis_orientation != 360):
            sys.exit('Error: x_axis_orientation must be either 0, 90, 180, 270, 360.')

    def __rgb_threshold(self, color, min=0, max=255):
        if (color < min):
            return min
        if (color > max):
            return max
        return color
    
    def __export_generate_rolling_avg(self, idx):
        avgd_data = np.array([])
        for i in range(len(self.y_datasets[idx]) - (len(self.x_dataset) + self.n_rolling_avgs[idx]), len(self.y_datasets[idx])):
            sum_data = 0
            for j in range(i - self.n_rolling_avgs[idx], i):
                sum_data += self.y_datasets[idx][j]
            sum_data /= self.n_rolling_avgs[idx]
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.colors[idx][1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.__rgb_threshold(r * 0.6))
        g = int(self.__rgb_threshold(g * 0.6))
        b = int(self.__rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        self.axis.plot(self.x_dataset, avgd_data[self.n_rolling_avgs[idx]:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.rolling_avg_labels[idx])
        self.axis.legend(loc='upper left')

    def __setup_generate_rolling_avg(self, ax, idx):
        avgd_data = np.array([])
        for i in range(len(self.y_datasets[idx]) - (len(self.x_dataset) + self.n_rolling_avgs[idx]), len(self.y_datasets[idx])):
            sum_data = 0
            for j in range(i - self.n_rolling_avgs[idx], i):
                sum_data += self.y_datasets[idx][j]
            sum_data /= self.n_rolling_avgs[idx]
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.colors[idx][1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.__rgb_threshold(r * 0.6))
        g = int(self.__rgb_threshold(g * 0.6))
        b = int(self.__rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        ax.plot(self.x_dataset, avgd_data[self.n_rolling_avgs[idx]:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.rolling_avg_labels[idx])
        ax.legend(loc='upper left')

    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axis = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(left=0.08, bottom=0.12, right=0.98, top=0.92, wspace=0.15, hspace=0.38)

        if(self.legend):
            for i in range(0, self.n_datasets):
                self.axis.plot(self.x_dataset[i], self.y_datasets[i], color=self.colors[i], linestyle=self.linestyles[i],
                            marker=self.markers[i], linewidth=self.linewidths[i], label=self.labels[i])
            self.axis.legend(loc='upper left')
        else:
            for i in range(0, self.n_datasets):
                self.axis.plot(self.x_dataset[i], self.y_datasets[i], color=self.colors[i], linestyle=self.linestyles[i],
                            marker=self.markers[i], linewidth=self.linewidths[i])
        
        self.axis.tick_params(axis='x',labelrotation=90)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        self.axis.set_xlabel(self.x_label, **self.text_font, fontsize=self.x_axis_label)
        self.axis.set_ylabel(self.y_label, **self.text_font, fontsize=self.y_axis_label)

        for i in range(0, self.n_datasets):
            self.__export_generate_rolling_avg(i)

        self.axis.grid()

        self.axis.set_title(self.title, fontsize=self.title_size, **self.text_font)
        self.fig.suptitle(self.super_title, fontsize=self.super_title_size, **self.text_font)
        self.fig.savefig(self.filename)

    def set_up_axis(self, ax):
        if(self.legend):
            for i in range(0, self.n_datasets):
                ax.plot(self.x_dataset[i], self.y_datasets[i], color=self.colors[i], linestyle=self.linestyles[i],
                        marker=self.markers[i], linewidth=self.linewidths[i], label=self.labels[i])
            ax.legend(loc='upper left')
        else:
            for i in range(0, self.n_datasets):
                ax.plot(self.x_dataset[i], self.y_datasets[i], color=self.colors[i], linestyle=self.linestyles[i],
                        marker=self.markers[i], linewidth=self.linewidths[i])
        
        ax.tick_params(axis='x',labelrotation=90)
        for tick in ax.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        ax.set_xlabel(self.x_label, **self.text_font, fontsize=self.x_axis_label)
        ax.set_ylabel(self.y_label, **self.text_font, fontsize=self.y_axis_label)

        for i in range(0, self.n_datasets):
            self.__setup_generate_rolling_avg(i)
        ax.grid()
        ax.set_title(self.title, fontsize=self.title_size, **self.text_font)

class QuadPlot:
    # plot1 -> ScatterPlot/BarPlot/LayeredScatterPlot
    # plot2 -> ScatterPlot/BarPlot/LayeredScatterPlot
    # plot3 -> ScatterPlot/BarPlot/LayeredScatterPlot
    # plot4 -> ScatterPlot/BarPlot/LayeredScatterPlot
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # filename -> string
    def __init__(self, plot1, plot2, plot3, plot4, super_title, super_title_size, text_font, filename):
        self.plot1 = plot1
        self.plot2 = plot2
        self.plot3 = plot3
        self.plot4 = plot4
        self.super_title = super_title
        self.super_title_size = super_title_size
        self.text_font = {'fontname': text_font}
        self.filename = filename
        self.validate()

    def validate(self):
        self.plot1.validate()
        self.plot2.validate()
        self.plot3.validate()
        self.plot4.validate()

    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axes = [self.fig.add_subplot(2,2,1),
                     self.fig.add_subplot(2,2,2),
                     self.fig.add_subplot(2,2,3),
                     self.fig.add_subplot(2,2,4)]
        self.fig.subplots_adjust(left=0.05, bottom=0.08, right=0.98, top=0.94, wspace=0.15, hspace=0.38)

        self.plot1.set_up_axis(self.axes[0])
        self.plot2.set_up_axis(self.axes[1])
        self.plot3.set_up_axis(self.axes[2])
        self.plot4.set_up_axis(self.axes[3])

        self.fig.suptitle(self.super_title, fontsize=self.super_title_size, **self.text_font)
        self.fig.savefig(self.filename)

############################################################################################################################################################

#import random
#xdata1 = [i for i in range(0, 100)]
#ydata1 = [random.uniform(1, 2) for i in range(0,100)]
#p1 = ScatterPlot(
#    xdata1,
#    ydata1,
#    '-',
#    'o',
#    '#5B90F3',
#    True,
#    'data',
#    2.5,
#    True,
#    5,
#    'avg 5',
#    'xaxis',
#    12,
#    90,
#    12,
#    'yaxis',
#    12,
#    'my title 1',
#    20,
#    'username',
#    10,
#    'Bahnschrift',
#    'Consolas',
#    'output1.png'
#)
#p1.export()
#
#xdata2 = [i for i in range(0, 30)]
#ydata2 = [random.uniform(1, 2) for i in range(0,30)]
#p2 = BarPlot(
#    xdata2,
#    ydata2,
#    '#8C8C8C',
#    '',
#    False,
#    True,
#    10,
#    'avg 10',
#    'days',
#    12,
#    90,
#    12,
#    'cases',
#    12,
#    'my title 2',
#    20,
#    'username',
#    10,
#    'Bahnschrift',
#    'Consolas',
#    'output2.png'    
#)
#p2.export()
#
#p3 = QuadPlot(
#    p1, 
#    p2,
#    p1,
#    p2,
#    'username',
#    12,
#    'Bahnschrift',
#    'output3.png'
#)
#p3.export()