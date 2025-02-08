class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'Сотрудник: {self.name}\nДолжность {self.position}\nЗП: {self.salary}'

    def display_info(self):
        return f'Сотрудник: {self.name}\nДолжность {self.position}\nЗП: {self.salary}'

    def calculate_salary(self):
        return f'Зарплата сотрудника: {self.salary}'

class Manager(Employee):
    def __init__(self, name, position, salary, bonus):
        super().__init__(name, position, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return f'зарплата менеджера :{self.salary + self.bonus}'

class Developer(Employee):
    def __init__(self, name, position, salary, overtime_hours):
        super().__init__(name, position, salary)
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        overtime_pay = self.overtime_hours * 50
        return f'Зарплата рабочего: {self.salary + overtime_pay}'

class Company:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)
        return f'Сотрудник по имени {employee.name} добавлен!'

    def display_employers(self):
        if not self.employee_list:
            print('компания пуста!')
        else:
            for employee in self.employee_list:
                print(employee.display_info())

    def calculate_salary(self, name):
        for employee in self.employee_list:
            if employee.name == name:
                print(f'зарплата сотрудника {name} = {employee.calculate_salary()}')
                return
            else:
                print('Такого сотрудника у нас нет!')

