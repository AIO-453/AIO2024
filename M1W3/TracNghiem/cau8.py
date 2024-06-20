# Câu hỏi 8c
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


class Doctor (Person):
    def __init__(self, name: str, yob: int, specialist: str):
        # Your Code Here
        super().__init__(name, yob)
        self._specialist = specialist
    # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Name : {self._name} - yob : {self._yob} - specialist : {self._specialist}")
    # End Code Here


class Ward:
    def __init__(self, name: str):
        self . __name = name
        self . __listPeople = list()

    def add_person(self, person):
        self . __listPeople . append(person)

    def describe(self):
        print(f" Ward Name : { self . __name }")
        for p in self . __listPeople:
            p . describe()

    def count_doctor(self):
        # Your Code Here
        return sum(1 for person in self . __listPeople if isinstance(person, Doctor))
    # End Code Here


if __name__ == '__main__':
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor1 = Doctor(name=" doctorA ", yob=1945,
                     specialist=" Endocrinologists ")
    assert Ward . count_doctor() == 1
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ")
    ward1 . add_person(student1)
    ward1 . add_person(teacher1)
    ward1 . add_person(teacher2)
    ward1 . add_person(doctor1)
    ward1 . add_person(doctor2)
    ward1 . count_doctor()
