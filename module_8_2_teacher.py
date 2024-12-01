class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experienc(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience

    def get_teacher_data(self):
        return f'Имя: {self.get_name()}\nОбразование: {self.__education}\nОпыт работы: {self.get_experienc()} года/лет'

    def add_mark(self, name_of_student, mark_of_student):
        self.name_of_student = name_of_student
        self.mark_of_student = mark_of_student
        return f'{self.get_name()} поставил оценку: {self.mark_of_student} студенту: {self.name_of_student}'


teacher_1 = Teacher('Иван Петров', 'БГПУ', 4)
teacher_1.set_experience(8)
print(teacher_1.add_mark('Вася Пупкин', 5))
print(teacher_1.get_name())
print(teacher_1.get_teacher_data())