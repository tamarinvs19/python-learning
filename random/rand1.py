from random import choice
b = [[0,0,0,0,0,0,0,0,0,0] for _ in range(10)]
coord = [(i, j) for i in range(len(b)) for j in range(len(b))]

for _ in range(5):
	i, j = choice(coord)
	coord.remove((i,j))
	b[i][j] = 2
print(b)