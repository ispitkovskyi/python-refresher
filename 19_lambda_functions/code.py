def add(x, y):
    return x + y


print(add(5, 7))

# -- Written as a lambda --

add = lambda x, y: x + y  # lambdas are designed to return values, so you do NOT need to explicitly specify 'return', it returns result of 'x + y' by default
print(add(5, 7))
print((lambda x, y: x + y)(5, 7)) # such format is rarely used, because of its ambiguity

# Four parts
# lambda
# parameters
# :
# return value

# Lambdas are meant to be short functions, often used without giving them a name.
# For example, in conjunction with built-in function map
# map applies the function to all values in the sequence


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
# doubling using 'list comprehension'
doubled = [
    double(x) for x in sequence
]  # Put the result of double(x) in a new list, for each of the values in `sequence`
print(doubled)

# doubling using 'map' function
# map goes over each value in the sequence and applies the 'double' function to each element
doubled = map(double, sequence)
print(list(doubled))

# -- Written as a lambda --

sequence = [1, 3, 5, 9]

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))

# -- Important to remember --
# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name.
