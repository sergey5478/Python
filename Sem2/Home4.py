# 4. Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5  -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]   -> 15
numberA = int(input())
numberB = int(input())
n = int(input())
list = []
for i in range (-n,n+1):
    list.append (i)
sum = list[numberA-1] * list[numberB-1]
print(f"При n = {n} получаем список {list} Произведение элементов {numberA} и {numberB} = {sum}")