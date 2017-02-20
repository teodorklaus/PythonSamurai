import datetime




class Human:
    def __init__(self, n, s, l, b, i):
        self.name = n                   #імя
        self.surname = s                #фамілія
        self.lastname = l               #по-батькові
        self.birthdate = b              #дата народження
        self.persontaxid = i            #ІНН(ідентифікаційний код)

    def pib(self):
        self.fullname = (self.surname + " " + self.name + " " + self.lastname)                                        #Повне Ім'я
        self.initials = self.surname + " " + self.name[0] + "." + " " + self.lastname[0] + "."                      #ПІБ
        return self.fullname

    def years(self):
        self.humanage = datetime.date.today().year - datetime.datetime.strptime((self.birthdate), "%Y-%m-%d").year   #Вік людини
        return self.humanage


class EducationalProgres:
    def __init__(self, vis1, eps1, es1, et1, en1, vis2, eps2, es2, et2, en2,  vis3, eps3, es3, et3, en3,  vis4, eps4, es4, et4, en4):
        # vi, aem,
        #self.visiting = vi                              #Відвідування
        #self.averageedumark = aem                       #Бал за навчальний процес
        self.VisSub1 = vis1                             #Відвідування навчальний предмет №1
        self.EduProgSub1 = eps1                          #Бал за навчальний процес прдмет №1
        self.ExamSub1 = es1                              #Баз за екзамен навчальний процес №1
        self.EduType1 = et1                              #Тип предмету (залік\екзамен) #1
        self.EduName1 = en1                               #Назва предмету №1
        self.VisSub2 = vis2                              #Відвідування навчальний предмет №2
        self.EduProgSub2 = eps2                          #Бал за навчальний процес прдмет №2
        self.ExamSub2 = es2                              #Баз за екзамен навчальний процес №2
        self.EduType2 = et2                              #Тип предмету (залік\екзамен) #2
        self.EduName2 = en2                               # Назва предмету №2
        self.VisSub3 = vis3                              #Відвідування навчальний предмет №3
        self.EduProgSub3 = eps3                          #Бал за навчальний процес прдмет №3
        self.ExamSub3 = es3                              #Баз за екзамен навчальний процес №3
        self.EduType3 = et3                              #Тип предмету (залік\екзамен) #3
        self.EduName3 = en3                              # Назва предмету №3
        self.VisSub4 = vis4                              #Відвідування навчальний предмет №4
        self.EduProgSub4 = eps4                          #Бал за навчальний процес прдмет №4
        self.ExamSub4 = es4                              #Баз за екзамен навчальний процес №4
        self.EduType4 = et4                              #Тип предмету (залік\екзамен) #4
        self.EduName4 = en4                              # Назва предмету №4
        self.LitMarkValueSub1 = ''
        self.LitMarkValueSub2 = ''
        self.LitMarkValueSub3 = ''
        self.LitMarkValueSub4 = ''


    def literalValue(self, other):
        if self >= 60 and self <= 67:
            other = 'E'  # Буквений загальний бал за предмет №1
        elif self >= 68 and self <= 74:
            other = 'D'  # Буквений загальний бал за предмет №1
        elif self >= 75 and self <= 80:
            other = 'C'  # Буквений загальний бал за предмет №1
        elif self >= 81 and self <= 90:
            other = 'B'  # Буквений загальний бал за предмет №1
        elif self >= 91 and self <= 100:
            other = 'A'  # Буквений загальний бал за предмет №1
        return other

    def subject1(self):
        self.ScMarkSub1 = (((int(self.VisSub1) + int(self.EduProgSub1)) / 2) * 0.7) + int(self.ExamSub1)    #Кінцевий бал предмент №1
        self.LitMarkValueSub1 = EducationalProgres.literalValue(self.ScMarkSub1, '')         #Буквений загальний бал за предмет №1
        return self.ScMarkSub1

    def subject2(self):
        self.ScMarkSub2 = (((int(self.VisSub2) + int(self.EduProgSub2)) / 2) * 0.7) + int(self.ExamSub2)     #Кінцевий бал предмент №2
        self.LitMarkValueSub2 = EducationalProgres.literalValue(self.ScMarkSub2, '')          # Буквений загальний бал за предмет №2
        return self.ScMarkSub2

    def subject3(self):
        self.ScMarkSub3 = (((int(self.VisSub3) + int(self.EduProgSub3)) / 2) * 0.7) + int(self.ExamSub3)     #Кінцевий бал предмент №3
        self.LitMarkValueSub3 = EducationalProgres.literalValue(self.ScMarkSub2, '')          # Буквений загальний бал за предмет №3
        return self.ScMarkSub3

    def subject4(self):
        self.ScMarkSub4 = (((int(self.VisSub4) + int(self.EduProgSub4)) / 2) * 0.7) + int(self.ExamSub4)     #Кінцевий бал предмент №4
        self.LitMarkValueSub4 = EducationalProgres.literalValue(self.ScMarkSub4, '')          # Буквений загальний бал за предмет №4
        return self.ScMarkSub4

    def averageMark(self):
        self.avemark = (EducationalProgres.subject1(self) + EducationalProgres.subject2(self) + EducationalProgres.subject3(self) + EducationalProgres.subject4(self)) / 4
        return self.avemark

class Student(Human):
    #def __init__(self, sID, gb):
    #    self.studentID = sID            #Номер студентського
    #    self.gradebook = gb             #Залікова книжка

    def studID(self):
        self.studentID = self.surname[0] + self.name[0] + self.persontaxid                      #Номер студентського
        return self.studentID

    def grbook(self):
        self.gradebook = Human.pib(self) + "\n " + "bithdate " + self.birthdate + "\n " + self.studentID          #Чія залікова книжка
        return self.gradebook

class GradeBook(Student, EducationalProgres):
    def print(self):
        self.p1 = (' First page ' + Student.grbook(self))
        self.p2 = ('\n Subject page')
        self.p3 = ("\n " "№1" + " | " + self.EduName1 + " | " + self.EduType1 + " | " + str(EducationalProgres.subject1(self)) + " | " + self.LitMarkValueSub1)
        self.p4 = ("\n " "№2" + " | " + self.EduName2 + " | " + self.EduType2 + " | " + str(EducationalProgres.subject2(self)) + " | " + self.LitMarkValueSub2)
        self.p5 = ("\n " "№3" + " | " + self.EduName3 + " | " + self.EduType3 + " | " + str(EducationalProgres.subject3(self)) + " | " + self.LitMarkValueSub3)
        self.p6 = ("\n " "№4" + " | " + self.EduName4 + " | " + self.EduType4 + " | " + str(EducationalProgres.subject4(self)) + " | " + self.LitMarkValueSub4)
        self.p7 = ("\n " + "Average Balll: "+ str(EducationalProgres.averageMark(self)))
        self.p = str(self.p1) + str(self.p2) + str(self.p3) + str(self.p4) + str(self.p5) + str(self.p6) + str(self.p7)
        return self.p

