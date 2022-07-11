# Exceptions - used when expecting a wrong value or similar


# Handling Exceptions

try:
    age = int(input('enter age:'))
except ValueError:
    print('Dont put non number values')
else:
    print('no exceptions were thrown')


# Handling different exceptions

try:
    age = int(input('enter age:'))
    xfactor = 10/0
# If you have multiple error messages with the same print statemnet u can just make it into one
except (ValueError, ZeroDivisionError):
    print('Not accepted')
else:
    print('no exceptions were thrown')


# Cleaning Up

try:
    file = open("app.py")
    age = int(input('enter age:'))
    xfactor = 10/0
except (ValueError, ZeroDivisionError):
    print('Not accepted')
else:
    print('no exceptions were thrown')
finally:  # Best palce to close files, database connecitons, network connecitons and so on.
    file.close()


# The with statement (similar to finally clause)

try:
    with open("app.py") as file:
        print('File opened.')

    age = int(input('enter age:'))
    xfactor = 10/0
except (ValueError, ZeroDivisionError):
    print('Not accepted')
else:
    print('no exceptions were thrown')


# Raising Exceptions

def calculate_xfactor(value):
    if value <= 0:
        raise ValueError('cannot use 0 or below ')
    return 10/value


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


# Use none when u dont want to implement except clause
