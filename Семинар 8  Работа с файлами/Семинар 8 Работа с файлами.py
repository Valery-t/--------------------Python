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
            print_result(phone_book)
        elif choice == 2:
            last_name = input("lastname ")
            print(find_by_lastname(phone_book, last_name))
        # elif choice == 3:
        #     last_name = input("lastname ")
        #     new_number = input("new number ")
        #     print(change_number(phone_book, last_name, new_number))
        # elif choice == 4:
        #     lastname = input("lastname ")
        #     print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input("number ")
            print(find_by_number(phone_book, number))
        # elif choice == 6:
        #     user_data = input("new data ")
        #     add_user(phone_book, user_data)
        #     write_txt("phonebook.txt", phone_book)
        choice = show_menu()


def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(
                zip(fields, line.split(","))
            )  # dict(((фамилия, Иванов), (имя, Точка), (номер, 8928)))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open("phone.txt", "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s += v + ","
            phout.write(f"{s[:-1]}\n")


def print_result(phone_book):
    for dict in phone_book:
        x = [*dict.values()]
        print(x)


def find_by_number(phone_book, number):  # 5. Найти абонента по номеру телефона
    for dict in phone_book:
        if dict["Телефон"] == int(number):
            print(dict.get("Фамилия"))


def delete_by_lastname(phone_book, lastname):
    for dict in phone_book:
        if lastname in dict:
            del dict["lastname"]
            print(f"Элемент с ключом {lastname} удален")
        else:
            print("Элемент не найден")


def add_user(phone_book, user_data):
    re


def find_by_lastname(phone_book, last_name):  # 2. Найти телефон по фамилии
    for dict in phone_book:
        if dict["Фамилия"] == str(last_name):
            print(dict.get("Телефон"))
            break


work_with_phonebook()
