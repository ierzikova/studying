"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B,
т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами
внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C,
что из A в C можно перейти за один переход и из C в B можно перейти
за один переход.

Вашей программе на вход подаются две строки, содержащие url
двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода,
иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа
могут вести на существующие HTML документы.
"""

import requests
import re
from bs4 import BeautifulSoup


def two_handshakes(url1, url2):
    """ проверяет можно ли за два клика попасть с одной страницы на другую"""
    response = requests.get(url1)
    if response.status_code != 200 or url2 in response.text:
        return False
    soup = BeautifulSoup(response.text, features="html.parser")
    links = []
    for a in soup.find_all('a'):
        link = a.get('href')
        links.append(link)
    for link in links:
        response = requests.get(link)
        if url2 in response.text:
            return True
        return False


#samples:
s1 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
s2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'



# test. Should be 'Yes'
answer = two_handshakes(s1, s2)
if answer:
    print('Yes')
else:
    print('No')
