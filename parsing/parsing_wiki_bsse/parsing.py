import requests
from bs4 import BeautifulSoup
from pprint import pprint


url_wiki = "https://bsse.compscicenter.ru/wiki/index.php?title=С%2B%2B_1MIT_осень_1_2019"

def get_data():
    resp = requests.get(url_wiki)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content.decode('utf-8'), "lxml")
        return soup
    else:
        return None

def parsing():
    soup = get_data()
    if soup:
        lectures = soup.findAll('ul')[3]
        links = [[str(a).split('href=')[1].split('"')[1] for a in lect.children if 'href' in str(a)][0] for lect in lectures.children if lect.name == 'li']
        for i, link in enumerate(links, 14):
            resp = requests.get(link)
            if resp.status_code == 200:
                with open(f'Lect_{i}.pdf', 'wb') as f:
                    f.write(resp.content)

if __name__ == '__main__':
    parsing()
