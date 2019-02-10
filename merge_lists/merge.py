from heapq import merge
from collections import Counter

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
    return (result + list1[-1::-1] + list2[-1::-1])[-1::-1]

def counter_merge(list1, list2):
    return sorted(list(Counter(list1 + list2).elements()))

def heapq_merge(list1, list2):
    return list(merge(list1, list2))
