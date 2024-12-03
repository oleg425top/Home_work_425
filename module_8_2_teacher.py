class Teacher:
    def __init__(self, name, education, experience):
        self.discipline = None
        self.mark_of_student = None
        self.name_of_student = None
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience

    def get_teacher_data(self):
        return f'Имя: {self.get_name()}\nОбразование: {self.get_education()}\nОпыт работы: {self.get_experience()} года/лет'

    def add_mark(self, name_of_student, mark_of_student):
        self.name_of_student = name_of_student
        self.mark_of_student = mark_of_student
        return f'{self.get_name()} поставил оценку: {self.mark_of_student} студенту: {self.name_of_student}'

    def remove_mark(self, name_of_student, mark_of_student):
        self.name_of_student = name_of_student
        self.mark_of_student = mark_of_student
        return f'{self.get_name()} удалил оценку: {self.mark_of_student} студенту: {self.name_of_student}'




teacher_1 = Teacher('Иван Петров', 'БГПУ', 4)
teacher_1.set_experience(8)
print()
# print()
print(teacher_1.get_teacher_data())
print()
print(teacher_1.add_mark('Вася Пупкин', 5))
print(teacher_1.remove_mark('Иван Иванов', 3))

