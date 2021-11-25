import sys
from math import sqrt
import numpy as np

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
        print(self.mean, self.stdev)

    def plot_gauss_bell():
        self.plot = LayeredScatterPlot()
        return 0

data = np.array([5,98,4,94,6,46,4,6,48,2,1,854,62,6,5,4,3,65,6,6,9,869,2,1,68,3,61,9,3,57,3,3,5,553,53,3,35,9])
tmp = Stats(data)