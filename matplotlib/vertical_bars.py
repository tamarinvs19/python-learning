import matplotlib.pyplot as plt
from itertools import product


all_colors = list(plt.cm.colors.cnames.keys())

front_gears = {
    'centurion': [28, 34, 42],
    'merida 500': [26, 36],
    'merida 400': [32],
    }
rear_gears = {
    'centurion': [14, 16, 18, 20, 22, 25, 28],
    'merida 500': [11, 13, 15, 17, 19, 21, 24, 28, 32, 37, 42],
    'merida 400': [11, 13, 15, 18, 21, 24, 28, 33, 39, 45, 51],
    }

df = {
    name: sorted(
        (
            front / rear,
            len(front_gears[name]) - front_gears[name].index(front),
            len(rear_gears[name]) - 1 - rear_gears[name].index(rear),
            )
        for front, rear in product(front_gears[name], rear_gears[name])
        )
    for name in front_gears.keys()
    }

print(df)

plt.figure(figsize=(35, 10), dpi=80)
plt.bar(
    range(21),
    [x[0] for x in df['centurion']],
    color=[['skyblue', 'cyan', 'steelblue'][x[1]-1] for x in df['centurion']],
    width=0.5,
    )
plt.bar(
    range(21, 22+21),
    [x[0] for x in df['merida 500']],
    color=[['red', 'darkred'][x[1]-1] for x in df['merida 500']],
    width=0.5,
    )
plt.bar(
    range(22+21, 11+22+21),
    [x[0] for x in df['merida 400']],
    color=['forestgreen'],
    width=0.5,
    )
plt.hlines(1, -1, 55, color='gray', linewidth=1, linestyle=':')
plt.hlines(1.5, -1, 55, color='gray', linewidth=1, linestyle=':')
plt.hlines(2, -1, 55, color='gray', linewidth=1, linestyle=':')
plt.hlines(2.5, -1, 55, color='gray', linewidth=1, linestyle=':')
plt.hlines(3, -1, 55, color='gray', linewidth=1, linestyle=':')

# Decoration
gears = [x[2]+1 for values in df.values() for x in values]
for i, val in enumerate(gears):
    plt.text(
        i, 0, val,
        horizontalalignment='center',
        verticalalignment='bottom',
        fontdict={'fontweight': 500, 'size': 10},
        )
plt.title('Gear ration', fontsize=22)
plt.ylabel('Value')
plt.ylim(0, 4)
plt.show()

