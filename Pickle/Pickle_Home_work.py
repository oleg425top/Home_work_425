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
