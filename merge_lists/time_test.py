from merge import linear_merge0, linear_merge1, linear_merge2, iter_merge0, iter_merge1, heapq_merge, counter_merge, simple_merge

from timeit import timeit
import random
from copy import copy


res0, res1, res2, res3, res4, res5, res6, res7 = [0] * 8
def test_time():
    global res0, res1, res2, res3, res4, res5, res6, res7
    r1, r2 = random.randint(1, 1000), random.randint(1, 1000)
    list1 = sorted([random.randint(1, 10000) for _ in range(r1)])
    list2 = sorted([random.randint(1, 10000) for _ in range(r2)])
    res2 += timeit('merge(list1, list2)', number=100, globals={'merge': iter_merge0, 'list1': list1, 'list2': list2})
    res3 += timeit('merge(list1, list2)', number=100, globals={'merge': iter_merge1, 'list1': list1, 'list2': list2})
    res4 += timeit('merge(list1, list2)', number=100, globals={'merge': heapq_merge, 'list1': list1, 'list2': list2})
    res5 += timeit('merge(list1, list2)', number=100, globals={'merge': counter_merge, 'list1': list1, 'list2': list2})
    res6 += timeit('merge(list1, list2)', number=100, globals={'merge': simple_merge, 'list1': list1, 'list2': list2})
    res0 += timeit('merge(list1, list2)', number=100, globals={'merge': linear_merge0, 'list1': list1, 'list2': list2})
    res1 += timeit('merge(list1, list2)', number=100, globals={'merge': linear_merge1, 'list1': copy(list1), 'list2': copy(list2)})
    res7 += timeit('merge(list1, list2)', number=100, globals={'merge': linear_merge2, 'list1': copy(list1), 'list2': copy(list2)})

def time_test():
    for _ in range(1000):
        test_time()

    print('linear_merge0', res0)
    print('linear_merge1', res1)
    print('linear_merge2', res7)
    print('iter_merge0  ', res2)
    print('iter_merge1  ', res3)
    print('heapq_merge  ', res4)
    print('counter_merge', res5)
    print('simple_merge ', res6)

time_test()
