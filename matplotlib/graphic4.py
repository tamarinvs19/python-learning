import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 10.0, 0.01)
s = np.exp(-t/2.) * np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax.plot(t, s, 'o')


ax.set(xlabel='x', ylabel='y')
ax.grid()

plt.show()
