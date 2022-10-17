# 2. Создать телефонный справочник с возможностью импорта 
# и экспорта данных в нескольких форматах.
client = 'Фамилия Имя №Телефона Описание'
client1 = 'Иванов Сергей 112233 домашний'
client2 = 'Петров Александр 445566 рабочий'
client3 = 'Сидоров Андрей 778899 корпоративный'
with open('directory.csv', 'w', encoding='utf-8') as data1:
    data1.write(f"{client}\n")
    data1.write(f"{client1}\n")
    data1.write(f"{client2}\n")
    data1.write(f"{client3}\n")

with open('directory.csv', 'r', encoding='utf-8') as data2:
    data = data2.readlines()    
    for line in data:
        print((line.strip('\n')))

def search(data):        
    flag = 1
    name = input('Введите фамилию клиента > ')
    for line in data:               
        if name in line:
            flag = 0
            print(f"\033[32m {line} \033[39m")
    if flag: print('no name given')
search(data)  