# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Function with decorator applied
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
