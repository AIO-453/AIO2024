# Câu hỏi 5a:
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self . _name = name
        self . _yob = yob

    def get_yob(self):
        return self . _yob

    @abstractmethod
    def describe(self):
        pass


class Student (Person):
    def __init__(self, name: str, yob: int, grade: str):
        # Your Code Here
        super().__init__(name, yob)
        self._grade = grade
    # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Name : {self._name} - yob : {self._yob} - grade : {self._grade}")
    # End Code Here


if __name__ == '__main__':
    student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
    assert student1 . _yob == 2011
    student1 . describe()
