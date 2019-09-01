import csv
import datetime
import pprint
import matplotlib.pyplot as plt

def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

def format_date(s):
    assert(type(s) == str)
    return datetime.datetime.strptime(s, '%Y.%m.%d %H:%M:%S')

def read_file():
    with open('temp.csv', 'r') as f:
        cin = csv.reader(f)
        new_data = []
        for temp in cin:
            time = format_date(temp[0])
            temp_data = int(temp[1].split('.')[0]) + 10**(-len(temp[1].split('.')[1])) * int(temp[1].split('.')[1])
            if not(datetime.time(8, 0, 0) <= time.time() <= datetime.time(13, 30, 0)) and temp_data < 40:
                new_data.append((time, temp_data))

        # pprint.pprint(data[10000:10100])
        return new_data

def draw(data):
    data1, data2 = [d[0].strftime('%d.%m %H:%M') for d in data], [d[1] for d in data]
    fig, ax = plt.subplots(1, 1)
    my_plotter(ax, data1, data2, {'marker': '.'})
    plt.show()

def average_in_time_of_day(temps):
    if len(temps) != 0:
        return round(sum(temps) / len(temps), 3)
    else:
        return None

def format_to_time_of_day(day):
    temps = {'morning': [], 'daytime': [], 'evening': []}
    for time, temp in day:
        if datetime.time(6, 0, 0) <= time.time() <= datetime.time(8, 0, 0) and temp < 40:
            temps['morning'].append(temp)
        elif datetime.time(13, 30, 0) <= time.time() <= datetime.time(15, 30, 0) and temp < 40:
            temps['daytime'].append(temp)
        elif datetime.time(17, 30, 0) <= time.time() <= datetime.time(22, 30, 0) and temp < 40:
            temps['evening'].append(temp)

    # print(temps)
    temps = {
        'morning': average_in_time_of_day(temps['morning']),
        'daytime': (lambda x: None if len(x) == 0 else round((max(x) + average_in_time_of_day(x))/2, 3))(temps['daytime']),
        'evening': average_in_time_of_day(temps['evening']),
    }

    return temps

def format_to_days(data):
    days = {}
    now = 0
    current_temps = []
    for d, t in data:
        if now != d.date():
            days[now] = current_temps
            current_temps = []
            now = d.date()
        current_temps.append((d, t))
    days[now] = current_temps

    return days

def average_temps(days):
    average = {}
    for day in days.keys():
        average[day] = format_to_time_of_day(days[day])

    return average

def write_to_file(res):
    with open('average_temp_3.csv', 'w') as fout:
        cout = csv.DictWriter(fout, ['date', 'morning', 'daytime', 'evening'])
        cout.writeheader()
        pprint.pprint(res)
        cout.writerows(res)

def update(key, others):
    others.update({'date':key.strftime('%d.%m.%Y')})
    return others

def main():
    # data = read_file()
    data = read_file()
    # pprint.pprint(data)
    days = format_to_days(data)
    # pprint.pprint(days)
    res = [update(key, average_temps(days)[key]) for key in days.keys() if key != 0]
    write_to_file(res)


if __name__ == '__main__':
    main()


