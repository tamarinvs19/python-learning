with open('input', 'r') as f:
    line = ''
    a = f.read(1)
    while a != ' ':
        line += a
        a = f.read(1)

print(line)
