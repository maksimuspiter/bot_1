import requests
from bs4 import BeautifulSoup

url = 'http://www.RzhuNeMogu.ru/Widzh/WidzhRNM.aspx?type=1&callback=onSuccess'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
# quote = soup.find('p')
soup = str(soup)
print(soup.index('"result":'))

new = soup[(soup.index('{"result":') + 11): (soup.index('</p><p><a'))]
print(new)
print('--------------------------------')
print(soup)

print('--------------------------------')

while '<br>' in new:
    new = new.replace('<br>', '')
    new = new.replace('<br/>', '')
    print(new)