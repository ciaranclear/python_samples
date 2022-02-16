"""
A decorator is a function that takes an other function as an argument
and adds some extra functionality and then returns a function
"""
from functools import wraps


def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function


hi_func = outer_function("hi")
bye_func = outer_function("bye")
hi_func()
bye_func()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper ran before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


def display():
    print("Display function ran")


decorated_function = decorator_function(display)
decorated_function()


@decorator_function
def display2():
    print("Display2 ran")


display2()


@decorator_function
def display_info(name, age):
    print(f"Name is {name} and is {age} years old")


display_info("John",30)


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call method ran before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_info2(name, age):
    print(f"Name is {name} and is {age} years old")


display_info2("Bill", 56)


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args} and kwargs: {kwargs}"
        )
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in {t2} sec")
        return result

    return wrapper


@my_logger
@my_timer
def display_info3(name, age):
    print(f"Name is {name} and is {age} years old")


display_info3("Mark", 32)

