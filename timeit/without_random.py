
import timeit
import random
n = 200
res = {'a': 0, 'b': 1}
for i in range(99):
	a = timeit.timeit('generation_test.one()', number = n, setup='import random, generation_test')
	b = timeit.timeit('generation_test.two()', number = n, setup='import random, generation_test')
	if a >= b:
		res['a'] += 1
	else:
		res['b'] += 1

print('for =', res['a'], 'generator =',res['b'])
print('for >= generator', a>=b)

