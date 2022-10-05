# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (от 0 до 10) многочлена, записать в файл 
# полученный многочлен не менее 3-х раз.
# in 9 5 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
from random import randint, choice

def Array(number):
    array = []
    for i in range(number + 1):
        array.append(randint(0, 9))
    return array

def Get_resalt(arr, number):
    items = ['+', '-']
    with open('Привет', 'a', encoding='utf-8') as my_file:
        for i in arr:
            if i > 0 and number > 0:
                my_file.write(f' {i}*x^{number} ')
                my_file.write(choice(items))
                number -= 1
        if arr[len(arr)-1] != 0:
            my_file.write(f" {arr[len(arr)-1]} = 0 \n")
            my_file.close()

for i in range(3):
    number = int(input('Введите число: '))
    if number > 0:
        Get_resalt(Array(number), number)