class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return True if pos >= neg else False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция ()
        return True if (pos >= 1) else False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return True if neg == 0 else False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = [f for f in funcs]
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            pos, neg = 0, 0
            for f in self.funcs:
                if f(i) is True:
                    pos +=1
                else:
                    neg += 1
            if self.judge(pos, neg) is True:
                yield i
            else:
                continue


def f2(x):
     return x % 2 == 0 # возвращает True, если x делится на 2

def f3(x):
    return x % 3 == 0

a = [1, 2, 3]

[print(i) for i in multifilter(a, f2, f3)]
