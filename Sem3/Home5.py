# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов. Негафибоначчи
# in 8 out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in 5 out 5 -3 2 -1 1 0 1 1 2 3 5
def Fibonachi(num):
    list = [0]
    fib1 = fib2 = 1

    for i in range(num):
        if i == 0:
            list.append(fib1)
            list.insert(0, fib1)
            continue
        if i == 1:
            list.append(fib2)
            list.insert(0, fib2 * -1)
            continue
        fib_sum = fib1 + fib2
        list.append(fib_sum)
        list.insert(0, (fib_sum) * (-1) ** i)
        fib1 = fib2
        fib2 = fib_sum
    return list

list = Fibonachi(int(input()))
for i in list:
    print(i, end=" ")
print()