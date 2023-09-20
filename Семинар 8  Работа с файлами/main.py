from actions import *
from menu import show_menu


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
            phone_book = change_number(phone_book)
            print(f'{write_txt("phone.txt",phone_book)}\n')
            phone_book = read_txt("phone.txt")
        elif choice == 4:
            lastname = input("Фамилия: ")
            phone_book = delete_by_lastname(phone_book, lastname)
            print(f'Абонент удален {write_txt("phone.txt",phone_book)}\n')
            phone_book = read_txt("phone.txt")
        elif choice == 5:
            number = input("Номер: ")
            print(find_by_number(phone_book, number))
        elif choice == 6:
            data = add_data(phone_book)
            print(f'Данные внесены {write_user("phone.txt",data)}\n')
            phone_book = read_txt("phone.txt")

        choice = show_menu()


if __name__ == "__main__":
    work_with_phonebook()
