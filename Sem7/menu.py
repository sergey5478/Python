import Input
import File
 
def Number():
    print ('1 Поиск записи по фамилии')
    print ('2 Удалить запись из справочника')
    print ('3 Добавить запись в справочник')
    
    number = Input.Input()
    if number == 1:
        File.Search()
    elif number == 2:
        File.Delet()
    elif number == 3:
        File.Add()