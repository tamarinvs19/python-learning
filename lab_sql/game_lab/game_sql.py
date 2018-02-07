import sqlite3
from csv import reader
from random import randint
def make_levels():
	LEVEL = 'INSERT INTO level VALUES(?);'
	levels = ['one', 'two', 'three', 'four']
	with sqlite3.connect('game.db') as game:
		game.execute('CREATE TABLE IF NOT EXISTS level (name TEXT);')
		for level in levels:
			game.execute(LEVEL, [level])
		game.commit()
		
def make_atoms(atoms):
	ATOM = 'INSERT INTO atom VALUES (?, ?, ?);'
	CREATE_ATOMS = 'CREATE TABLE IF NOT EXISTS atom (x INTEGER, y INTEGER, level INTEGER);'
	with sqlite3.connect('game.db') as game:
		game.execute(CREATE_ATOMS)
		for atom in atoms:
			#print(ATOM.format(*atom))
			game.execute(ATOM, atom)
		game.commit()
def make_atom_list():
	global n
	atoms = []
	dictionary_level = {0:'one', 1:'two', 2:'three', 3:'four'}
	with open('points.csv') as f:
		r = reader(f)
		next(r)
		for row in r:
			row[2] = abs(int(row[2])) % 4
			atoms.append(row[:3])
	return atoms[:n]
	
def make_connections():
	global n
	connections =[]
	CONNECTION = 'INSERT INTO connection VALUES (?, ?, ?);'
	CREATE_CONNECTIONS = 'CREATE TABLE IF NOT EXISTS connection (a1 INTEGER, a2 INTEGER, level INTEGER);'
	for i in range(4*n):
		connect = (randint(1,n), randint(1,n),randint(1, 5))
		while connect in connections:
			connect = (randint(1,n), randint(1,n), randint(1, 5))
		connections.append(connect)
	with sqlite3.connect('game.db') as game:
		game.execute(CREATE_CONNECTIONS)
		for connect in connections:
			game.execute(CONNECTION, connect)
		game.commit()
		
def open_level(level):
	ATOM = 'SELECT ROWID, x, y FROM atom WHERE level = ?;'
	CONNECT = 'SELECT a1, a2 FROM connection WHERE a1 IN(SELECT ROWID, x, y FROM atom WHERE level = ?;) AND a2 IN(?);'
	with sqlite3.connect('game.db') as game:
		atoms =[]
		id_atoms = set()
		connections = []
		atoms = game.execute(ATOM, [level]).fetchall()
		for atom in atoms:
			id_atoms.union({atom[0]})
		#print(atoms)
		id_atoms = tuple(id_atoms)
		connections = game.execute(CONNECT, [id_atoms, id_atoms])
	return level ,connections
global n
n = 100
#make_levels()
#make_atoms(make_atom_list())
#make_connections()
print(open_level(0))