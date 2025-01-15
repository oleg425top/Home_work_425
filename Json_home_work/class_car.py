import pickle


class Car:
    def __init__(self, brand, model, milage):
        self.brand = brand
        self.model = model
        self.milage = milage

    def display_info(self):
        print(f"Бранд: {self.brand}, Модель: {self.model}, Пробег: {self.milage}")

    def change_milage(self, new_year):
        self.milage = new_year
        print(f"Пробег был смотан до: {self.milage} км")


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

if __name__ == '__main__':
    car = Car('Lada', 'Largus',  100000)
    car.display_info()
    car.change_milage(80000)
    car.display_info()
    my_pickler = MyPickler()
    pickle_car = my_pickler.pickle_data(car)
    print(pickle_car)
    my_pickler.pickle_file('pickle_car.car', car)
    unpickle_car = MyUnPickler.unpickle_data(pickle_car)
    unpickle_car.display_info()
    unpickle_car.change_milage(55000)
    unpickle_car.display_info()
    unpickle_car_from_file = MyUnPickler.unpickled_file('pickle_car.car')
    unpickle_car_from_file.display_info()