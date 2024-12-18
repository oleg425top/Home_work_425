import unittest

from teacher import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    test_teacher = Teacher('test_name', 'test_education', 99)

    def test_01_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 2)
        self.assertEqual(Teacher.teacher_dict, {'new_name': ['new_education', 66], 'test_name': ['test_education', 99]})

    def test_02_get_name(self):
        self.assertEqual(self.test_teacher.get_name(), 'test_name')

    def test_03_get_education(self):
        self.assertEqual(self.test_teacher.get_education(), 'test_education')

    def test_04_get_experience(self):
        self.assertEqual(self.test_teacher.get_experience(), 99)

    def test_05_get_teacher_data(self):
        self.assertEqual(self.test_teacher.get_teacher_data(),
                         'Имя: test_name. Образование: test_education. Опыт работы: 99 (года/лет)')

    def test_05_set_experience(self):
        self.assertEqual(self.test_teacher.set_experience(100), 'Изменен опыт работы на 100 лет')

    def test_06_add_mark(self):
        self.assertEqual(self.test_teacher.add_mark('Коля', 5), 'test_name поставил оценку: 5 студенту: Коля')

    def test_07_remove_mark(self):
        self.assertEqual(self.test_teacher.remove_mark('Коля', 5), 'test_name удалил оценку: 5 студенту: Коля')

    def test_07_give_a_consultation(self):
        self.assertEqual(self.test_teacher.give_a_consultation('11A'), 'test_name провел консультацию в классе: 11A')

    def test_08_display_teacher_data(self):
        self.assertEqual(self.test_teacher.display_teacher_data(), 'Данные успешно выведены')
        self.assertEqual(Teacher.display_teacher_data(), 'Данные успешно выведены')

    def test_09_fire_teacher(self):
        self.assertEqual(self.test_teacher.fire_teacher(), 'Учитель test_name  был уволен')
        self.assertEqual(self.test_teacher.fire_teacher(), 'Учителя test_name  уже уволили')
        self.assertEqual(Teacher.teacher_dict, {'new_name': ['new_education', 66]})

class TestDisciplineTeacher(unittest.TestCase):
    test_discipline_teacher = DisciplineTeacher('new_name', 'new_education', 66, 'test_discipline', 'test_job_title')

    def test_10_init(self):
        self.assertEqual(len(DisciplineTeacher.discipline_teacher_dict), 1)
        self.assertEqual(DisciplineTeacher.discipline_teacher_dict, {'new_name': ['test_discipline', 'test_job_title']})

    def test_11_get_discipline(self):
        self.assertEqual(self.test_discipline_teacher.get_discipline(), 'test_discipline')

    def test_12_get_job_title(self):
        self.assertEqual(self.test_discipline_teacher.get_job_title(), 'test_job_title')

    def test_13_get_teacher_data(self):
        self.assertEqual(self.test_discipline_teacher.get_teacher_data(),
                         'Имя: new_name. Образование: new_education. Опыт работы: 66 (года/лет)\nПредмет test_discipline. Должность test_job_title')

    def test_14_add_mark(self):
        self.assertEqual(self.test_discipline_teacher.add_mark('test_student', 5),
                         'new_name, поставил оценку 5 студенту test_student\nПредмет test_discipline')

    def test_15_remove_mark(self):
        self.assertEqual(self.test_discipline_teacher.remove_mark('test_student', 4), 'new_name, удалил оценку 4 студенту test_student\nПредмет test_discipline')

    def test_16_give_a_consultation(self):
        self.assertEqual(self.test_discipline_teacher.give_a_consultation('8A'), 'new_name провел консультацию в классе 8A\nПо предмету test_discipline как test_job_title')

    def test_17_fire_discipline_teacher(self):
        self.assertEqual(self.test_discipline_teacher.fire_discipline_teacher(),'Учитель new_name по дисциплине test_discipline  был уволен')
        self.assertEqual(self.test_discipline_teacher.fire_discipline_teacher(),'Учителя new_name по дисциплине test_discipline уже уволили')
        self.assertEqual(DisciplineTeacher.discipline_teacher_dict, {})
        self.assertEqual(len(DisciplineTeacher.discipline_teacher_dict), 0)

