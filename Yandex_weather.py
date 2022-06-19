from bs4 import BeautifulSoup
import requests

link = requests.get(f'https://yandex.ru/')
link_2 = requests.get(f'https://www.rbc.ru/')
content = link.text
content_2 = link_2.text
soup = BeautifulSoup(content, 'lxml')
soup_2 = BeautifulSoup(content_2, 'lxml')
w = soup.find('div', class_="weather__content").find('a').get('aria-label')
print(w)
traffic = soup.find('div', class_="traffic__rate-text").text
print('Пробки - ', traffic, 'бал')
USD = soup.find('span', class_="key-indicators__diff key-indicators__diff_fall").text
print('Пробки - ', USD, 'бал')
