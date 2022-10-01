# 3. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Без использования встроенной функции преобразования,
# без строк.         in 88  out  1011000 in 11 out 1011
def Binary(number):
    tabl = []
    while number:
        if number / 2 < 1:
            tabl.append(1)
            return tabl
        else:
            tabl.append(number % 2)
            number = int(number / 2)                    
number = Binary(int(input()))
number.reverse()
for i in number:
    print(i, end = "")