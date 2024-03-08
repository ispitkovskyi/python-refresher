# Parameters can have default values - such parameters are called 'Optional'
# 'Optional' parameters must go after mandatory parameters.
def add(x, y=3):
    print(x + y)


# 'Optional' parameters must go after mandatory parameters.
def subtract(x=0, y):   # Error
    print(x-y)
