# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет
day_week = int(input("введите день недели(цифру):  "))
if 6 <= day_week <= 7:
    print("Weekend")
elif 0 < day_week < 6:
    print("Workday")
else:
    print("Вы ввели не день недели!")
