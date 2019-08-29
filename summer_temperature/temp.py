import csv
import datetime
import pprint
import matplotlib.pyplot as plt

def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out



def format_date(s):
    return datetime.datetime.strptime(s, '%Y.%m.%d %H:%M:%S')

def read_file():
    with open('temp.csv', 'r') as f:
        cin = csv.reader(f)
        data = [(format_date(day[0]), int(day[1].split('.')[0]) +
            10**(-len(day[1].split('.')[1])) * int(day[1].split('.')[1])) for day in cin]
        # pprint.pprint(data[10000:10100])
        return data


data = read_file()[10000:10010]

data1, data2 = [str(d[0]) for d in data], [d[1] for d in data]
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
plt.show()
