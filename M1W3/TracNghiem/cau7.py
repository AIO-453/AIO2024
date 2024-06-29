# Câu hỏi 7a:
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


if __name__ == '__main__':
    doctor1 = Doctor(name=" doctorZ2023 ", yob=1981,
                     specialist=" Endocrinologists ")
    assert doctor1 . _yob == 1981
    doctor1 . describe()