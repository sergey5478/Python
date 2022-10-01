# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4 out [2, 5, 8, 10] [20, 40] in 5 out [2, 2, 4, 8, 8] [16, 16, 4]
from random import randint
def My_list(amount):
    my_list = []
    for k in range(amount):
        my_list.append(randint(1, 10))
    return my_list
new_list = My_list(int(input()))
print(new_list)
def Product(number):
    list = []
    i=0    
    for i in range(int((len(number))/2)+1):
        if i != int((len(number))/2):
            list.append(number[i]*number[-1-i])
        else:
            list.append(number[int((len(number))/2)])
    return list
print (Product(new_list))