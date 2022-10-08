# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in 
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
start = 'aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa\
vvvvvvvvvvvbbwwPPuuuTTYyWWQQ'
with open('text_words.txt', 'w', encoding='utf-8') as data1:
    data1.writelines(start)

with open('text_words.txt', 'r') as data2:
    data = ''
    for line in data2:
        data += line
    print(data)

def Encode(data): 
    result = '' 
    prev_char = '' 
    a = 1 
    if not data: return '' 
    for i in data: 
        if i != prev_char:                 
                if prev_char: 
                    result += str(a) + prev_char 
                a = 1 
                prev_char = i 
        else: 
            a += 1 
    else: 
        result += str(a) + prev_char 
        return result
encoded_val = Encode(data) 
print(encoded_val)

with open('text_code_words.txt', 'w', encoding='utf-8') as data3:
    data3.writelines(encoded_val)

with open('text_code_words.txt', 'r') as data4:
    data5 = ''
    for line in data4:
        data5 += line
    print(data5)

def Decode(data):
    result = ''
    a = ''
    for i in data:        
        if i.isdigit():            
           a += i 
        else:            
            result += i * int(a)
            a = ''
    return result
decoded_val = Decode(data5)
print(decoded_val)

with open('text_decode_words.txt', 'w', encoding='utf-8') as data33:
    data33.writelines(decoded_val)