from class_epmployer import Employee, Manager, Developer, Company

def main():
    company = Company()

    while True:
        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Просмотреть всех сотрудников")
        print("3. Рассчитать зарплату сотрудника")
        print("4. Выйти")

        choice = input("Выберите опцию: ")

        if choice == '1':
            name = input('Введите имя сотрудника')
            position = input('Введите должность сотрудника')
            salary = input('Введите зарплату сотрудника')
            type_employee = input('Введите тип сотрудника (Manager\Developer)')
            if type_employee.lower() == 'manager':
                bonus = float(input("Введите бонус: "))
                employee = Manager(name, position, salary, bonus)
            elif type_employee.lower() == 'developer':
                overtime_hours = int(input("Введите количество сверхурочных часов: "))
                employee = Developer(name, position, salary, overtime_hours)
            else:
                print("Неверный тип сотрудника.")
                continue
            company.add_employee(employee)
        elif choice == 2:
            return company.display_employers()

company = Company()
manager = Manager('dgfgd', 'fdhfgh', 1200, 500)
company.add_employee(manager)

