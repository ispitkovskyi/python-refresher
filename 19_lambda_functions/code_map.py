def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

# doubling using 'map' function
# map goes over each value in the sequence and applies the 'double' function to each element
doubled = map(double, sequence)
print(list(doubled))    # Need to wrap return of 'map' to a 'list', because 'map' does not return a list of objects, instead it returns something called 'map object'

# -- Written as a lambda --

sequence = [1, 3, 5, 9]

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))        # Need to wrap return of 'map' to a 'list', because 'map' does not return a list of objects, instead it returns something called 'map object'

# -- Important to remember --
# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name.
