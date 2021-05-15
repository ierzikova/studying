import time
start_time = time.time()


def primes():
    ''' Генератор простых чисел '''
    yield 2
    prime_numbers = [2]
    i = 3
    while True:
        for n in prime_numbers:
            if i % n == 0:
                continue
        prime_numbers.append(i)
        yield i
        i+=2


# Проверка:
from itertools import takewhile
print(list(takewhile(lambda x: x <= 1000, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 ...]


print("--- %s seconds ---" % (time.time() - start_time))
#--- 0.01690530776977539 seconds ---
