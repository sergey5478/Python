# 1. Представлен список чисел. Необходимо вывести элементы исходного 
# списка, значения которых больше предыдущего элемента. Use comprehension.
# in 9 out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
from random import randint

def My_list(amount):
    my_list = [randint(0, 10)for k in range(amount)]          
    return my_list
list = (My_list(9))
print(list)

def Main(list):
    my_list = [list [i+1]for i in range(len(list)-1)if list [i+1] > list[i]]    
    return my_list    
print (Main(list))