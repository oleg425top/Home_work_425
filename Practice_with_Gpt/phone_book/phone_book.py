phone_book = {}


def append_user():
    user_name = input('Введите имя')
    phone = input('введите номер телефона')
    mail = input('введите маил')
    phone_book[user_name] = {'Phone': phone, 'Mail': mail}


def del_user():
    rm_user = input('Введите имя для удаления')
    if rm_user in phone_book:
        del phone_book[rm_user]
        print('абонент удален')
    else:
        print('абонент не найден')

def show():
    if not phone_book:
        print('Список пуст')
    else:
        for user in phone_book:
            print(user, phone_book[user])



if __name__ == '__main__':
    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Обновить контакт")
        print("4. Просмотреть все контакты")
        print("5. Выйти")

        choice = input("Выберите опцию: ")

        if choice == '1':
            append_user()
        elif choice == '2':
            del_user()
        elif choice == '4':
            show()
        elif choice == '5':
            print('До свидания')
            break