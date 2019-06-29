# https://www.programiz.com/python-programming/exception-handling

import sys

random_list = ['a', 0, 2]

for entry in random_list:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry...")
        print()

print("The reciprocal of", entry, "is", r)

# Catching Specific Exceptions in Python

for entry in random_list:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except ValueError:  # single exception
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry...")
        print()
    except (TypeError, ZeroDivisionError):  # multiple exceptions
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry...")
        print()

print("The reciprocal of", entry, "is", r)

# Raising Exceptions
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
