class WeakPasswordError(Exception):
    pass
def validate_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 6 characters long.")
    print("Password accepted.")
try:
    pwd = input("Create a password: ")
    validate_password(pwd)

except WeakPasswordError as e:
    print("Custom Error:", e)
