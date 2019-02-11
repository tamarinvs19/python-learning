import random
def linear_merge2(l1, l2):
    result, list1, list2 = [], iter(l1), iter(l2)
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

def test_correctness():
    list1 = [1,2,3,4]
    list2 = [3,4,5,6]
    assert sorted(list1+list2) == linear_merge2(list1, list2)

def time_test():
    r1, r2 = random.randint(1, 1000), random.randint(1, 1000)
    list1 = sorted([random.randint(1, 10000) for _ in range(r1)])
    list2 = sorted([random.randint(1, 10000) for _ in range(r2)])
    print(linear_merge2(list1, list2))
