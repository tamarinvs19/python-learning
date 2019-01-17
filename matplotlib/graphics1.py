import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(-8.0, 8.0, 0.01)
a = (abs(25 - x**2))**0.5
b = -0.05*x**2 + 1.25
c = np.cos(x) + 4
d = x*np.sign(x)

fig, ax = plt.subplots()
ax.plot(x, a)
ax.plot(x, b)
ax.plot(x, c)
ax.plot(x, d)

ax.set(xlabel='x', ylabel='y',
        title='Graphics')
ax.grid()

# fig.savefig("test.png")
plt.show()
