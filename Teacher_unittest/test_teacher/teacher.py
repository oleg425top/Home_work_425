class Teacher:
    teacher_dict = {}

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.teacher_dict[self.__name] = [self.__education, self.__experience]

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience
        return f'Изменен опыт работы на {new_experience} лет'

    def get_teacher_data(self):
        return f'Имя: {self.get_name()}. Образование: {self.get_education()}. Опыт работы: {self.get_experience()} (года/лет)'

    def add_mark(self, name_of_student, mark_of_student):
        self.name_of_student = name_of_student
        self.mark_of_student = mark_of_student
        return f'{self.get_name()} поставил оценку: {self.mark_of_student} студенту: {self.name_of_student}'

    def remove_mark(self, name_of_student, mark_of_student):
        self.name_of_student = name_of_student
        self.mark_of_student = mark_of_student
        return f'{self.get_name()} удалил оценку: {self.mark_of_student} студенту: {self.name_of_student}'

    def give_a_consultation(self, class_of_school):
        self.class_of_school = class_of_school
        return f'{self.get_name()} провел консультацию в классе: {self.class_of_school}'

    def fire_teacher(self):
        if self.__name in Teacher.teacher_dict.keys():
            Teacher.teacher_dict.pop(self.__name)
            return f'Учитель {self.__name}  был уволен'
        else:
            return f'Учителя {self.__name}  уже уволили'

    @staticmethod
    def display_teacher_data():
        for name, data in Teacher.teacher_dict.items():
            print(f'имя: {name}')
            print(f'образование: {data[0]}')
            print(f'опыт: {data[1]}')
            print()
        return 'Данные успешно выведены'


class DisciplineTeacher(Teacher):
    discipline_teacher_dict = {}

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__job_title = job_title
        self.__discipline = discipline
        DisciplineTeacher.discipline_teacher_dict[self.get_name()] = [self.__discipline, self.__job_title]

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, new_job_title):
        self.__job_title = new_job_title
        return self.__job_title

    def get_teacher_data(self):
        data = super().get_teacher_data()
        return f"{data}\nПредмет {self.get_discipline()}. Должность {self.get_job_title()}"

    def add_mark(self, student_name, mark_of_student):
        data = super().get_name()
        return f"{data}, поставил оценку {mark_of_student} студенту {student_name}\nПредмет {self.get_discipline()}"

    def remove_mark(self, student_name, mark_of_student):
        super().remove_mark(student_name, mark_of_student)
        return (f"{self.get_name()}, удалил оценку {mark_of_student} студенту {student_name}\n"
                f"Предмет {self.get_discipline()}")

    def give_a_consultation(self, class_of_school):
        super().give_a_consultation(class_of_school)
        return (f"{self.get_name()} провел консультацию в классе {class_of_school}\n"
                f"По предмету {self.get_discipline()} как {self.__job_title}")

    def fire_discipline_teacher(self):
        if self.get_name() in DisciplineTeacher.discipline_teacher_dict.keys():
            DisciplineTeacher.discipline_teacher_dict.pop(self.get_name())
            return f'Учитель {self.get_name()} по дисциплине {self.__discipline}  был уволен'
        else:
            return f'Учителя {self.get_name()} по дисциплине {self.__discipline} уже уволили'


