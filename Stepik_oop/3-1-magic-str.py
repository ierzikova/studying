"""
    Создайте класс Person, у которого есть:

        конструктор __init__, принимающий 3 аргумента: name, surname, gender.
        Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male".
        Если в атрибут gender передается любое другое значение, печатать сообщение:
        "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
        переопределить метод __str__ следующим образом:
            если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
            если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
"""
class Person:
    GENDERS = {
        'male' : 'M',
        'female' : 'F'
    }  #there are many different people in the world

    def __init__(self, name:str, surname:str, gender:str='male'):
        self.name = name
        self.surname = surname
        if gender not in Person.GENDERS:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            gender = 'male'
        self.gender = Person.GENDERS[gender]

    def __str__(self):
        prefix = 'Гражданка' if self.gender == 'M' else 'Гражданин'
        return f"{prefix} {self.surname} {self.name}"

# Тестовый код из задачи:
p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
