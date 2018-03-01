def time_gen_rand_list():
    import timeit

    n = 10000

    a = timeit.timeit('generation_test.one_r()', number = n, setup='import random, generation_test')
    b = timeit.timeit('generation_test.two_r()', number = n, setup='import random, generation_test')
            
    print('for =', a, 'generator =', b, 'f/g =', a/b )
    if a > b:
        print('method for' , '>','method generator')
    elif a < b:
        print('method for' , '<','method generator')
    else:
        print('method for' , '=','method generator')


