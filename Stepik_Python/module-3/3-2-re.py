'''
3-2-7
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
'''

import sys
import re

for line in sys.stdin:
    template = 'cat.*cat'
    if re.search(template, line) is not None:
        print(line.strip())


'''
3-2-8
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

'''
# import sys
# import re

for line in sys.stdin:
    line = line.rstrip()
    template = r'\bcat\b'
    if re.search(template, line) is not None:
        print(line)



'''
3-2-9
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми
ровно три символа.
'''
# import sys
# import re

for line in sys.stdin:
    template = r'z.{3}z'
    if re.search(template, line) is not None:
        print(line.strip())

'''
3-2-10
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
'''
# import sys
# import re

for line in sys.stdin:
    template = r'\\'
    if re.search(template, line) is not None:
        print(line.strip())


'''
3-2-11
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
'''
# import sys
# import re

for line in sys.stdin:
    template = r'\\'
    if re.search(template, line) is not None:
        print(line.strip())


'''
3-2-12
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух 
одинаковых частей (тандемный повтор).
'''
# import sys
# import re

for line in sys.stdin:
    template = r'\b(\w+)\1\b'
    if re.search(template, line) is not None:
        print(line.strip())


'''
3-2-13
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" 
на подстроку "computer" и выведите полученные строки.
'''
# import sys
# import re

for line in sys.stdin:
    template = r'human'
    new = r'computer'
    new_line = re.sub(template, new, line)
    print(new_line.strip())


'''
3-2-14
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, 
состоящего только из латинских букв "a" (регистр не важен),
на слово "argh".
'''
# import sys
# import re

for line in sys.stdin:
    template = r'\b[aA]+\b'
    new = r'argh'
    new_line = re.sub(template, new, line, count=1)
    print(new_line.strip())


'''
3-2-15
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове,
состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
'''
# import sys
# import re

for line in sys.stdin:
    template = r'\b(\w)(\w)'
    new = r'\2\1'
    new_line = re.sub(template, new, line)
    print(new_line.strip())


'''
3-2-16
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв
на одну букву.
Буквой считается символ из группы \w.
'''
# import sys
# import re

for line in sys.stdin:
    template = r'(\w){2}+'
    new = r'\1'
    new_line = re.sub(template, new, line)
    print(new_line.strip())
