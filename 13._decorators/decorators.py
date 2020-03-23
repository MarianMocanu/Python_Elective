# Functions are first class functions
# Functions can take other functions as parameters
# Functions can return functions as return values

def my_first_class_function(x):
    return x
    
# def greet():
#     return "Hello"

# inner functions
def foo():

    #declare
    def inner():
        return "Hello from inner"
    
    return inner

# simple decorator
def my_decorator(function):
    def wrapper(*args):
        print("This is before function execution")
        function(*args)
        print("This is after function execution")
    
    return wrapper

# @my_decorator
# def greet():
#     print("Hello")

# @my_decorator
# def greet(name):
#     print(f'Hello {name}')

@my_decorator
def greet2(name, age):
    print(f'Hello {name}, {age}')

def me_2_decorator(function):
    def wrapper(*args):
        x = "before execution"
        x += function(*args)
        x += "after execution"
        return x

    return wrapper

@me_2_decorator
def greet(name):
    return f'Hello {name}'