def get_admin_password():
    return "1234"

# This is a DECORATOR. It will create a function and replace the origin function 'func' with a secure one 'secure_function'
def make_secure(func):  # 'get_admin_password' is passed here as 'func'
    def secure_function():  # This is a FUNCTION-DEFINITION inside a function, and it will be returned as result of calling the 'make_secure' func
        if user["access_level"] == "admin":
            return func()    # Returns CALLING (not the function itself) the 'get_admin_password' function, which is "1234"

    return secure_function  # Here we return the function itself (not the function call)


get_admin_password = make_secure(get_admin_password)  # `get_admin_password` is now `secure_function` from above, returned in here from line 11
# NOTE: after line 14 the 'get_admin_password' equals to 'secure_function' func, which wraps the initial 'get_admin_password' (which returns "1234")

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level

# -- More information or error handling --


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
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
