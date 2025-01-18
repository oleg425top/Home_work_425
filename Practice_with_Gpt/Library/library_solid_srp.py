class Book:

    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.available = True

    def __str__(self):
        return f'Книга под названием: {self.title}, автор: {self.author}'

class Library:
    def __init__(self):
         self.books_list = []

    def append_book(self, book):
        self.books_list.append(book)

    def search_book(self, title = None, author = None):
        for book in self.books_list:
            if not title:
                title = ' '
            if not author:
                author = ''
            if (title and title == book.title) or (author and author == book.author):

                return f'{book} - найдена '
            else:
                return f"Название: {title}, автор:  {author} :таких данных нет в библиотеке"

    def show_library(self):
        for book in self.books_list:
            print(book)

book_1 = Book('451° по Фаренгейту', 'Рэй Брэдбери')
book_2 = Book('1984', 'Джордж Оруэлл')
library = Library()
library.append_book(book_1)
library.append_book(book_2)
library.show_library()
print(library.search_book(title='453'))
print(library.search_book(title='451° по Фаренгейту'))





