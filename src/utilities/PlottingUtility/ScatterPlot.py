from matplotlib.figure import Figure
import warnings
import numpy as np
import sys

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
    # rolling_avg_data -> array
    # n_rolling_avg -> integer
    # rolling_avg_label -> string
    # x_axis_label -> string
    # x_axis_labelsize -> integer
    # x_axis_orientation -> integer
    # x_ticks_size -> integer
    # x_ticks_interval -> integer
    # y_axis_label -> string
    # y_axis_labelsize -> integer
    # title -> string
    # title_size -> integer
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # digit_font -> string
    # filename -> string
    def __init__(self, x_dataset, y_dataset, linestyle, marker, color, label, linewidth, legend, rolling_avg, rolling_avg_data,
                 n_rolling_avg, rolling_avg_label, x_axis_label, x_axis_labelsize, x_axis_orientation, x_ticks_size, x_ticks_interval,
                 y_axis_label, y_axis_labelsize, title, title_size, super_title, super_title_size, text_font, digit_font, filename):
        self.x_dataset  = x_dataset
        self.y_dataset = y_dataset
        self.linestyle = linestyle
        self.marker = marker
        self.color = color
        self.label = label
        self.linewidth = linewidth
        self.legend = legend
        self.rolling_avg = rolling_avg
        self.rolling_avg_data = rolling_avg_data
        self.n_rolling_avg = n_rolling_avg
        self.rolling_avg_label = rolling_avg_label
        self.x_axis_label = x_axis_label
        self.x_axis_labelsize = x_axis_labelsize
        self.x_axis_orientation = x_axis_orientation
        self.x_ticks_size = x_ticks_size
        self.x_tick_interval = x_ticks_interval
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

        # Validate if rolling_avg is True and n_rolling_avg = len(self.rolling_avg_data) - len(y_dataset)
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
            self.axis.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth, label=self.label)
            self.axis.legend(loc='upper left')
        else:
            self.axis.plot(self.x_dataset, self.y_dataset, color=self.color, linestyle=self.linestyle, marker=self.marker, linewidth=self.linewidth)
        
        self.axis.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        x_axis_ticks = []
        for i in range(0, len(self.x_dataset)):
            if(i % self.x_tick_interval == 0):
                x_axis_ticks.insert(0, self.x_dataset[len(self.y_dataset) - i - 1])
            else:
                x_axis_ticks.insert(0, '')
        self.axis.set_xticklabels(labels=x_axis_ticks, fontsize=self.x_ticks_size, **self.digit_font)
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
        x_axis_ticks = []
        for i in range(0, len(self.x_dataset)):
            if(i % self.x_tick_interval == 0):
                x_axis_ticks.insert(0, self.x_dataset[len(self.y_dataset) - i - 1])
            else:
                x_axis_ticks.insert(0, '')
        ax.set_xticklabels(labels=x_axis_ticks, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in ax.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        ax.set_xlabel(self.x_axis_label, **self.text_font, fontsize=self.x_axis_labelsize)
        ax.set_ylabel(self.y_axis_label, **self.text_font, fontsize=self.y_axis_labelsize)
        
        if(self.rolling_avg):
            self.__setup_generate_rolling_avg(ax)
        ax.grid()
        ax.set_title(self.title, fontsize=self.title_size, **self.text_font)