try:
    fin = open('res', 'w')
    for number in range(27*10**4+2346, 10**7):
        series = '4015'
        number = '0'*(6-len(str(number))) + str(number)
        res = get_result(parsing(series, number))
        if res != ('',''):
            fin.write(number+','+ str(res))
            print(number, res)
finally:
        fin.close()
