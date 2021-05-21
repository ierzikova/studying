"""
В этой задаче вам необходимо воспользоваться API сайта
numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать,
существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует
интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке,
в каком следуют числа во входном файле.
"""
import requests
import os

API_URL = f'http://numbersapi.com/'


def get_fact(number='random', api_url=API_URL):
    '''
    Отправляет API запрос с заданным number
    Возвращаает словарь с информацией о number
    '''
    params = {
        'json': True
        }
    url = api_url + number + '/math/'
    res = requests.get(url, params)
    if res.status_code == 200:
        return res.json()
    return "Smth wrong with API..."


def is_interesting(number):
    '''
    По заданному number возвращает 'Interesting,
    если о числе есть интересные факты,
    'Boring' в остальных случаях
    '''
    info = get_fact(number)
    return 'Interesting' if info['found'] else 'Boring'


test_path = (os.path.join(os.path.dirname(__file__), '3-3-5-testcase.txt'))
with open(test_path) as file:
    data = file.readlines()
    for line in data:
        number = line.strip()
        print(is_interesting(number))
