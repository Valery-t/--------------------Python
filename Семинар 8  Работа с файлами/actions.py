def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            if line.strip():
                for i in line:
                    " ".join(i.strip())
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
            phout.write(f"{s[:-1]}\n")


def print_result(phone_book):  # 1. Распечатать справочник
    for dict in phone_book:
        print(dict)


def find_by_lastname(phone_book, last_name):  # 2. Найти телефон по фамилии
    for dict in phone_book:
        if dict["Фамилия"] == last_name:
            print(f'Номер телефона: {dict.get("Телефон")}')


def change_number(phone_book):  # 3. Изменить номер телефона
    while True:
        last_name = input("Фамилия:\n" + '(для выхода введите "q")')
        for dict in phone_book:
            if dict["Фамилия"] == last_name:
                while True:
                    new_number = input("Новый номер: ")
                    check_phone = check_phone_number(phone_book, new_number)
                    if check_phone is True:
                        print("Такой номер уже введен, введите другой")
                        continue
                    elif check_phone is False:
                        dict["Телефон"] = new_number
                        print("Номер телефона изменен")
                        return phone_book
        if last_name == "q":
            break
        print("Такой фамилии нет")
    return phone_book


def check_phone_number(phone_book, phone):
    for dict in phone_book:
        if dict["Телефон"] == phone:
            return True
    return False


def delete_by_lastname(phone_book, lastname):  # 4. Удалить запись
    for dict in phone_book:
        if dict["Фамилия"] == lastname:
            del dict["Фамилия"], dict["Имя"], dict["Телефон"], dict["Описание"]
    return phone_book


def find_by_number(phone_book, number):  # 5. Найти абонента по номеру телефона
    for dict in phone_book:
        if dict["Телефон"] == number:
            print(f'Фамилия: {dict.get("Фамилия")}')


def add_data(phone_book):  # 6. Добавить абонента
    while True:
        surname = str(input("Введите фамилию: "))
        name = str(input("Введите имя: "))
        phone = str(input("Введите телефон: "))
        describe = str(input("Введите описание: "))
        check = check_data(phone_book, phone)
        if check != True:
            break
        print("Такой номер уже введен, введите другой")
    return surname, name, phone, describe


def check_data(phone_book, number):
    for dict in phone_book:
        if dict["Телефон"] == number:
            return True


def write_user(filename, data):  # 6.Записать абонента в справочник
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
