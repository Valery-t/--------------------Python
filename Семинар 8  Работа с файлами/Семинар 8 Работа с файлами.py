# Задача №49. Решение в группах Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def show_menu():
    print(
        "1. Распечатать справочник",
        "2. Найти телефон по фамилии",
        "3. Изменить номер телефона",
        "4. Удалить запись",
        "5. Найти абонента по номеру телефона",
        "6. Добавить абонента в справочник",
        "7. Закончить работу",
        sep="\n",
    )
    choice = int(input("Введите ваш выбор: "))
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt("phone.txt")
    while choice != 7:
        if choice == 1:
            print([print_result(phone_book)])
        elif choice == 2:
            last_name = input("Фамилия: ")
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input("Фамилия: ")
            new_number = input("Новый номер: ")
            phone_book = change_number(phone_book, last_name, new_number)
            print(f'Номер телефона изменен {write_txt("phone.txt",phone_book)}')
            phone_book = read_txt("phone.txt")
        elif choice == 4:
            lastname = input("Фамилия: ")
            phone_book = delete_by_lastname(phone_book, lastname)
            print(f'Абонент удален {write_txt("phone.txt",phone_book)}')
            phone_book = read_txt("phone.txt")
        elif choice == 5:
            number = input("Номер: ")
            print(find_by_number(phone_book, number))
        elif choice == 6:
            data = add_data()
            print(f'Данные внесены {write_user("phone.txt",data)}')
            phone_book = read_txt("phone.txt")

        choice = show_menu()


def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(
                zip(fields, line.strip().split(","))
            )  # dict(((фамилия, Иванов), (имя, Точка), (номер, 8928)))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s += v + ","
            phout.write(f"{s[:-1]}")


def print_result(phone_book):  # 1. Распечатать справочник
    for dict in phone_book:
        print(dict)


def find_by_lastname(phone_book, last_name):  # 2. Найти телефон по фамилии
    for dict in phone_book:
        if dict["Фамилия"] == last_name:
            print(f'Номер телефона: {dict.get("Телефон")}')


def change_number(phone_book, last_name, new_number):  # 3. Изменить номер телефона
    for dict in phone_book:
        if dict["Фамилия"] == last_name:
            dict["Телефон"] = new_number
    return phone_book


def delete_by_lastname(phone_book, lastname):  # 4. Удалить запись
    for dict in phone_book:
        if dict["Фамилия"] == lastname:
            del dict["Фамилия"], dict["Имя"], dict["Телефон"], dict["Описание"]
    return phone_book


def find_by_number(phone_book, number):  # 5. Найти абонента по номеру телефона
    for dict in phone_book:
        if dict["Телефон"] == number:
            print(f'Фамилия: {dict.get("Фамилия")}')


def add_data():  # 6. Добавить абонента
    surname = str(input("Введите фамилию: "))
    name = str(input("Введите имя: "))
    phone = int(input("Введите телефон: "))
    describe = str(input("Введите описание: "))
    return surname, name, phone, describe


def write_user(filename, data):  # 6.Записать абонента в справочник
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")


work_with_phonebook()
