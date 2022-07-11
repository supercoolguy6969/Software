# Functions
def greet():
    print("Hello ther")
    print("Welcome")


greet()


# Arguments
def meet(first_name, last_name):     # Parameters - input defined
    print(f"Hello {first_name} {last_name}")
    print("Welcome")


meet('Ankar', 'Ahmat')              # Arguments - values to the inputs


# Types of functions
# 1 -  Perform a task
# 2 - Return a value
# All functins by default return none (absence of a value) unless u specifically return a value

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting('Ankar')

print(message)


# Keyword Arguements

def increment(number, by):  # We can make by=1 to make the value fixed, ofc it can be changed with the arugment down below
    return number + by


print(increment(2, by=1))  # Using by to make it easier to read


# xargs

def multiply(*numbers):   # numbers is collection of arguments
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 5, 6))


# **args

def save_user(**user):    # user object is a dictionary
    print(user["id"])


save_user(id=8, name='john', age=33)


# Debugging


# Exercise
def fizz_buzz(input):
    if (input % 3 == 0 and input % 5 == 0):
        return 'fizzbuzz'
    elif (input % 3 == 0):
        return 'fizz'
    elif(input % 5 == 0):
        return 'buzz'

    else:
        return input


print(fizz_buzz(15))
