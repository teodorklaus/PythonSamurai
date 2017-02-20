import unittest

from Serhii_Popov.week3.Student.StudentClass import *

class TestStudent(unittest.TestCase):
    def test_pib(self):
        name_t = Human('Name', 'Surname', 'Lastname', '1992-02-20', '1234567812')
        self.assertNotEqual(name_t.pib(), ('Surname Name Name'), msg='Surname Name Lastname != Surname Name Name')
        self.assertEqual(name_t.pib(), ('Surname Name Lastname'))
        return name_t

    def test_years(self):
        test_years = Human('Name', 'Surname', 'Lastname', '1992-02-20', '1234567812')
        self.assertEqual(test_years.years(), (25))

    def test_EduProg(self):
        test_edpr = EducationalProgres('60', '70', '22', 'Exam', 'OOP',
                                       '75', '80', '23', 'Credit', 'SQL',
                                       '80', '80', '25', 'Exam', 'Diagrams',
                                       '90', '99', '28', 'Exam', 'English')
        self.assertEqual(test_edpr.subject1(), (67.5), msg='67.5 = 67.5')
        self.assertNotEqual(test_edpr.subject2(), (67.5), msg= str(test_edpr.subject2()) + '!= 67.5' )
        self.assertEqual(test_edpr.subject3(), (81))
        self.assertNotEqual(test_edpr.subject4(), (95))

    def test_student(self):
        test_stud_hum = Human
        test_stud_st = Student
        self.assertEqual((str(test_stud_hum.__init__(self, 'Name', 'Surname', 'Lastname', '1992-02-25', '1234567812'))
                         + test_stud_st.studID(self))[4:16],
                         "SN1234567812")
        self.assertNotEqual((str(test_stud_hum.__init__(self, 'Name', 'Surname', 'Lastname', '1992-02-25', '1234567812'))
                         + test_stud_st.studID(self))[4:16],
                         'SK1231231231')



    def test_gradebook(self):
        test_grade_hm = Human
        test_grade_ep = EducationalProgres
        test_grade_st = Student
        test_grade_gr = GradeBook
        self.assertNotEqual((str(test_grade_hm.__init__(self, 'Name', 'Surname', 'Lastname', '1992-02-25', '1234567812'))
                          +
                          str(test_grade_ep.__init__(self, '60', '70', '22', 'Exam', 'OOP',
                                                 '75', '80', '23', 'Credit', 'SQL',
                                                 '80', '80', '25', 'Exam', 'Diagrams',
                                                 '90', '99', '28', 'Exam', 'English'))
                          +
                          test_grade_st.studID(self)
                          +
                          test_grade_gr.print(self))[20:]
                          , '')


if __name__ == '__main__':
    unittest.main()