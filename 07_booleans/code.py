# -- Comparisons --

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False
print(friends is friends)  # True

# `is` keyword checks if two lists are exactly the same thing (probably meaning they are the same piece of memory allocated by python, not checking elements inside)