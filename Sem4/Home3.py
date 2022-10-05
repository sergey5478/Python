# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2] [5, 1, 2]
from random import randint

number = int(input("Задайте последовательность чисел: "))

def Array(number):
    array = []
    for i in range(number):
        array.append(randint(0, 9))
    return array

def Elements(arr):
    result = []
    for i in arr:
        if arr.count(i) == 1:
            result.append(i)
    return result

if number > 0:
    arr = Array(number)
    print(arr)
    print(Elements(arr))
else:
    print('Вы ввели некорректное значение элементов')