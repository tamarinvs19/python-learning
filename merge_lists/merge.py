from heapq import merge
from collections import Counter
from timeit import timeit
import random

def linear_merge1(list1, list2):
    result, list1, list2 = [], list1[:], list2[:]
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    return result + list1 + list2

def linear_merge2(list1, list2):
    result, list1, list2 = [], list1[:], list2[:]
    while list1 and list2:
        result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))
    return (result + list1 + list2)[-1::-1]

def counter_merge(list1, list2):
    return sorted(list(Counter(list1 + list2).elements()))

def heapq_merge(list1, list2):
    return list(merge(list1, list2))

# random.seed(7)
res1, res2, res3, res4 = 0, 0, 0, 0
def test_time():
    global res1, res2, res3, res4
    r = random.randint(1, 1000)
    list1 = [random.randint(1, 10000) for _ in range(r)]
    list2 = [random.randint(1, 10000) for _ in range(r)]
    res1 += timeit('merge(list1, list2)', number=1, globals={'merge': linear_merge1, 'list1': list1, 'list2': list2})
    res2 += timeit('merge(list1, list2)', number=1, globals={'merge': linear_merge2, 'list1': list1, 'list2': list2})
    res3 += timeit('merge(list1, list2)', number=1, globals={'merge': heapq_merge, 'list1': list1, 'list2': list2})
    res4 += timeit('merge(list1, list2)', number=1, globals={'merge': counter_merge, 'list1': list1, 'list2': list2})

for _ in range(10000):
    test_time()

print('linear_merge1', res1)
print('linear_merge2', res2)
print('heapq_merge  ', res3)
print('counter_merge', res4)
