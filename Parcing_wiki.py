import re

import requests
from bs4 import BeautifulSoup

search_req = input('Введите запрос: ')
search_req = search_req.lower()
search_req = search_req.title()
def get_link(search_req):
    link = requests.get(f'https://ru.wikipedia.org/wiki/{search_req}')
    content = link.text
    return content
get_link(search_req)

soup = BeautifulSoup(get_link(search_req), 'lxml')

links = []
links_2 = []
for link in soup.find_all('a', href=True):
    link = link['href']
    if link[:4] == 'http':
        print(link)
        links.append(link)
print(links)