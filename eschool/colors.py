key_coefs = {'style="background-color: rgba(56, 112, 30': 1.0, 'style="background-color: rgba(229, 122, 122': 0.5, 'style="background-color: rgba(3, 91, 1': 2.0, 'style="background-color: rgba(7, 111, 197': 1.0, 'style="background-color: rgba(255, 247, 119': 1.75, 'style="background-color: rgba(229, 122, 220': 0.75, 'style="background-color: rgba(156, 229, 122': 1.0, 'style="background-color: rgba(104, 218, 169': 1.0, 'style="background-color: rgba(0, 154, 69': 1.0, 'style="background-color: rgba(211, 8, 150': 1.75, 'style="background-color: rgba(255, 182, 119': 2.5, 'style="background-color: rgba(118, 0, 2': 1.3, 'style="background-color: rgba(177, 237, 0': 1.0, 'style="background-color: rgba(239, 111, 229': 1.0, 'style="background-color: rgba(104, 255, 235': 1.25, 'style="background-color: rgba(3, 7, 252': 2.0, 'style="background-color: rgba(218, 8, 99': 1.25, 'style="background-color: rgba(255, 223, 119': 1.25, 'style="background-color: rgba(102, 0, 125': 2.0, 'style="background-color: rgba(235, 47, 0': 1.5, 'style="background-color: rgba(119, 255, 119': 1.0, 'style="background-color: rgba(130, 255, 119': 1.0}
with open('colors.html', 'r') as f:
    xs = f.readlines()
xs = [(x.strip('\n'), 1) for x in xs if x != '\n']
xs = dict(xs)
ys = key_coefs
#print(xs)
for x in xs.keys():
    print(x)
    print('style="background-color: rgba' + x.split(';')[0][:-1])
    if 'style="background-color: rgba' + x.split(';')[0][:-1] not in key_coefs.keys():
        ys['style="background-color: rgba' + str(x.split(";")[0][:-1])] = float(input())

with open('types', 'w') as f:
    f.write(str(ys))
