'''
Задание:

Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
'''


with open('test_origin.txt', 'r') as r, open('test_copy.txt', 'w') as w:
    lst = [line for line in r]
    for line in lst[::-1]:
        w.write(line)

