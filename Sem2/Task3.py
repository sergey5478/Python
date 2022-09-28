# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.
n = int(input())
my_list = []
for k in range (1,n+1):
    my_list.append (3*k + 1)
print(my_list)
