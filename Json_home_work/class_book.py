import pickle
import json
from json import JSONEncoder


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"

    def change_year(self, new_year):
        self.year = new_year
        return f"Год издания был изменен на: {self.year}"

class MyPickler:
    def __init__(self, protocol=pickle.HIGHEST_PROTOCOL):

        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data):
        pickle_data = pickle.dumps(data, self.protocol)
        return pickle_data

    def pickle_file(self, file_name, data):
        with open(file_name, 'wb') as fp:
            pickle.dump(data, fp, self.protocol)
        return 'произведен пиклинг в файл'

class MyUnPickler:
    @classmethod
    def unpickle_data(cls, pickle_data):
        unpickled_data = pickle.loads(pickle_data)
        return unpickled_data

    @classmethod
    def unpickled_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as fp:
                unpickle_data = pickle.load(fp)
        except FileNotFoundError:
            return 'Файл не найден'
        else:
            return unpickle_data

class MyBookEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            'Название: ': o.title,
            'Автор: ': o.author,
            'Год издания: ': o.year,
            'Название класса: ': o.__class__.__name__,
            'Методы класса: ':{
                'display_info: ':o.display_info(),
                'change_year: ': o.change_year(1950)
            }
        }
if __name__ == '__main__':

    my_book = Book("1984", "George Orwell", 1949)
    json_book = json.dumps(my_book, cls=MyBookEncoder, ensure_ascii=False, indent=3)
    print(json_book)
    with open(r'class_book.json', 'w', encoding='utf-8') as fh:
        json.dump(my_book, fh, cls=MyBookEncoder, ensure_ascii=False, indent=3)

    with open(r'class_book.json', 'r', encoding='utf-8') as fh:
        python_book_from_json = json.load(fh)
    print(python_book_from_json)