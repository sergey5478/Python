# 1. Задайте список, состоящий из произвольных чисел, количество
# задаёт пользователь. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in 5     out   [10, 2, 3, 8, 9]    22
from random import randint

def My_list(amount):
    my_list = []
    for k in range(amount):
        my_list.append(randint(0, 10))
        print (my_list)
    return my_list

f = My_list(int(input()))
print(f)

def SumNumbers(f):
    Summa = 0
    for i in range(len(f)):
        if i % 2 == 0:
            Summa = Summa+f[i]
    return Summa
print(SumNumbers(f))


