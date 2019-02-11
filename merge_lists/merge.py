from heapq import merge
from collections import Counter


def linear_merge0(list1, list2):
    i, j = 0, 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res += list1[i:] + list2[j:]
    return res

def linear_merge1(list1, list2):
    result, list1, list2 = [], list1[:], list2[:]
    while list1 and list2:
        result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))
    return (result + list1[-1::-1] + list2[-1::-1])[-1::-1]

def iter_merge0(list1, list2):
    result, list1, list2 = [], iter(list1), iter(list2)
    x = next(list1, None)
    y = next(list2, None)
    while x is not None and y is not None:
        if x>y:
            result.append(y)
            y = next(list2, None)
        else:
            result.append(x)
            x = next(list1, None)
    if x is None:
        result += [y] + list(list2)
    else:
        result += [x] + list(list1)
    return result

def iter_merge1(ia, ib):
    ia, ib = iter(ia), iter(ib)
    a = next(ia, None)
    b = next(ib, None)
    while a is not None or b is not None:
        if b is None or (a is not None and a < b):
            yield a
            a = next(ia, None)
        else:
            yield b
            b = next(ib, None)

def counter_merge(list1, list2):
    return sorted(list(Counter(list1 + list2).elements()))

def heapq_merge(list1, list2):
    return list(merge(list1, list2))

def simple_merge(list1, list2):
    return sorted(list1 + list2)
