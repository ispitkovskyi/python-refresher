# A first class function just means that functions can be passed as arguments to functions.
# Functions in python are just "callable" variables

def calculate(*values, operator):
    return operator(*values)    # Call "operator" argument as function


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


# We pass the `divide` function as an argument
result = calculate(20, 4, operator=divide)
print(result)


def average(*values):
    return sum(values) / len(values)


result = calculate(10, 20, 30, 40, operator=average)
print(result)

# -- searching with first-class functions --


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))
# print(search(friends, "Bob Smith", get_friend_name))    # gives error, as there is no "Bob Smith" in the dictionary


# -- using LAMBDAS since this can be simple enough --


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
# Here it is expected, that when the lambda is called it's being passed a dictionary-element from the list above

print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
# print(search(friends, "Bob Smith", lambda friend: friend["name"]))    # gives error, as there is no "Bob Smith" in the dictionary


# -- or as an extra, using built-in functions --

from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(search(friends, "Rolf Smith", itemgetter("name")))
