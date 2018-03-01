import timeit
n = 100000
setup0 = 'import genetation_test_fix, one; xs = genetation_test_fix.generate_lists({})'
def test(count):
    setup1 = setup0.format(count)
    a = timeit.timeit('one.first_while(xs)',
                      number = n, setup=setup1)
    b = timeit.timeit('one.second_for(xs)',
                      number = n, setup=setup1)
    c = timeit.timeit('one.third_index(xs)',
                      number = n, setup=setup1)
    d = timeit.timeit('one.fourth_try_index(xs)',
                      number = n, setup=setup1 )
    print(count)
    print('while :', a)
    print('for :', b)
    print('index :', c)
    print('try :', d)
test(750)
test(500)
test(250)
