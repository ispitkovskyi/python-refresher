student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))

# But wouldn't it be nice if we could...
# print(student.average()) ?


# IMPORTANT: the '__init__' method is used to CREATE INSTANCE of a class
class Student:
    # When instance of the class is created, python automatically calls __init__ and creates and empty "self"
    # The "self" - is actually an object of Student, so you can operate with created instance inside the class code
    def __init__(self):
        self.name = "Rolf"  # AUTOMATICALLY creates 'name' inside 'self' here and assign "Rolf" value to it
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student() # Here python returns 'self' of the created Student instance
print(student.average())
# Identical to Student.average(student)


# -- Parameters in __init__ --


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (36, 67, 90, 100, 100))
print(student.average())

# -- Remember *args ? --


class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", 36, 67, 90, 100, 100)
print(student.average())
