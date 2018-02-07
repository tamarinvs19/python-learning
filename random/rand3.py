def next_step(last):
	r = (6364136223846793005 * last + 1442695040888963407) % (2^64 +239)
	return r
from random import randint
r = randint(1, 4)
for _ in range(100):
	r = next_step(r)
	print(r)