"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях
искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства
(назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника
и годе рождения.
Выведите имена художников в порядке неубывания года рождения.
В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.

От автора решения:

Эту задачу можно решить намного намного проще.
Но моя цель - разобраться в пайтоне, а не решить задачу.
К скрипту в этом файле можно абсолютно безболезненно прикрутить
много других функций - круто же!
А еще скрипт использует ранее полученный токен, не DDOSит сервер API :)
"""

import requests
import json
import os
from datetime import datetime, timezone

PERSONAL_DATA_FILE = 'personal.txt'
TEST_DATA_FILE = '3-3-6-testdata.txt'
API_URL = 'https://api.artsy.net/api/'


def get_personal_data(file=PERSONAL_DATA_FILE):
    """
    Достает из текcтового файла идентификаторы пользователя,
    необходимые для доступа к API.
    Возвращает словарь с идентификаторами.
    """
    file_path = os.path.join(os.path.dirname(__file__), file)
    with open(file_path, 'rt') as file:
        personal_data = json.load(file)
    return personal_data


def get_new_token():
    """ Возвращает новый токен доступа к API (и записывает его в token.txt) """
    personal_data = get_personal_data()
    responce = requests.post(API_URL + "tokens/xapp_token", personal_data)
    token = responce.json()
    file_path = os.path.join(os.path.dirname(__file__), 'token.txt')
    with open(file_path, 'w+') as file:
        json.dump(token, file)
    return token


def check_token():
    """
    Возвращает валидный токен.
    Проверяет срок действия токена из файла token.txt.
    Если срок действия токена не прошел, возвращает его.
    В противном случае получает новый токен, перезаписывает файл, возвращает токен.
    """
    file_path = os.path.join(os.path.dirname(__file__), 'token.txt')
    with open(file_path, 'rt') as file:
        token = json.load(file)
        expire = datetime.fromisoformat(token['expires_at'])
        if expire > datetime.now(timezone.utc):
            # print('we use old token, its good')
            return token
        return get_new_token()


def get_from_api(object_type, object_id):
    """
    Обращается к серверу API с заданным вопросом.
    Возвращает весь ответ целиком
    """
    token = check_token()['token']
    headers = {"X-Xapp-Token": token}
    url = API_URL + object_type + "/" + object_id
    responce = requests.get(url, headers=headers)
    if responce.status_code == 200:
        result = json.loads(responce.text)
        return result
    else:
        print('Smth wrong with connection')
        return None


def find_artist(artist_id):
    """ По id художника возвращает словарик с информацией о нем"""
    artist = get_from_api('artists', artist_id)
    return artist


def get_test_data(file=TEST_DATA_FILE):
    """ Возвращает список ID художников из заданного файла. """
    test_data = []
    file_path = os.path.join(os.path.dirname(__file__), file)
    with open(file_path, 'rt') as file:
        data = file.readlines()
        for line in data:
            test_data.append(line.strip())
    return test_data


# ! Выведите имена художников в порядке неубывания года рождения.
# В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.

td = get_test_data()
artists = []
for i in td:
    artist = find_artist(i)
    artists.append((artist['sortable_name'], artist['birthday']))
artists.sort(key=lambda x: x[1])
for a in artists:
    print(a[0])
