# 3. Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = int(input("введите x (x не должен быть равен 0):  "))
y = int(input("введите y (y не должен быть равен 0):  "))
if x > 0 and y > 0:
    print("точка находится в 1 четверти координат")
elif x > 0 and y < 0:
    print("точка находится в 4 четверти координат")
elif x < 0 and y < 0:
    print("точка находится в 3 четверти координат")
elif x < 0 and y > 0:
    print("точка находится во 2 четверти координат")
else:
    print("Вы ввели ноль!")
