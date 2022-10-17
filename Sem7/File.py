
def Search():
    with open('directory.csv', 'r', encoding = 'utf-8') as data:
        data2 = data.readlines()
        flag = 1
        name = input('Введите фамилию клиента > \n')
        for line in data2:       
            if name in line:
                flag = 0
                print(line)
        if flag: print('no name given')
    return name

def Delet():
     with open('directory.csv', 'r', encoding = 'utf-8') as data:
        data2 = data.readlines()
        flag = 1
        name = input('Номер телефона записи, которую хотите удалить\n')
        with open('directory.csv', 'w', encoding = 'utf-8') as data3:
            for line in data2:       
                if name not in line:
                    data3.write(line)
            
        return name

def Add():
    with open('directory.csv', 'a', encoding = 'utf-8') as data:
        line = input('Введите Фамилию Имя телефон \n')
        data.write(line + '\n')
    return line

 