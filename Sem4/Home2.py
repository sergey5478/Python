# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Простые делители числа in 54 out [2, 3, 3, 3]
number = int(input("Введите число: "))
def Factors(number):
    i = 2
    result = []
    while i**2 <= number:
        while number % i == 0:
            result.append(i)
            number /= i
        i += 1
    if number > 1:
        result.append(int(number))
    return result
print(f"Список простых множителей числа {number} равен {Factors(number)}")