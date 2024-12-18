import unittest

from Teacher_unittest.teacher import DisciplineTeacher


class TestDisciplineTeacher(unittest.TestCase):
    test_discipline_teacher = DisciplineTeacher('new_name', 'new_education', 66, 'test_discipline', 'test_job_title')

    def test_01_init(self):
        self.assertEqual(len(DisciplineTeacher.discipline_teacher_dict), 1)
        self.assertEqual(DisciplineTeacher.discipline_teacher_dict, {'new_name': ['test_discipline', 'test_job_title']})

    def test_02_get_discipline(self):
        self.assertEqual(self.test_discipline_teacher.get_discipline(), 'test_discipline')

    def test_03_get_job_title(self):
        self.assertEqual(self.test_discipline_teacher.get_job_title(), 'test_job_title')

    def test_04_get_teacher_data(self):
        self.assertEqual(self.test_discipline_teacher.get_teacher_data(),
                         'Имя: new_name. Образование: new_education. Опыт работы: 66 (года/лет)\nПредмет test_discipline. Должность test_job_title')

    def test_05_add_mark(self):
        self.assertEqual(self.test_discipline_teacher.add_mark('test_student', 5),
                         'new_name, поставил оценку 5 студенту test_student\nПредмет test_discipline')

    def test_06_remove_mark(self):
        self.assertEqual(self.test_discipline_teacher.remove_mark('test_student', 4), 'new_name, удалил оценку 4 студенту test_student\nПредмет test_discipline')

    def test_07_give_a_consultation(self):
        self.assertEqual(self.test_discipline_teacher.give_a_consultation('8A'), 'new_name провел консультацию в классе 8A\nПо предмету test_discipline как test_job_title')

    def test_08_fire_discipline_teacher(self):
        self.assertEqual(self.test_discipline_teacher.fire_discipline_teacher(),'Учитель new_name по дисциплине test_discipline  был уволен')
        self.assertEqual(self.test_discipline_teacher.fire_discipline_teacher(),'Учителя new_name по дисциплине test_discipline уже уволили')
        self.assertEqual(DisciplineTeacher.discipline_teacher_dict, {})
        self.assertEqual(len(DisciplineTeacher.discipline_teacher_dict), 0)
