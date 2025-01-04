import pickle
from pickle import HIGHEST_PROTOCOL


def load_from_file(name_of_file):
    try:
        with open(name_of_file,'rb') as fp:
            load_data = pickle.load(fp)
    except FileNotFoundError:
        return 'File Not Found'
    return f'Данные: {load_data} получены из файла {name_of_file}'


class CountriesDict:
    def __init__(self):
        self.countries_dict = {}

    def add_country(self, country, capital):
        self.countries_dict.update({country: capital})

    def delete_country(self, country):
        for key, value in self.countries_dict.items():
            if key == country:
                self.countries_dict.pop(key)
                return f'{key},{value} :данные удалены'
        else:
            return 'данные для удаления не найдены'

    def search(self, data):
        for key, value in self.countries_dict.items():
            if data == key or data == value:
                return True
        else:
            return False

    def editing(self, data_to_search, new_data):
        for key, values in self.countries_dict.items():
            if key == data_to_search:
                self.countries_dict.update({key: new_data})
                return 'данные заменены'
        else:
            self.countries_dict.update({data_to_search: new_data})
            return f'в словарь добавлены новые данные: {data_to_search}: {new_data}'

    def show(self):
        return f'словарь: {self.countries_dict}'

    def save_to_file(self, name_of_file):
        with open(f'{name_of_file}.city', 'wb') as fp:
            pickle.dump(self.countries_dict, fp, HIGHEST_PROTOCOL)
        return f'данные записаны в файл {name_of_file}.city'


if __name__ == '__main__':
    country_dict = CountriesDict()
    country_dict.add_country('Russia', 'Moscow')
    country_dict.add_country('USA', 'Washington')
    country_dict.add_country('Ukraine', 'Kyew')
    print(country_dict.show())
    print(country_dict.search('Washington'))
    print(country_dict.delete_country('Ukraine'))
    print(country_dict.show())
    print(country_dict.search('Kyew'))
    print(country_dict.delete_country('Ukdraine'))
    print(country_dict.show())
    print(country_dict.editing('USA', 'Chicago'))
    print(country_dict.show())
    print(country_dict.editing('Egypt', 'Khair'))
    print(country_dict.show())
    print(country_dict.save_to_file('my_countries'))
    print(load_from_file('my_countries.city'))
