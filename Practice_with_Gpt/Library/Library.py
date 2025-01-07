library = []


def app_book():
    title = input('Введите название книги')
    author = input('Введите автора книги')
    library.append({'Title': title, 'Author': author})
    print('книга добавлена')


def del_book():
    title = input('введите название книги')
    for book in library:
        if title == book['Title']:
            library.remove(book)
            print(book, 'удалена')


def show_library():
    if not library:
        return print('библиотека пуста')
    else:
        for book in library:
            print(book)
    return print('библиотека показана')


if __name__ == '__main__':
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Просмотреть все книги")
        print("4. Выйти")

        choice = int(input("Выберите опцию: "))
        if choice == 1:
            app_book()

        elif choice == 2:
            del_book()

        elif choice == 3:
            show_library()

        elif choice == 4:
            break

        else:
            print('неправильный выбор\nПовторите попытку')


    # show_library()
    # app_book('451° по Фаренгейту', 'Рэй Брэдбери')
    # app_book('1984', 'Джордж Оруэлл')
    # app_book('Мастер и Маргарита', 'Михаил Булгаков')
    # show_library()
    # del_book('Мастер и Маргарита')
    # print()
    # show_library()
