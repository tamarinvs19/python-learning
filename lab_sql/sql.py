import sqlite3
from csv import reader

molecule = 'INSERT INTO molecule VALUES (?, ?, ?, ?, ?, ?);'
db = sqlite3.connect('test.db')
db.execute('CREATE TABLE IF NOT EXISTS molecule (x INTEGER, y INTEGER, z INTEGER, vx INTEGER, vy INTEGER, vz INTEGER);' )  

with open('points.csv') as f:
    r = reader(f)
    next(r)
    for row in r:
        db.execute(molecule, row)
db.commit()
db.close()
