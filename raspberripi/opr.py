xs = []
with open('opros_na_udarenia.csv', 'r') as f:
    xs = f.readlines()
for i in range(len(xs)):
    xs[i] = xs[i].strip().split()

for i in range(len(xs)):
    xs[i] = {'time': xs[i][0], 'year': xs[i][1], 'month': xs[i][2], 'obr': xs[i][3], 'ling': xs[i][4], 'ul': xs[i][5]}

with open('res.csv', 'w') as f:
    for x in xs
