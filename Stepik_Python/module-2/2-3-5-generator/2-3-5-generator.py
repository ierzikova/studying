import time
start_time = time.time()


def is_prime(n):
    ''' Возвращает True, если число простое '''
    d = 2
    while n % d != 0 and d**2 <= n:
        d+=1
    return d**2 > n


def primes():
    ''' Генератор простых чисел '''
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Проверка:
from itertools import takewhile
print(list(takewhile(lambda x: x <= 1000, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 ...]


print("--- %s seconds ---" % (time.time() - start_time))
#--- 0.004685640335083008 seconds ---
