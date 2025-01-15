class Car:
    def __init__(self, brand, model, milage):
        self.brand = brand
        self.model = model
        self.milage = milage

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Milage {self.milage}")

    def change_milage(self, new_year):
        self.milage = new_year
        print(f"Пробег был смотан до: {self.milage} км")