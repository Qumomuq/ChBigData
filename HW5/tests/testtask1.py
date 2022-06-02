import datetime
from HW5.task1 import Homework, Teacher, Student

expired_hw = Homework('calculate', 0)
actual_hw = Homework('read', 5)
student = Student('Roman', 'Petrov')
teacher = Teacher('Daniil', 'Ivanov')


class TestHomework:
    def test_hw_attributes(self):
        print('testing HomeWork attributes')
        assert expired_hw.text == 'calculate'
        assert actual_hw.deadline == datetime.timedelta(5)

    def test_hw_is_active_method(self):
        print('testing HomeWork "is_active" method')
        assert expired_hw.is_active() is False
        assert actual_hw.is_active() is True


class TestTeacher:
    def test_teacher_attributes(self):
        print('testing Teacher attributes')
        assert teacher.first_name == 'Daniil'
        assert teacher.last_name == 'Ivanov'

    def test_teacher_create_hw_method(self):
        print('testing Teacher "create_hw" method')
        assert teacher.create_homework("do something", 5).text == 'do something'


class TestStudent:
    def test_student_attributes(self):
        print('testing Student attributes')
        assert student.first_name == 'Roman'
        assert student.last_name == 'Petrov'

    def test_student_do_hw_method(self):
        assert student.do_homework(expired_hw) is None
        assert student.do_homework(actual_hw) is actual_hw