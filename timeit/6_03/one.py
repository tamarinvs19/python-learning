def first_while(xs):
    #print(len(xs))
    i = 0
    while i < len(xs) and xs[i] != 1:
        i += 1 
        #print(i)
    if i <= len(xs):
        res = i
    else:
        res = None
    return res
def second_for(xs):
    res = None
    for i, x in enumerate(xs):
        if x == 1:
            res = i
            break
    return res
def third_index(xs):
    if 1 in xs:
        res = xs.index(1)
    else:
        res = None
    return res
def fourth_try_index(xs):
    try:
        res = xs.index(1)
    except:
        res = None
    return res