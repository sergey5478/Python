# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.
a = int(input("enter a"))
b = int(input("enter a"))

if a == b**2 or b == a**2:
    print("Yes")
else:
    print("No")
