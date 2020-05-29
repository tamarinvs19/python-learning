import timeit

times_perm = []
times_iter = []
for i in range(4, 11):
    setup = f'import permutations; i = {i}'
    time_perm = timeit.timeit('permutations.perms(i, i)', number=1, setup=setup)
    time_iter = timeit.timeit('permutations.iter_perms(i, i)', number=1, setup=setup)
    print(f'{i}, perm:' , time_perm)
    print(f'{i}, iter:', time_iter)
    times_perm.append(time_perm)
    times_iter.append(time_iter)


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(4, 11, 1)

plt.plot(x, [times_perm[i-4] for i in x], label='perm')
plt.plot(x, [times_iter[i-4] for i in x], label='iter')
plt.show()
