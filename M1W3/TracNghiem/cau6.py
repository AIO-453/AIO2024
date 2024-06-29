# Câu hỏi 6:b
from abc import ABC, abstractmethod


class Person (ABC):
    def __init__(self, name: str, yob: int):
        self . _name = name
        self . _yob = yob

    def get_yob(self):
        return self . _yob

    @abstractmethod
    def describe(self):
        pass


class Teacher (Person):
    def __init__(self, name: str, yob: int, subject: str):
        # Your Code Here
        super().__init__(name, yob)
        self._subject = subject
    # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Name : {self._name} - yob : {self._yob} - subject : {self._subject}")
    # End Code Here


if __name__ == '__main__':
    teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
    assert teacher1 . _yob == 1991
    teacher1 . describe()
