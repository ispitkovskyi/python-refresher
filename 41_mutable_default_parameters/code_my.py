# NOTE: Avoid it by not having mutable parameters. Instead, do what we did in prior lectures:

from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # Better way of handling parameters, which potentially may equal to None
        self.name = name
        self.grades = grades or []  # New list created if one isn't passed (if 'grades' is None)

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.
