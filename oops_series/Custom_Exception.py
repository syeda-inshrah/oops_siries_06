# Custom Exception
class InvalidAgeError(Exception):
    pass

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Age is valid.")


try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Caught an error: {e}")
