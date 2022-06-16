from bs4 import BeautifulSoup
import requests
import re

req = requests.get('https://yandex.ru/')
s = req.text

s = re.findall('<a aria-label=\"([^/"]+)\" class=\"home-link2 weather__grade home-link2_color_black home-link2_hover_red\" ', s)

print(s)

# from bs4 import BeautifulSoup
#
# with open('index.html', encoding='utf-8') as f:
#     s = f.read()
# li = re.findall('<a aria-label=\"([^/"]+)\" class=\"home-link2 weather__grade home-link2_color_black home-link2_hover_red\" ', s)
#
# print(li)

