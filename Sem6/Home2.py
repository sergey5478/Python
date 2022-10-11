# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. 
# Use comprehension. in 100 out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
def My_list (amount):
    my_list = [i for i in range(20, amount+1)]    
    return my_list
list = My_list(int(input()))
print(list)
def Main (list):
    my_list = [list[i]for i in range(len(list))\
        if list[i] % 20 == 0 or list[i] % 21 == 0]
    return my_list
print (Main(list))