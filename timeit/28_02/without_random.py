def test_time_list():
    import timeit
    import random
    n = 1000

    a = timeit.timeit('generation_test.one()', number = n, setup='import generation_test')
    b = timeit.timeit('generation_test.two()', number = n, setup='import generation_test')
            
    print('for =', a, 'generator =', b, 'f/g =', a/b )
    if a > b:
        print('method for' , '>','method generator')
    elif a < b:
        print('method for' , '<','method generator')
    else:
        print('method for' , '=','method generator')


