def multiply(*args):        # all arguments will be collected in a tuple 'args' !!!!!!!!
    print(f"debug: {args}")
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(3, 5))
print(multiply(-1))

# The asterisk takes all the arguments and packs them into a tuple.
# The asterisk can be used to unpack sequences into arguments too!


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])

# -- Uses with keyword arguments --
# Double asterisk packs or unpacks keyword arguments


def add(x, y):
    return x + y


nums = {"y": 25, "x": 15} # dictionary used as argument

print(add(**nums))  # NOTE! use double-asterisk '**' to pass dictionary as named arguments

# -- Forced named parameter --


def multiply(*args):    # in line 50 this function is called passing tuple as argument into this func
    print(f"debug: {args}")
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # need to UNPACK the 'args' here into 4 separate values. Otherwise, if we DON'T use '*' to unpack the 'args' tuple here, it'll pass a TUPLE OF VALUES taken from the *args argument into 'multiply' function.
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="+"))
# print(apply(1, 3, 5, "+"))  # Error - because 'apply' has packed arguments first, you MUST specify 'operator' argument as NAMED at the end (like line above)
print(apply(1, 3, 6, 7, operator="*"))

# SUMMARY
# when '*' used with argument inside function definition - it means number of input arguments will be COLLECTED INTO A SINGLE TUPLE of values
# when '*' used with argument inside a function call - it means that arguments will be UNPACKED to separate values before passing them into the called function