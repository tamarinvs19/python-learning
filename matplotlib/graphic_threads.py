import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 17, 1)
y = np.arange(1, 16, 1)

fig, ax = plt.subplots()
ax.plot(x, y, 'x')
ax.plot(x, y)
ax.set_xlim(1.5, 16.5)
ax.set_ylim(0, 30)
ax.set(xlabel='Количество потоков', ylabel='Время на обработку, мин', title='График времени обработки в зависимости от количества потоков')
ax.grid()

plt.show()
