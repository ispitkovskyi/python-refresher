user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


print(get_admin_password())  # Can do this even though I'm a "guest"

# Now this only runs if I'm an admin... but
if user["access_level"] == "admin":
    print(get_admin_password())

print(get_admin_password())  # The function itself is still unsecured

# -- "secure" function --


def secure_get_admin():
    if user["access_level"] == "admin":
        print(get_admin_password())


# Now secure_get_admin() is secure.
# But get_admin_password() is still around, and I could call it:

secure_get_admin()
print(get_admin_password())

# We want to get rid of get_admin_password so that only the secure function remains!
# Maybe something like this?


def secure_function(func):
    if user["access_level"] == "admin":
        return func


user = {"username": "bob", "access_level": "admin"}

get_admin_password = secure_function(get_admin_password)
print(get_admin_password())  # Error!

# When we ran `secure_function`, we checked the user's access level. Because at that point the user was not an admin, the function did not `return func`. Therefore `get_admin_password` is set to `None`.

# We want to delay overwriting until we run the function


def get_admin_password():
    return "1234"

def make_secure(func):  # This is a DECORATOR
    def secure_function():
        if user["access_level"] == "admin":
            return func() #Decorated function returns (if condition is met) a CALL of the func() function. If condition is not met - nothing happens

    return secure_function


get_admin_password = make_secure(get_admin_password)  # `get_admin_password` is now `secure_func` from above

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now, the new "get_admin_password" function is DECORATED, and it checks access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level

# -- More information or error handling --


def get_admin_password():
    return "1234"


def make_secure(func):     # This IS a DECORATOR function
    def secure_function():  # This is NOT a decorator function. It is a function, which REPLACES the decorated one
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


get_admin_password = make_secure(
    get_admin_password
)  # `get_admin_password` is now `secure_func` from above

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level
