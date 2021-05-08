from matplotlib.figure import Figure
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
        
class ScatterPlot:
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

        self.axis.plot(self.x_data, self.y_data, color=self.color_plot)
        self.axis.plot(self.x_data, self.y_data, 'ko')
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
            if(len(self.ravg_ydata) == 0):
                sys.exit('Rolling average ydata is empty')
            self.generate_rolling_average()
        self.axis.grid()

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