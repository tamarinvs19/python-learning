from sys import stdin


line = ''
a = stdin.read(1)
while a != ' ':
    line += a
    a = stdin.read(1)
