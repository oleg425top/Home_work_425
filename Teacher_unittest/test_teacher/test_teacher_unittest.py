import  unittest
from Teacher_unittest.teacher import Teacher, DisciplineTeacher

class TestTeacher(unittest.TestCase):

    test_teacher = Teacher('test_name', 'test_education', 99)

    def test_01_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 1)
        self.assertEqual(Teacher.teacher_dict, {'test_name': ['test_education', 99]})

    def test_02_get_name(self):
        self.assertEqual(self.test_teacher.get_name(), 'test_name')

    def test_03_get_education(self):
        self.assertEqual(self.test_teacher.get_education(), 'test_education')

    def test_04_get_experience(self):
        self.assertEqual(self.test_teacher.get_experience(), 99)

    def test_05_get_teacher_data(self):
        self.assertEqual(self.test_teacher.get_teacher_data(), 'Имя: test_name. Образование: test_education. Опыт работы: 99 (года/лет)')

    def test_06_add_mark(self):
        self.assertEqual(self.test_teacher.add_mark('Коля', 5), 'test_name поставил оценку: 5 студенту: Коля')

    def test_07_remove_mark(self):
        self.assertEqual(self.test_teacher.remove_mark('Коля', 5), 'test_name удалил оценку: 5 студенту: Коля')

    def test_07_give_a_consultation(self):
        self.assertEqual(self.test_teacher.give_a_consultation('11A'), 'test_name провел консультацию в классе: 11A')

    def test_08_display_teacher_data(self):
        self.assertEqual(self.test_teacher.display_teacher_data(),'Данные успешно выведены')
        self.assertEqual(Teacher.display_teacher_data(),'Данные успешно выведены')

    def test_09_fire_teacher(self):
        self.assertEqual(self.test_teacher.fire_teacher(), 'Учитель test_name  был уволен')
        self.assertEqual(self.test_teacher.fire_teacher(), 'Учителя test_name  уже уволили')


#    def test_1_init(self):
#         self.assertEqual(len(Employer.employers_dict), 1)
#         self.assertEqual(Employer.employers_dict, {'test_phone': ['test_name', 'test_surname']})
