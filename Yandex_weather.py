from bs4 import BeautifulSoup
import requests

link = requests.get(f'https://yandex.ru/')
content = link.text
soup = BeautifulSoup(content, 'html.parser')
w = soup.find('div', class_="weather__content").find('a').get('aria-label')
print(w)
USD = soup.find('div', class_="stocks__item-right")
print(USD)