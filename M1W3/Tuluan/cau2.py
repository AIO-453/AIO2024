# 2
class person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        print(f"Name : {self.name} - yob : {self.yob}")


class student(person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Name : {self.name} - yob : {self.yob} - grade : {self.grade}")


class teacher(person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Name : {self.name} - yob : {self.yob} - subject : {self.subject}")


class doctor(person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Name : {self.name} - yob : {self.yob} - specialist : {self.specialist}")


class ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        for i in self.people:
            i.describe()
        # print(self.people)

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers = [
            person.yob for person in self.people if isinstance(person, teacher)]
        if teachers:
            return sum(teachers) / len(teachers)
        return 0


if __name__ == '__main__':
    # a
    student1 = student(name="studentA", yob=2010, grade="7")
    student1 . describe()
    teacher1 = teacher(name="teacherA", yob=1969, subject=" Math ")
    teacher1 . describe()
    doctor1 = doctor(name="doctorA", yob=1945, specialist=" Endocrinologists ")
    doctor1 . describe()
    # b
    print()
    teacher2 = teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor2 = doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = ward(name=" Ward1 ")
    ward1 . add_person(student1)
    ward1 . add_person(teacher1)
    ward1 . add_person(teacher2)
    ward1 . add_person(doctor1)
    ward1 . add_person(doctor2)
    ward1 . describe()

    # c
    print(f"\nNumber of doctors : { ward1 . count_doctor ()}")

    # d
    print("\nAfter sorting Age of Ward1 people ")
    ward1 . sort_age()
    ward1 . describe()

    # e
    print(
        f"\nAverage year of birth ( teachers ): { ward1 . compute_average ()}")
