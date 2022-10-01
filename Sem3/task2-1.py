# 2. Задайте список, состоящий из произвольных слов, количество
# задаёт пользователь. Напишите программу, которая определит
# индекс второго вхождения строки в списке либо сообщит, что её нет.
from random import choices


def Name(a, b):
    name = []
    for t in range(a):
        y = choices(b, k=3)
        name.append("".join(y))
    return name


f = Name(10, "abc")
print(f)


def Find(m, o: list):
    if o.count(m) > 1:
        p = o.index(m)
        print(o.index(m, p+1))
    else:
        print(-1)


Find(input(), f)
