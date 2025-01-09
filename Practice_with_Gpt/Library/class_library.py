class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year  = year

    def __str__(self):
        return (f'Книга под названием {self.title}\n'
                f'Год выпуска: {self.year}\n'
                f'Написана автором: {self.author}\n')

class Library:
    def __init__(self):
        self.library_list = []

    def __str__(self):
        return f'Список книг в библиотеке:\n{[book.__str__() for book in self.library_list]}'

    def app_book(self, book):
        self.library_list.append(book)
        return f'Книга {book.title} добавлена в библиотеку'

    def show_books(self):
        [print(book) for book in self.library_list]
        return 'Библиотека перед вами ^'

    def remove_book(self, title):
        for book in self.library_list:
            if book.title == title:
                self.library_list.remove(book)
                return f'Книга "{book.title}" удалена из библиотеки'


if __name__ == '__main__':
    book_1 = Book('451° по Фаренгейту', 'Рэй Брэдбери', 2000)
    book_2 = Book('1984', 'Джордж Оруэлл', 1995)
    book_3 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1965)
    # print(book_1)
    library_1 = Library()
    print(library_1.app_book(book_1))
    print(library_1.app_book(book_2))
    print(library_1.app_book(book_3))

    # print(library_1)
    print(library_1.remove_book('451° по Фаренгейту'))
    print()
    print(library_1)
    print()
    print(library_1.show_books())
