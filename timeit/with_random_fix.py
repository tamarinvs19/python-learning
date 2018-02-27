def time_gen_rand_list_fix():
    import timeit
    import random
    
    n = 10**4
    random.seed(239)
    a = timeit.timeit('genetation_test_fix.one_rf()', number = n, setup='import genetation_test_fix')
    random.seed(239)
    b = timeit.timeit('genetation_test_fix.two_rf()', number = n, setup='import genetation_test_fix')
            
    print('for =', a, 'generator =', b, 'f/g =', a/b )
    if a > b:
        print('method for' , '>','method generator')
    elif a < b:
        print('method for' , '<','method generator')
    else:
        print('method for' , '=','method generator')


