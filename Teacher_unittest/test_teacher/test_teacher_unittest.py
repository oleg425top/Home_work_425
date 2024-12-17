import  unittest
from Teacher_unittest.teacher import Teacher, DisciplineTeacher

class TestTeacher(unittest.TestCase):

    test_teacher = Teacher('test_name', 'test_education', 99)

    def test_01_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 1)
        self.assertEqual(Teacher.teacher_dict, {'test_name': ['test_education', 99]})



#    def test_1_init(self):
#         self.assertEqual(len(Employer.employers_dict), 1)
#         self.assertEqual(Employer.employers_dict, {'test_phone': ['test_name', 'test_surname']})
