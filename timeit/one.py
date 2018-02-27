import timeit
print(timeit.timeit('[x**2 for x in range(100)]', number = 5))