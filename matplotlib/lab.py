# from cycler import cycler
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# default_cycler = (cycler(color=['b', 'c', 'r', 'y']) +
#         cycler(linestyle=['-', ':', '-.', '--']))
#
# plt.rc('lines', linewidth=4)
# plt.rc('axes', prop_cycle=default_cycler)
# Data for plotting
x = np.arange(0, 10.0, 0.05)
z = np.arange(0, 10.0, 0.05)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

fig, ax = plt.subplots()
ax.plot(x, y, 'x')
ax.plot(z, y)
ax.set_xlim(-0.5, 10)
ax.set_ylim(-1, 1)
ax.set(xlabel='t, s', ylabel='U, V', title='Voltage')
ax.grid()

plt.show()
