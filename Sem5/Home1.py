# 1. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". В тексте используется разделитель пробел.
# in Number of words: 10
# out авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
from random import sample

# def Get_word(number):
#     word = 'абв'
#     result = []
#     for i in range(number):
#         temp = sample(word, k = 3)
#         result.append(''.join(temp))     
#     return ' '.join(result)

def Get_word(number: int, alp: str = 'абв'):
    return " ".join("".join(sample(alp, 3)) for _ in range(number))

def Sorting(tabl):
    tabl = list(filter(lambda x: 'абв' not in x, tabl.split()))
    return " ".join(tabl)

my_list = Get_word(int(input('in Number of words ')))
print(my_list)
print(Sorting(my_list))