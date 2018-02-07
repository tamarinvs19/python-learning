import sqlite3

db = sqlite3.connect('test.db')
c = db.cursor()
points =[]
for m in c.execute('SELECT x, y, z FROM molecule WHERE (x*x+y*y+z*z) <= 25;' ):
	points.append(m)
db.close()

print(points)

with open('result.txt', 'w') as f:
	for i in range(len(points)):
		print(points[i], file=f)

