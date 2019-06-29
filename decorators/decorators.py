import math
import time


# decorator to calculate duration taken by any function
def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()

        print("Total time taken in: ", func.__name__, end - begin)

    return inner


@calculate_time
def factorial(num):
    # time.sleep(2)
    print(math.factorial(num))


# factorial(100000)


# What if a function returns something...
def hello_decorator(func):
    def inner(*args, **kwargs):
        print("Bebore execution")

        returned_value = func(*args, **kwargs)

        print("After execution")

        return returned_value
    return inner


@hello_decorator
def sum_to_numbers(a, b):
    print("Inside the function")
    return a + b

x, y = 1, 2

print("Sum =", sum_to_numbers(x, y))


def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner1


@hello_decorator
def function_to_be_used():
    print("This is inside the function!")
