import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

plt.plot(x, x**np.sign(x), label='a')
plt.plot(x, (x+5)*(x-2)*(x+6), label='b')
plt.plot(x, 5*x*np.sin(x), label='c')
plt.plot(x, np.degrees((np.sign(x)*x)**0.5), label='d')
plt.plot(x, 0.5**x, label='e')

plt.xlabel('x label')
plt.ylabel('y label')

plt.legend()

plt.show()
