def siftdown(i, a):
    while 2*i + 1 < len(a):
        mn = i
        if a[2*i + 1] < a[mn]:
            mn = 2 * i + 1
        if 2*i + 2 < len(a) and a[2*i + 1] < a[mn]:
            mn = 2 * i + 2
        if mn == i:
            break
        a[mn], a[i] = a[i], a[mn]
        i = mn
    return a

def add(v, a):
    a.append(v)
    i = len(a) - 1
    p = i // 2
    while i > 0 and a[p] < a[i]:
        a[i], a[p] = a[p], a[i]
        i, p = p, i // 2
    return a

def buildheap(a):

