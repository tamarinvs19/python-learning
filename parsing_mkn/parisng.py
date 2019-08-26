import requests
from bs4 import BeautifulSoup


url_maad = 'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_85a72c55-0204-40ca-8d50-5daa1a4f0f50.html'
url_list = 'https://cabinet.spbu.ru/Lists/1k_EntryLists/index_comp_groups.html'

def parsing(url):
    payload = {}
    resp = requests.get(url)
    if resp.status_code == 200:
        # return resp.content.decode('utf-8')
        soup = BeautifulSoup(resp.content.decode('utf-8'))
        return soup
    else:
        return False

def del_tags(x):
    res = ''
    tag = False
    for i in range(len(x)):
        if x[i] == '<':
            tag = True
        if not tag:
            res += x[i]
        if x[i] == '>':
            tag = False
    return res


def html_to_list(html):
    html = str(html)
    list_abit = [del_tags(line[4:-5]) for line in html.split('\n')[1:-1]]
    return list_abit

def get_spbu(url):
    soup = parsing(url)
    abits = soup.findAll('tr')
    abits = [html_to_list(abit) for abit in abits]
    print(abits[1])


get_spbu(url_maad)
