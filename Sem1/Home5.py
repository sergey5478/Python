# 5. Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# in
# - 3  -6  -2  -1
# out
# 5.099
xA = int(input("Введите координату x, точки A:  "))
yA = int(input("Введите координату y, точки A:  "))
xB = int(input("Введите координату x, точки B:  "))
yB = int(input("Введите координату x, точки B:  "))
distanceAB = ((xB - xA)**2 + (yB - yA)**2)**0.5
print (f"{(distanceAB):.3f}")