# SUMMARY IMPORTANT!!!
# when '*' used with argument inside function DEFINITION - it means number of input arguments will be COLLECTED INTO A TUPLE of values
# when '*' used with argument inside a function CALL - it means that arguments will be UNPACKED to separate values before passing them into the called function


# Example when FUNCTION COLLECTS ARGUMENTS INTO TUPLE, but function is called passing UNPACKED SEPARATED VALUES
def multiplyPacked(*args):    # function WILL COLLECT input values into a TUPLE
    print(f"debug: {args}")
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiplyPacked(*args) # Pass UNPACKED SEPARATE values
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))

print('---------------------------------------------------------------------------------')

# Example when FUNCTION ACCEPTS SEPARATE ARGUMENTS, but function is called passing VALUES PACKED INTO TUPLE
def multiplySeparateValues(args):    # function WON'T try to collect input to a TUPLE
    print(f"debug: {args}")
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply2(*args, operator):
    if operator == "*":
        return multiplySeparateValues(args) # Pass TUPLE of values 'args'
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply2(1, 3, 6, 7, operator="+"))
print(apply2(1, 3, 6, 7, operator="*"))

