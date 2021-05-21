'''
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано
максимальное число раз в 2015 году.
'''

import csv

with open('Crimes.csv', 'rt') as file:
    data = csv.DictReader(file)
    counter = {}
    for row in data:
        if '2015' in row['Date']:
            try:
                counter[row['Primary Type']] += 1
            except KeyError:
                counter[row['Primary Type']] = 1

    s = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print(s[0][0])
