import time
start_time = time.time()


def primes():
    ''' Генератор простых чисел по теореме Вильсона '''
    n, factorial = 2, 1
    while True:
        if (factorial + 1) % n == 0:
            yield n
        factorial, n = factorial * n, n + 1


# Проверка:
from itertools import takewhile
print(list(takewhile(lambda x: x <= 1000, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 ...]


print("--- %s seconds ---" % (time.time() - start_time))
#--- 0.005995750427246094 seconds ---
