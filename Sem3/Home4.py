# 4.* Задайте список из произвольных вещественных чисел, количество
# задаёт пользователь. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# in5out[5.16, 8.62, 6.57, 7.92, 9.22]Min: 0.16, Max: 0.92. Difference: 0.76
# in 3 out [9.26, 8.5, 1.14] Min: 0.14, Max: 0.5. Difference: 0.36
from random import uniform

def My_list(amount):
    amount = amount if amount > 0 else -amount
    my_list = [round(uniform(1, 10), 2)for k in range(amount)]
    return my_list
my_list = My_list(int(input()))
print(my_list)

def Ostatki(list):
    tabl1 = []
    for i in range(len(list)):
        tabl1.append(round(list[i]-int(list[i]),2))
    return tabl1
tabl = Ostatki(my_list)

print (f"Разница между максимальным {max (tabl)} - и минимальным {min (tabl)}\
    значением дробной части элементов = {round(max (tabl)-min (tabl),2)}")


 




