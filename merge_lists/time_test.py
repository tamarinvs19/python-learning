from merge import linear_merge1, linear_merge2, heapq_merge, counter_merge
from timeit import timeit
import random


res1, res2, res3, res4 = 0, 0, 0, 0
def test_time():
    global res1, res2, res3, res4
    r1, r2 = random.randint(1, 1000), random.randint(1, 1000)
    list1 = [random.randint(1, 10000) for _ in range(r1)]
    list2 = [random.randint(1, 10000) for _ in range(r2)]
    res1 += timeit('merge(list1, list2)', number=100, globals={'merge': linear_merge1, 'list1': list1, 'list2': list2})
    res2 += timeit('merge(list1, list2)', number=100, globals={'merge': linear_merge2, 'list1': list1, 'list2': list2})
    res3 += timeit('merge(list1, list2)', number=100, globals={'merge': heapq_merge, 'list1': list1, 'list2': list2})
    res4 += timeit('merge(list1, list2)', number=100, globals={'merge': counter_merge, 'list1': list1, 'list2': list2})

def time_test():
    for _ in range(1000):
        test_time()

    print('linear_merge1', res1)
    print('linear_merge2', res2)
    print('heapq_merge  ', res3)
    print('counter_merge', res4)

time_test()
