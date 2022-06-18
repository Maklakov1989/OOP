from bs4 import BeautifulSoup
import requests

link = requests.get(f'https://yandex.ru/')
content = link.text
soup = BeautifulSoup(content, 'html.parser')
a = soup.find('div', class_="widget__content weather__content-outer").find('a').get('aria-label')
print(a)

