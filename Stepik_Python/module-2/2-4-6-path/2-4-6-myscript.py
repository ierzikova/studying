'''
Вам дана в файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной
файловой структуре все директории, в которых есть хотя бы один файл
с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий,
отсортированных в лексикографическом порядке.
'''

import os

path = os.walk('main')

for dirpath, dirname, filenames in sorted(path):
    for filename in filenames:
        if '.py' in filename:
            print(dirpath)
            break

