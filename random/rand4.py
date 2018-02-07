from random import choice
ds = {'sword' : 1, 'armor' : 1, 'potion' : 2, 'gold' : 4, 'beer' : 2}
l = []
for d in set(ds.keys()):
	for _ in range(ds[d]):
		l.append(d)
res = choice(l)
print(res)