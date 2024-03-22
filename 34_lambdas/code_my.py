# Some examples of lambdas

a = 1
b = 2
sum = lambda x, y : x + y
c = sum(a, b)
print(c)


l = [2, 4, 7, 3, 14, 19]
for i in l:
    # create lambda lambda i : (i % 2) == 1 and call it in the same line (lambda i : (i % 2) == 1)(i)
    print((lambda i : (i % 2) == 1)(i))


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