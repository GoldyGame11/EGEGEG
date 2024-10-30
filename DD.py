class StudySubject:
    def __init__(self, name: str, hours: int, enable: bool):
        self.name = input('name ')
        self.hours = input('hours ')
        self.enable =input('accept? ')

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')

python = StudySubject(name='Python', hours=18, enable=True)
# python.info_study()

class Student:
    def __init__(self):
        self.name = input('name: ')
        self.surname = input('surname: ')

        self.study = StudySubject()

    def info_student(self):
        print(f'Student: {self.name} | Surname: {self.surname}')

    def info_all(self):
        self.info_student()
        self.study.info_study()


student = Student()
student.info_all()

