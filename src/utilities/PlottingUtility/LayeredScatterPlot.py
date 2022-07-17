from matplotlib.figure import Figure
import numpy as np
import sys

class LayeredScatterPlot:
    # n_datasets -> integer
    # x_dataset -> array
    # y_datasets -> array of arrays
    # linestyles -> array of strings
    # markers -> array of strings
    # colors -> array of strings
    # labels -> array of strings
    # legend -> boolean
    # linewidths -> array of strings
    # rolling_avgs -> array of booleans
    # rolling_avgs_data -> array of arrays
    # n_rolling_avgs -> array of integers
    # x_axis_label -> string
    # x_axis_labelsize -> integer
    # x_axis_orientation -> integer
    # x_ticks_size -> integer
    # x_ticks_interval -> integer
    # title -> string
    # title_size -> integer
    # super_title -> string
    # super_title_size -> integer
    # text_font -> string
    # digit_font -> string
    # filename -> string
    def __init__(self, n_datasets, x_dataset, y_datasets, linestyles, markers, colors, labels, legend, linewidths, rolling_avgs, rolling_avgs_data, 
                 n_rolling_avgs, rolling_avg_labels, x_axis_label, x_axis_labelsize, x_axis_orientation, x_ticks_size, x_ticks_interval,
                 y_axis_label, y_axis_labelsize, title, title_size, super_title, super_title_size, text_font, digit_font, filename):
        self.n_datasets = n_datasets
        self.x_dataset  = x_dataset
        self.y_datasets = y_datasets
        self.linestyles = linestyles
        self.markers = markers
        self.colors = colors
        self.labels = labels
        self.legend = legend
        self.linewidths = linewidths
        self.rolling_avgs = rolling_avgs
        self.rolling_avgs_data = rolling_avgs_data
        self.n_rolling_avgs = n_rolling_avgs
        self.rolling_avg_labels = rolling_avg_labels
        self.x_axis_label = x_axis_label
        self.x_axis_labelsize = x_axis_labelsize
        self.x_axis_orientation = x_axis_orientation
        self.x_ticks_size = x_ticks_size
        self.x_ticks_interval = x_ticks_interval
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
        if(self.n_datasets != len(self.y_datasets)):
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
                sys.exit('Error: rolling_avgs[' + str(i) + '] is True -> n_rolling_avg must be greater than 0 and less than ' + str(len(self.x_dataset) - 1) + '.')

        # Validate if rolling_avgs[i] is True and n_rolling_avgs[i] = len(self.rolling_avgs_data[i]) - len(y_datasets[i])
        for i in range(0, self.n_datasets):
            if(self.rolling_avgs[i] and self.n_rolling_avgs[i] != len(self.rolling_avgs_data[i]) - len(self.y_datasets[i])):
                sys.exit('Error: rolling_avgs[i] is True -> the size of rolling_avgs_data[i] must be equal to len(y_datasets[i]) + n_rolling_avg[i].')
            
        # Validate if colors[i] is a string type
        for i in range(0, self.n_datasets):
            if(not isinstance(self.colors[i], str)):
                sys.exit('Error: colors[' + str(i) + '] is must be a str type.')

        # Validate first char of color is a pound sign (#)
        for i in range(0, self.n_datasets):
            if(self.colors[i][0] != '#'):
               sys.exit('Error: colors[' + str(i) + '] is must be a string with a HEX value for a color -> ex: #FFFFFF.')

        # Validate that the following 6 chars of color are alphanumeric
        for i in range(0, self.n_datasets):
            for j in range(1, len(self.colors)):
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
        for i in range(len(self.rolling_avgs_data[idx]) - (len(self.x_dataset) + self.n_rolling_avgs[idx]), len(self.rolling_avgs_data[idx])):
            sum_data = 0
            for j in range(i - self.n_rolling_avgs[idx], i):
                sum_data += self.rolling_avgs_data[idx][j]
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
        for i in range(len(self.rolling_avgs_data[idx]) - (len(self.x_dataset) + self.n_rolling_avgs[idx]), len(self.rolling_avgs_data[idx])):
            sum_data = 0
            for j in range(i - self.n_rolling_avgs[idx], i):
                sum_data += self.rolling_avgs_data[idx][j]
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
                self.axis.plot(self.x_dataset, self.y_datasets[i], color=self.colors[i], linestyle=self.linestyles[i],
                            marker=self.markers[i], linewidth=self.linewidths[i], label=self.labels[i])
            self.axis.legend(loc='upper left')
        else:
            for i in range(0, self.n_datasets):
                self.axis.plot(self.x_dataset, self.y_datasets[i], color=self.colors[i], linestyle=self.linestyles[i],
                            marker=self.markers[i], linewidth=self.linewidths[i])
        
        self.axis.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        x_axis_ticks = []
        for i in range(0, len(self.x_dataset)):
            if(i % self.x_ticks_interval == 0):
                x_axis_ticks.insert(0, self.x_dataset[len(self.x_dataset) - i - 1])
            else:
                x_axis_ticks.insert(0, '')
        self.axis.set_xticklabels(labels=x_axis_ticks, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in self.axis.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        self.axis.set_xlabel(self.x_axis_label, **self.text_font, fontsize=self.x_axis_labelsize)
        self.axis.set_ylabel(self.y_axis_label, **self.text_font, fontsize=self.y_axis_labelsize)

        for i in range(0, self.n_datasets):
            if(self.rolling_avgs[i]):
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
        
        ax.tick_params(axis='x',labelrotation=self.x_axis_orientation)
        x_axis_ticks = []
        for i in range(0, len(self.x_dataset)):
            if(i % self.x_ticks_interval == 0):
                x_axis_ticks.insert(0, self.x_dataset[len(self.x_dataset) - i - 1])
            else:
                x_axis_ticks.insert(0, '')
        self.axis.set_xticklabels(labels=x_axis_ticks, fontsize=self.x_ticks_size, **self.digit_font)
        for tick in ax.get_yticklabels():
            tick.set_fontname(**self.digit_font)
            tick.set_fontsize(self.x_ticks_size)
        ax.set_xlabel(self.x_label, **self.text_font, fontsize=self.x_axis_label)
        ax.set_ylabel(self.y_label, **self.text_font, fontsize=self.y_axis_label)

        for i in range(0, self.n_datasets):
            self.__setup_generate_rolling_avg(i)
        ax.grid()
        ax.set_title(self.title, fontsize=self.title_size, **self.text_font)