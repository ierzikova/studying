test = open("1-6-7-classes-input.txt", "r").readlines()
n = int(test[0])
q = int(test[n + 1])

classes = dict() #словарь, в который будем класть данные в формате {класс : множество потомков}


def add_class(kid, *parents):
    """ Добавляем в наш словарь данные в формате {kid : set(parents)} """
    classes[kid] = set([parent for parent in parents])
    for parent in parents:
        if parent not in classes.keys():
            classes[parent] = {parent}
    return True


def is_parent(parent, kid, classes = classes):
    """ Проверяем является ли kid потомком parent.
    Изолируем рекурсивную функцию от глобального неймспейса."""
    def is_parent_inner(parent, kid, classes):
        """ Проверяем является ли kid потомком parent.
        Если нет, то рекурсивно проверяем является ли потомок kid потомком parent.
        В рекурсии пользуемся булевыми значениями, чтобы экономить память """
        if kid not in classes.keys():
            return False  # Выход из рекурсии, если дошли до конца ветки наследования и не нашли путь до потомка
        elif parent in classes[kid] or parent == kid:
            return True # Выход из рекурсии, если kid является потомком parent
        else:
            for preparent in classes[kid]:
                resp = is_parent_inner(parent, preparent, classes)
                if resp is not True: # Здесь с тупиковой ветки наследования возвращаемся \
                    continue         # к следующему потомку kid, чтобы проверить другую ветку наследования.
                else:
                    return resp      # Но если уже нашли путь до потомка, то выходим из рекурсии.

    if is_parent_inner(parent, kid, classes):
        return 'Yes'
    else:
        return 'No'


# n = int(input())

for i in range(1, n + 1):   # Пополняем базу
    # string = input()
    string = test[i]
    kid, *parents = [s for s in string.replace(":", " ").split()]
    add_class(kid, *parents)

# q = int(input())

for i in range(n + 2, n + 2 + q):   # Отвечаем да или нет на запросы пользователя "предок потомок"
    # string = input()
    string = test[i]
    q = [s.strip() for s in string.split()]
    if len(q)==2:
        parent, kid = q[0], q[1]
        print(is_parent(parent, kid))
    elif len(q)==1:
        print('Yes')
    else:
        print('No')

