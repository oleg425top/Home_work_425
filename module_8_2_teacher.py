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
        return f' Имя: {self.get_name()}\nОбразование {self.__education}\nОпыт работы {self.get_experienc()}'
