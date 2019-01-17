from scipy.optimize import newton
from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2**abs(x+5)+ 6*sin(x)**2 + 5*sin(x + pi/2)-8

print(newton(f, 0))
print(newton(f, -7))
print(newton(f, -5.5))
print(newton(f, -5))

x = np.linspace(-10, 0, 100)
y = np.array(list(map(f,x)))

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set(xlabel='x', ylabel='y', title='Graphic')

ax.grid()
plt.show()
