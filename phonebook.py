# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# 1) Создать телефонный справочник: +
#     - открыть файл для добавления (режим "а").    +
# 2) Добавить контакт:  +
#     - запросить информацию пользователя;  +
#     - подготовить информацию в нужном формате;    +
#     - открыть файл для добавления (режим "а");    +
#     - добавить контакт в файл.    +
# 3) Вывести данные на экран:   +
#     - открыть файл в режиме чтения ("r"); +
#     - вывести данные на экран.    +
# 4) Осуществить поиск данных:  +
#     - запросить вариант поиска;   +
#     - запросить информацию пользователя;  +
#     - открыть файл для чтения;    +
#     - сохранить файл в переменную;    +
#     - осуществить поиск;  +
#     - вывести информацию на экран.    +
# 5) Реализовать UI:    +
#     - вывести варианты меню;  +
#     - получение запроса пользователя; +
#     - реализация запроса пользователя;    +
#     - выход.  +


def input_name():
    return input("Введите имя: ")

def imput_surname():
    return input("Введите фамилию: ")

def input_patronus():
    return input("Введите отчество: ")

def input_phone():
    return input("Введите номер телефона: ")

def input_address():
    return input("Введите адрес: ")


def create_contact():
    name=input_name()
    surname=imput_surname()
    patronus=input_patronus()
    phone=input_phone()
    address=input_address()
    return f"{name} {patronus} {surname} {phone}\n{address}\n\n\n"


def add_contact():
    contact=create_contact()
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(contact)


def print_phonebook():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        contact_list=file.read().rstrip().split("\n\n")
        for nn, contact in enumerate(contact_list, 1):
            print(nn,contact)

    
def search_contact():
    
    
    case_search=input(
                    "Введите вариант поиска:\n"
                    "1. По имени\n"
                    "2. По отчееству\n"
                    "3. По фамилии\n"
                    "4. По номеру телефона\n"
                    "5. По адресу\n"
                    "Ваш выбор: "
    )
    
    while case_search not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод данных")
        case_search=input("Выберите вариант поиска: ")
        
    index_serch=int(case_search)-1
    search=input("Введите информацию для поиска: ")
    
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        contact_list=file.read().rstrip().split("\n\n")
        for contact_str in contact_list:
            contact_lst=contact_str.replace("\n", " ").split()
            if search in contact_lst[index_serch]:
                print(contact_str)


def copy_contact():
        
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        contact_list=file.read().rstrip().split("\n\n")
    
    set_num=set()
    for i in range(1,len(contact_list)+1):
        set_num.add(str(i))
            
    num_contact=input(f"Введите номер контакта (всего на данный момент {len(contact_list)} контактов): ")
        
    while num_contact not in set_num:
        num_contact=input(f"Введите номер контакта (всего на данный момент {len(contact_list)} контактов): ")

    with open("copy.txt", "a", encoding="UTF-8") as file:
        file.write(contact_list[int(num_contact)-1]+"\n\n")



def interface():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    commando="0"
    while commando!="5":
        print(
            "Варианты меню:\n"
            "1. Добавить контакт.\n"
            "2. Вывести на экран.\n"
            "3. Поиск контакта.\n"
            "4. Скопировать контакт в другой файл.\n"
            "5. Выход."
        )
        commando=input("Выберите пункт меню: ")
        while commando not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод данных")
            commando=input("Выберите пункт меню: ")

        if commando ==  "1":
            add_contact()
        if commando ==  "2":
            print_phonebook()
        if commando ==  "3":
            search_contact()
        if commando ==  "4":
            copy_contact()
        if commando ==  "5":
            print("Вышли.")
    


print()
interface()

