import datetime
from collections import defaultdict


class Human:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Homework:  # Класс принимает текст атрибутов task и time deadline
    # и имеет метод is_active(), который возвращает Boolean, если время выполнения задачи истекло.
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        data = self.created + self.deadline
        return self.created <= data


class HomeworkResult:  # Класс принимает объект( author, принимает исходную задачу
    # и ее решение в виде строки)
    def __init__(self, author: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = datetime.datetime.now()


class DeadLineError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


"""
Student class, accept last_name and first_name attributes,
and have create_homework() method,
that takes task text and integer number of days left for doing this homework, and returns Homework instance
that contains task text and timedelta instance with days left
"""


class Student(Human):
    # Класс Student, принимает атрибуты last_name и first_name
    # и имеет метод create_homework(),
    # который принимает текст задания и целое число дней, оставшихся для выполнения этого домашнего задания, и возвращает экземпляр домашнего
    # задания, содержащий текст задания и экземпляр timedelta с оставшимися днями
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadLineError("You are late")


# Класс учителя, принимает атрибуты last_name и first_name
# и имеет методы:
# create_homework, содержащий текст задачи и количество дней для этой задачи,
# возвращает экземпляр Homework
# check_homework, который проверяет продолжительность домашней работы и, после успешной проверки, добавляет в
# homework_done
# reset_results , который удаляет только результаты этой задачи из homework_done или полностью сбрасывает homework_done
class Teacher(Human):
    homework_done = defaultdict(lambda: [])

    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)

    def create_homework(self, task: str, days_left: int) -> Homework:
        return Homework(task, datetime.timedelta(days_left))

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework.text].append(homework_result)
            return True
        else:
            return False

    def reset_results(self, homework: Homework):
        Teacher.homework_done.pop(homework.text)


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleks', 'ivanov')

    lazy_student = Student('Vladd', 'Chirkov')
    good_student = Student('Ilya', 'Palagin')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
