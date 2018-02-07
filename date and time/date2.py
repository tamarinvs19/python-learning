from datetime import *
d = date(2018, 1, 24) + timedelta(180)
print(d.strftime('%d %B %Y'))