def hello():
    print("Hello!")


hello()

# -- Defining vs. calling --
# It's still all sequential!


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")



# -- Don't reuse names --


# def print():
#     print("Hello, world!")  # Error!

# -- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! --
# -- Don't reuse names, it's generally confusing! --
friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    #friends = friends + [friend_name]  # Error, because python creates a local variable "friends" inside the function and you're using the "friends" variable in the same line where it is defined
    f = friends + [friend_name]  # This is correct and will work!  Another way of adding to a list!
    print(f"New list of friends is {f}")


add_friend()
print("Lisf of friends is:", friends)  # Always ['Rolf', 'Bob']
# -- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! --

# Error below, because it tries to use "say_hello" function BEFORE it is defined in the code
# say_hello()
def say_hello():
    print("Hello!")




# -- Remember function body only runs when the function is called --
def add_friend():
    my_friends.append("Wolf")  #Here "my_friends" has not been defined yet, BUT it will be defined below and BEFORE this function is called.


my_friends = []
add_friend()  # At this moment, when the function is called, the 'my_friends' variable has already been defined, so function knows about it when it is called.
add_friend()  # At this moment, when the function is called, the 'my_friends' variable has already been defined, so function knows about it when it is called.
add_friend()  # At this moment, when the function is called, the 'my_friends' variable has already been defined, so function knows about it when it is called.

print(my_friends)  # [Rolf]
