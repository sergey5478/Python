# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
n = 10
list = []
for i in range(n):
    list.append(i)
print(list, end=" ")
for i in list:
    temp = list[i]
    randomI = random.randint(0, 9)
    list[i] = list[randomI]
    list[randomI] = temp
print(list, end=" ")
