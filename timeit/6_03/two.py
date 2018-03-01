import timeit
n = 10
def test():
    a = timeit.timeit('one.first_while(genetation_test_fix.generate_lists(750))', number = n, setup='import genetation_test_fix, one')
    b = timeit.timeit('one.second_for(genetation_test_fix.generate_lists(750))', number = n, setup='import genetation_test_fix, one')
    c = timeit.timeit('one.third_index(genetation_test_fix.generate_lists(750))', number = n, setup='import genetation_test_fix, one')
    d = timeit.timeit('one.fourth_try_index(genetation_test_fix.generate_lists(750))', number = n, setup='import genetation_test_fix, one')
    print('while - 750', a)
    print('for - 750', b)
    print('index - 750', c)
    print('try - 750', d)
test()