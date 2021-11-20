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

    def plot_gauss_bell():
        return 0
        