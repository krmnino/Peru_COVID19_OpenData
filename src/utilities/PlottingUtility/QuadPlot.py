from matplotlib.figure import Figure
import warnings

warnings.filterwarnings('ignore')

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
        self.fig.subplots_adjust(left=0.05, bottom=0.10, right=0.98, top=0.94, wspace=0.15, hspace=0.33)

        self.plot1.set_up_axis(self.axes[0])
        self.plot2.set_up_axis(self.axes[1])
        self.plot3.set_up_axis(self.axes[2])
        self.plot4.set_up_axis(self.axes[3])

        self.fig.suptitle(self.super_title, fontsize=self.super_title_size, **self.text_font)
        self.fig.savefig(self.filename)