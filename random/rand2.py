from random import random
ds = {'sword' : 0.1, 'armor' : 0.1, 'potion' : 0.2, 'gold' : 0.4, 'beer' : 0.2}
l = []
for key in set(ds.keys()):
	r = random()
	if r <= ds[key]:
		l.append(key)
print(l)