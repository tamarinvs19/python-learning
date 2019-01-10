import matplotlib.pyplot as plt
import numpy as np
from math import sin
def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2 = np.random.randn(2, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
