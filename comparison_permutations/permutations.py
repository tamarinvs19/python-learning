'''
======================================================
Код из статьи с HABR: https://habr.com/ru/post/276937/
'''
import math

def perms(elm, cells):
    res = []	
    arrang = math.factorial(elm) // math.factorial(elm-cells)	# расчёт к-ва сочетаний
    for i in range(arrang):
        res.append([])
        source = list(range(elm))	# массив ещё не задействованных элементов
        for j in range(cells):
            p = i // math.factorial(cells-1-j) % len(source)
            res[len(res)-1].append(source[p])
            source.pop(p)
    return res

'''
======================================================
'''

import itertools

def iter_perms(elm, cells):
    return list(itertools.permutations(range(elm), cells))

