""" Подключаем файл с тестом (не требуется, если код выполняется на сайте Stepik) """
test = open("2-1-6-test.txt", "r").readlines()

errors = dict()
""" Словарь, в который будем класть данные в формате {класс ошибки : множество потомков} """


def add_class(kid, *parents):

    """ Добавляем в наш словарь данные в формате {kid : set(parents)} """

    errors[kid] = set([parent for parent in parents])
    for parent in parents:
        if parent not in errors.keys():
            errors[parent] = {parent}
    return True


def is_parent(parent, kid, errors = errors):

    """ Проверяем является ли kid потомком parent.
    Изолируем рекурсивную функцию от глобального неймспейса."""

    def is_parent_inner(parent, kid, errors):

        """ Проверяем является ли kid потомком parent.
        Если нет, то рекурсивно проверяем является ли потомок kid потомком parent.
        В рекурсии пользуемся булевыми значениями, чтобы экономить память """

        if kid not in errors.keys():
            return False                # Выход из рекурсии, если дошли до конца ветки наследования и не нашли путь до потомка
        elif parent in errors[kid] or parent == kid:
            return True                 # Выход из рекурсии, если kid является потомком parent
        else:
            for preparent in errors[kid]:
                resp = is_parent_inner(parent, preparent, errors)
                if resp is not True:    # Здесь с тупиковой ветки наследования возвращаемся \
                    continue            # к следующему потомку kid, чтобы проверить другую ветку наследования.
                else:
                    return resp         # Но если уже нашли путь до потомка, то выходим из рекурсии.

    return is_parent_inner(parent, kid, errors)


n = int(test[0])                        # Либо n = int(input()), если на Степике


''' Пополняем базу: '''

for i in range(1, n + 1):

    string = test[i]                    # Либо string = input(), если на Степике
    kid, *parents = [s for s in string.replace(":", " ").split()]
    add_class(kid, *parents)


'''Собираем список исключенных ошибок:'''

# Для выполнения кода на сайте Степика:
# q = int(input())
# used = [input().strip() for i in range(q)]   # Собираем список исключенных ошибок

# Для выполнения кода в интерпретаторе (файл 2-1-6-test.txt должен лежать в той же папке)
q = int(test[n + 1])
used = [test[i].strip() for i in range(n + 2, n + 2 + q)]


'''Для каждой ошибки проверяем: если ранее использовали ее потомка, то выводим ошибку в консоль'''

for er in used:
    for parent in used[:used.index(er)]:
        if is_parent(parent, er):
            print(er)
            break
        else:
            continue

