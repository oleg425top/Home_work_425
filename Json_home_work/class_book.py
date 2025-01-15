import pickle
import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Год: {self.year}")

    def change_year(self, new_year):
        self.year = new_year
        print(f"Год издания был изменен на: {self.year}")

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