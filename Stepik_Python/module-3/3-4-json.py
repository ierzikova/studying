"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов,
которые соответствуют классам. У каждого JSON-объекта есть поле name,
которое содержит имя класса, и поле parents, которое содержит список
имен прямых предков.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, \
{"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2
"""

import json


def get_test_data():
    """ Достает тестовые данные из json. Возвращает список словарей. """
    # raw = input()
    raw = '[' \
          '{"name": "A", "parents": []},' \
          '{"name": "B", "parents": ["A", "C"]}, ' \
          '{"name": "C", "parents": ["A"]}' \
          ']'
    data = json.loads(raw)
    return (data)


def get_parents(kid, data):
    """ Для заданного потомка возвращает список предков """
    for item in data:
        if item["name"] == kid:
            return item["parents"]
    return []


def walk(start, finish, data):
    """
    Ищет путь от потомка до предка. Возвращает True,
    если предок и потомок связаны, False - иначе
    """
    for p in get_parents(start, data):
        if p == finish:
            return True
        else:
            part = walk(p, finish, data)
            if part:
                return part
    return False


def main():
    """
    Для каждого потомка считает количество предков
    (в том числе прадедушек :))
    """
    data = get_test_data()
    result = {}
    for i in data:
        result[i["name"]] = 1
    for k1 in result.keys():
        for k2 in result.keys():
            if k1!=k2 and walk(k1, k2, data):
                result[k2] +=1
    for key in sorted(result):
        print(f'{key} : {result[key]}')

main()
