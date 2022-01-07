from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import warnings
import numpy as np
import sys

warnings.filterwarnings('ignore')

class QuadPlot:
    def __init__(self, colors_sp, titles_sp, enable_rolling_avg_sp, type_sp, x_label_sp, y_label_sp, x_data, y_data, stitle, ofile,
                 ravg_days=[1, 1, 1, 1], ravg_labels=[None, None, None, None], ravg_ydata=[None, None, None, None]):        
        if(len(colors_sp) != 4):
            sys.exit('colors_sp does not equal 4')
        else:
            self.colors_subplots = colors_sp
        
        if(len(titles_sp) != 4):
            sys.exit('titles_sp does not equal 4')
        else:
            self.titles_subplots = titles_sp

        if(len(enable_rolling_avg_sp) != 4):
            sys.exit('enable_rolling_avg_sp does not equal 4')
        else:
            self.enable_rolling_avg_subplots = enable_rolling_avg_sp

        if(len(type_sp) != 4):
            sys.exit('type_sp does not equal 4')
        else:
            self.type_subplots = type_sp

        if(len(x_label_sp) != 4):
            sys.exit('x_label_sp does not equal 4')
        else:
            self.x_label_subplots = x_label_sp

        if(len(y_label_sp) != 4):
            sys.exit('y_label_sp does not equal 4')
        else:
            self.y_label_subplots = y_label_sp

        if(len(x_data) != 4):
            sys.exit('x_data does not equal 4')
        else:
            self.x_data = x_data

        if(len(y_data) != 4):
            sys.exit('y_data does not equal 4')
        else:
            self.y_data = y_data

        if(len(ravg_days) != 4):
            sys.exit('ravg_days does not equal 4')
        else:
            self.ravg_days = ravg_days

        if(len(ravg_labels) != 4):
            sys.exit('ravg_labels does not equal 4')
        else:
            self.ravg_labels = ravg_labels

        if(len(ravg_ydata) != 4):
            sys.exit('ravg_ydata does not equal 4')
        else:
            self.ravg_ydata = ravg_ydata

        for i in range(0, 4):
            if(self.enable_rolling_avg_subplots[i] and self.ravg_days[i] < 0):
                sys.exit('ravg_days[' + str(i) + '] must be 1 or greater if rolling average is enabled')
            if(self.enable_rolling_avg_subplots[i] and self.ravg_labels[i] == None):
                sys.exit('ravg_labels[' + str(i) + '] cannot be None if rolling average is enabled')

        self.suptitle = stitle
        self.out_file = ofile
        self.text_font = {'fontname':'Bahnschrift'}
        self.digit_font = {'fontname':'Consolas'}

    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axes = [self.fig.add_subplot(2,2,1),
                     self.fig.add_subplot(2,2,2),
                     self.fig.add_subplot(2,2,3),
                     self.fig.add_subplot(2,2,4)]
        self.fig.subplots_adjust(left=0.05, bottom=0.10, right=0.98, top=0.94, wspace=0.15, hspace=0.38)

        for i in range(0, 4):
            if(self.type_subplots[i] == 'bar'):
                self.bar_plot(i)
            elif(self.type_subplots[i] == 'scatter'):
                self.scatter_plot(i)

            if(self.enable_rolling_avg_subplots[i]):
                self.generate_rolling_average(i)
        
        self.fig.suptitle(self.suptitle, fontsize=10, **self.text_font)
        self.fig.savefig(self.out_file)

    def bar_plot(self, index):
        self.axes[index].grid(zorder=0)
        self.axes[index].bar(self.x_data[index], self.y_data[index], color=self.colors_subplots[index], zorder=2)
        self.axes[index].set_title(self.titles_subplots[index], fontsize=14, **self.text_font)
        self.axes[index].tick_params(axis='x',labelrotation=90)
        self.axes[index].set_xticklabels(labels=self.x_data[index], fontsize=8, **self.digit_font)
        for tick in self.axes[index].get_yticklabels():
            tick.set_fontname(**self.digit_font)
        self.axes[index].set_xlabel(self.x_label_subplots[index], **self.text_font)
        self.axes[index].set_ylabel(self.y_label_subplots[index], **self.text_font)

    def scatter_plot(self, index):
        self.axes[index].plot(self.x_data[index], self.y_data[index], color=self.colors_subplots[index])
        self.axes[index].plot(self.x_data[index], self.y_data[index], 'ko')
        self.axes[index].set_title(self.titles_subplots[index], fontsize=14, **self.text_font)
        self.axes[index].tick_params(axis='x',labelrotation=90)
        self.axes[index].set_xticklabels(labels=self.x_data[index], fontsize=8, **self.digit_font)
        for tick in self.axes[index].get_yticklabels():
            tick.set_fontname(**self.digit_font)
        self.axes[index].set_xlabel(self.x_label_subplots[index], **self.text_font)
        self.axes[index].set_ylabel(self.y_label_subplots[index], **self.text_font)
        self.axes[index].grid()

    def rgb_threshold(self, color, min=0, max=255):
        if (color < min):
            return min
        if (color > max):
            return max
        return color
    
    def generate_rolling_average(self, index):
        avgd_data = np.array([])
        for i in range(len(self.ravg_ydata[index]) - (len(self.x_data[index]) + self.ravg_days[index]), len(self.ravg_ydata[index])):
            sum_data = 0
            for j in range(i - self.ravg_days[index], i):
                sum_data += self.ravg_ydata[index][j]
            sum_data /= self.ravg_days[index]
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.colors_subplots[index][1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.rgb_threshold(r * 0.6))
        g = int(self.rgb_threshold(g * 0.6))
        b = int(self.rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        self.axes[index].plot(self.x_data[index], avgd_data[self.ravg_days[index]:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.ravg_labels[index])
        self.axes[index].legend(loc='upper left')
    
    def get_path(self):
        return self.out_file
        
#class ScatterPlot:
#    def __init__(self, color, linestyle, marker, title, enable_rolling_avg, x_label, y_label, x_data, y_data, stitle, ofile, ravg=1, ravg_label='', ravg_ydata=[]):
#        self.color_plot = color
#        self.linestyle_plot = linestyle
#        self.marker_plot = marker
#        self.title_plot = title
#        self.enable_rolling_avg_plot = enable_rolling_avg
#        self.ravg_days = ravg
#        self.ravg_label = ravg_label
#        self.ravg_ydata = ravg_ydata
#        self.x_label_plot = x_label
#        self.y_label_plot = y_label
#        self.x_data = x_data
#        self.y_data = y_data
#        self.suptitle = stitle
#        self.out_file = ofile
#        self.text_font = {'fontname':'Bahnschrift'}
#        self.digit_font = {'fontname':'Consolas'}
#    
#    def export(self):
#        self.fig = Figure(figsize=(14, 10), dpi=200)
#        self.axis = self.fig.add_subplot(1,1,1)
#        self.fig.subplots_adjust(left=0.07, bottom=0.14, right=0.98, top=0.92, wspace=0.15, hspace=0.38)
#
#        self.axis.plot(self.x_data, self.y_data, color=self.color_plot, linestyle=self.linestyle_plot, marker=self.marker_plot)
#        self.axis.set_title(self.title_plot, fontsize=22, **self.text_font)
#        self.axis.tick_params(axis='x',labelrotation=90)
#        self.axis.set_xticklabels(labels=self.x_data, fontsize=12, **self.digit_font)
#        for tick in self.axis.get_yticklabels():
#            tick.set_fontname(**self.digit_font)
#            tick.set_fontsize(12)
#        self.axis.set_xlabel(self.x_label_plot, **self.text_font, fontsize=12)
#        self.axis.set_ylabel(self.y_label_plot, **self.text_font, fontsize=12)
#        if(self.enable_rolling_avg_plot):
#            if(len(self.ravg_label) == 0):
#                sys.exit('Rolling average label or ydata is empty')
#            if(len(self.ravg_ydata) == 0):
#                sys.exit('Rolling average ydata is empty')
#            self.generate_rolling_average()
#        self.axis.grid()
#
#        self.fig.suptitle(self.suptitle, fontsize=12, **self.text_font)
#        self.fig.savefig(self.out_file)
#
#    def rgb_threshold(self, color, min=0, max=255):
#        if (color < min):
#            return min
#        if (color > max):
#            return max
#        return color
#
#    def generate_rolling_average(self):
#        avgd_data = np.array([])
#        for i in range(len(self.ravg_ydata) - (len(self.x_data) + self.ravg_days), len(self.ravg_ydata)):
#            sum_data = 0
#            for j in range(i - self.ravg_days, i):
#                sum_data += self.ravg_ydata[j]
#            sum_data /= self.ravg_days
#            avgd_data = np.append(avgd_data, sum_data)
#
#        color_to_string = self.color_plot[1:] 
#        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
#        r = int(self.rgb_threshold(r * 0.6))
#        g = int(self.rgb_threshold(g * 0.6))
#        b = int(self.rgb_threshold(b * 0.6))
#        avg_color = "#%02x%02x%02x" % (r, g, b)
#
#        self.axis.plot(self.x_data, avgd_data[self.ravg_days:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.ravg_label)
#        self.axis.legend(loc='upper left')
#
#    def get_path(self):
#        return self.out_file

class BarPlot:
    def __init__(self, color, title, enable_rolling_avg, x_label, y_label, x_data, y_data, stitle, ofile, ravg=1, ravg_label='', ravg_ydata=[]):
        self.color_plot = color
        self.title_plot = title
        self.enable_rolling_avg_plot = enable_rolling_avg
        self.ravg_days = ravg
        self.ravg_label = ravg_label
        self.ravg_ydata = ravg_ydata
        self.x_label_plot = x_label
        self.y_label_plot = y_label
        self.x_data = x_data
        self.y_data = y_data
        self.suptitle = stitle
        self.out_file = ofile
        self.text_font = {'fontname':'Bahnschrift'}
        self.digit_font = {'fontname':'Consolas'}            
    
    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axis = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(left=0.07, bottom=0.14, right=0.98, top=0.92, wspace=0.15, hspace=0.38)

        self.axis.grid(zorder=0)
        self.axis.bar(self.x_data, self.y_data, color=self.color_plot, zorder=2)
        self.axis.set_title(self.title_plot, fontsize=22, **self.text_font)
        self.axis.tick_params(axis='x',labelrotation=90)
        self.axis.set_xticklabels(labels=self.x_data, fontsize=12, **self.digit_font)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(12)
        self.axis.set_xlabel(self.x_label_plot, **self.text_font, fontsize=12)
        self.axis.set_ylabel(self.y_label_plot, **self.text_font, fontsize=12)
        if(self.enable_rolling_avg_plot):
            if(len(self.ravg_label) == 0):
                sys.exit('Rolling average label or ydata is empty')
            if(len(self.ravg_ydata == None) == 0):
                sys.exit('Rolling average ydata is empty')
            self.generate_rolling_average()

        self.fig.suptitle(self.suptitle, fontsize=12, **self.text_font)
        self.fig.savefig(self.out_file)

    def rgb_threshold(self, color, min=0, max=255):
        if (color < min):
            return min
        if (color > max):
            return max
        return color

    def generate_rolling_average(self):
        avgd_data = np.array([])
        for i in range(len(self.ravg_ydata) - (len(self.x_data) + self.ravg_days), len(self.ravg_ydata)):
            sum_data = 0
            for j in range(i - self.ravg_days, i):
                sum_data += self.ravg_ydata[j]
            sum_data /= self.ravg_days
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.color_plot[1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.rgb_threshold(r * 0.6))
        g = int(self.rgb_threshold(g * 0.6))
        b = int(self.rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        self.axis.plot(self.x_data, avgd_data[self.ravg_days:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.ravg_label)
        self.axis.legend(loc='upper left')

    def get_path(self):
        return self.out_file

class LayeredScatterPlot:
    def __init__(self, n_datasets, colors_ds, linestyle_ds, markers_ds, title, enable_rolling_avg_ds, x_label, y_label,
                 x_data, y_data, stitle, ofile, ravg_days_ds, ravg_labels_ds, ravg_ydata_ds):
        self.n_datasets = n_datasets
        
        if(len(colors_ds) != self.n_datasets):
            sys.exit('colors_ds size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.colors_datasets = colors_ds

        if(len(linestyle_ds) != self.n_datasets):
            sys.exit('linestyle_ds size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.linestyle_datasets = linestyle_ds

        if(len(markers_ds) != self.n_datasets):
            sys.exit('markers_ds size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.markers_datasets = markers_ds

        if(len(enable_rolling_avg_ds) != self.n_datasets):
            sys.exit('enable_rolling_avg_ds size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.enable_rolling_avg_datasets = enable_rolling_avg_ds

        if(len(x_data) != self.n_datasets):
            sys.exit('x_data size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.x_data = x_data

        if(len(y_data) != self.n_datasets):
            sys.exit('y_data size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.y_data = y_data

        if(len(ravg_days_ds) != self.n_datasets):
            sys.exit('ravg_days size does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.ravg_days_datasets = ravg_days_ds

        if(len(ravg_labels_ds) != self.n_datasets):
            sys.exit('ravg_labels_ds does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.ravg_labels_datasets = ravg_labels_ds

        if(len(ravg_ydata_ds) != self.n_datasets):
            sys.exit('ravg_ydata does not equal the expected n_datasets value (' + str(n_datasets) + ')')
        else:
            self.ravg_ydata_datasets = ravg_ydata_ds

        for i in range(0, self.n_datasets):
            if(self.enable_rolling_avg_datasets[i] and self.ravg_days_datasets[i] < 0):
                sys.exit('ravg_days_datasets[' + str(i) + '] must be 1 or greater if rolling average is enabled')
            if(self.enable_rolling_avg_datasets[i] and self.ravg_labels_datasets[i] == None):
                sys.exit('ravg_labels_datasets[' + str(i) + '] cannot be None if rolling average is enabled')

        self.title_plot = title
        self.x_label = x_label
        self.y_label = y_label
        self.suptitle = stitle
        self.out_file = ofile
        self.text_font = {'fontname':'Bahnschrift'}
        self.digit_font = {'fontname':'Consolas'}

    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axis = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(left=0.07, bottom=0.14, right=0.98, top=0.92, wspace=0.15, hspace=0.38)

        for i in range(0, self.n_datasets):
            self.axis.plot(self.x_data[i], self.y_data[i], color=self.colors_datasets[i],
                           linestyle=self.linestyle_datasets[i], marker=self.markers_datasets[i])
        
        self.axis.tick_params(axis='x',labelrotation=90)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(12)
        self.axis.set_xlabel(self.x_label, **self.text_font, fontsize=12)
        self.axis.set_ylabel(self.y_label, **self.text_font, fontsize=12)
        for i in range(0, self.n_datasets):
            if(self.enable_rolling_avg_datasets[i]):
                if(len(self.ravg_labels_datasets[i]) == 0):
                    sys.exit('Rolling average label or ydata is empty')
                if(len(self.ravg_ydata_datasets[i] == None) == 0):
                    sys.exit('Rolling average ydata is empty')
                self.generate_rolling_average(i)

        self.axis.set_title(self.title_plot, fontsize=22, **self.text_font)
        self.axis.grid()
        
        self.fig.suptitle(self.suptitle, fontsize=12, **self.text_font)
        self.fig.savefig(self.out_file)
        
    def rgb_threshold(self, color, min=0, max=255):
        if (color < min):
            return min
        if (color > max):
            return max
        return color

    def generate_rolling_average(self, idx):
        avgd_data = np.array([])
        for i in range(len(self.ravg_ydata_datasets[idx]) - (len(self.x_data[idx]) + self.ravg_days_datasets[idx]), len(self.ravg_ydata_datasets[idx])):
            sum_data = 0
            for j in range(i - self.ravg_days_datasets[i], i):
                sum_data += self.ravg_ydata_datasets[idx][j]
            sum_data /= self.ravg_days_datasets[i]
            avgd_data = np.append(avgd_data, sum_data)

        color_to_string = self.colors_datasets[idx][1:] 
        r, g, b = int(color_to_string[0:2], 16), int(color_to_string[2:4], 16), int(color_to_string[4:], 16)
        r = int(self.rgb_threshold(r * 0.6))
        g = int(self.rgb_threshold(g * 0.6))
        b = int(self.rgb_threshold(b * 0.6))
        avg_color = "#%02x%02x%02x" % (r, g, b)

        self.axis.plot(self.x_data[idx], avgd_data[self.ravg_days_datasets[idx]:], linestyle='dashed', 
                       linewidth=2.5, color=avg_color, label=self.ravg_labels_datasets[idx])
        self.axis.legend(loc='upper left')

    def get_path(self):
        return self.out_file

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
    # x_axis_labelsize =-> string
    # x_axis_orientation -> integer
    # x_ticks_size -> integer
    # title -> string
    # title_size -> integer
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # digit_font -> string
    # filename -> string
    def __init__(self, x_dataset, y_dataset, linestyle, marker, color, label, linewidth, rolling_avg, n_rolling_avg,
                 rolling_avg_label, x_axis_label, x_axis_labelsize, x_axis_orientation, x_ticks_size, y_axis_label,
                 y_axis_labelsize, title, title_size, super_title, super_title_size, text_font, digit_font, legend, filename):
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
        self.__validate()

    def __validate(self):
        # Validate len(x_dataset) = len(y_dataset)
        if(len(self.x_dataset) != len(self.y_dataset)):
            sys.exit('Error: x_dataset size does not equal y_dataset size.')
        if(self.rolling_avg and (not isinstance(self.n_rolling_avg, int))):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')
        if(self.rolling_avg and (self.n_rolling_avg < 0 or self.n_rolling_avg > len(self.x_dataset) - 1)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be greater than 0 and less than', str(len(self.x_dataset) - 1) + '.')
        if(not isinstance(self.color, str)):
            sys.exit('Error: color is must be a str type.')
        if(self.color[0] != '#'):
            sys.exit('Error: color is must be a string with a HEX value for a color -> ex: #FFFFFF.')
        for i in range(1, len(self.color)):
            if(not self.color[i].isalnum()):
                sys.exit('Error: color is must be a string with a HEX value for a color -> ex: #FFFFFF.')
        if(not isinstance(self.x_axis_orientation, int)):
            sys.exit('Error: rolling_avg is True -> n_rolling_avg must be an integer.')
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
    
    def __generate_rolling_avg(self):
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

        self.axis.plot(self.x_dataset, avgd_data[self.n_rolling_avg:], linestyle='dashed', linewidth=2.5, color=avg_color, label=self.x_ravg_label)
        self.axis.legend(loc='upper left')

    def export(self):
        self.fig = Figure(figsize=(14, 10), dpi=200)
        self.axis = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(left=0.07, bottom=0.08, right=0.98, top=0.92, wspace=0.15, hspace=0.38)
        
        self.axis.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth)
        
        self.axis.set_title(self.title, fontsize=self.title_size, **self.text_font)
        self.axis.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        self.axis.set_xticklabels(labels=self.x_dataset, fontsize=12, **self.digit_font)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        self.axis.set_xlabel(self.x_axis_label, **self.text_font, fontsize=12)
        self.axis.set_ylabel(self.y_axis_label, **self.text_font, fontsize=12)
        
        if(self.rolling_avg):
            self.__generate_rolling_avg()
        
        self.axis.grid()

        self.fig.suptitle(self.super_title, fontsize=self.super_title_size, **self.text_font)
        self.fig.savefig(self.filename)
        

import random
xdata = [i for i in range(0, 100)]
ydata = [random.uniform(1, 2) for i in range(0,100)]
p = ScatterPlot(
    xdata,
    ydata,
    '-',
    'o',
    '#5B90F3',
    '',
    2.5,
    False,
    0,
    '',
    'xaxis',
    12,
    90,
    12,
    'xaxis',
    12,
    'my title',
    20,
    'username',
    10,
    'Bahnschrift',
    'Consolas',
    True,
    'output.png'
)
p.display()