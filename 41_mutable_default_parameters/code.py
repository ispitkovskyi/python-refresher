from typing import List

# NOTE: NEVER make a parameter equal to a MUTABLE default value
# This happens, because DEFAULT values of the function parameters are evaluated, when the function is DEFINED, not when the function is called,
# So, when the class is created, DEFAULT values of this function are evaluated, and the default value is created.
# NOTE: This means, that ALL created instances if this class will share/use the SAME LIST used as default value of the 'grades' parameter
class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Whaaaaaat!?!?!?!?!?!?

# The function parameters evaluate when the function is defined, not when it runs.
# That means that self.grades is a name for the list that was evaluated when the function was defined.
# We're then modifying it in take_exam
# But all calls to the __init__ method have the same list (because parameters are only evaluated once!)
# So all students have the same list

# NOTE: Avoid it by not having mutable parameters. Instead, do what we did in prior lectures:

from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []  # New list created if one isn't passed (if 'grades' is None)

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.
