class Stadium:
    def __init__(self, name, capacity, year_opened):
        self.name = name
        self.capacity = capacity
        self.year_opened = year_opened

    def display_info(self):
        return f"Название: {self.name}, Вместимость: {self.capacity}, Год открытия: {self.year_opened}"

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        return f"Вместимость стадиона увеличена до:  {self.capacity} человек"