user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()           # NOTE: Name of a wrapped 'func' function here is changed to 'secure_function'
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


# @make_secure prevents "get_admin_password" from being created "as is",
# but will be possible to create and pass it only via the 'make_secure' decorator
# IMPORTANT NOTE: Whenever you call get_admin_password(), it actually makes make_secure(get_admin_password) call. Basically it's used instead of "get_admin_password = make_secure(get_admin_password)".
@make_secure
def get_admin_password():
    return "1234"

print("Now you do NOT need to call 'make_secure' decorator to secure 'get_admin_password', "
      "you can just call directly 'get_admin_password' and it will be passed through the 'make_secure decorator because the 'at syntax' is used' "
      "the annotation @make_secure will do decoration automatically")
# get_admin_password = make_secure(get_admin_password)   # NOT NEEDED ANYMORE due to @make_secure annotation
print(f"Name of wrapped function is now {get_admin_password.__name__}")
print(get_admin_password())