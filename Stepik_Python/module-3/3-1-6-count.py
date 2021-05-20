'''
Вашей программе на вход подаются две строки s и t, состоящие
из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
<aba>baba
ab<aba>ba
abab<aba>
'''

def function(string,substring):
    count = 0
    i = string.find(substring)
    while 0 <= i <= len(string):
        count +=1
        i = string.find(substring, i+1)
    return count


string = "abababa"
substring = "aba"

print(function(string,substring))
