# VSCODE shorcuts

# fn right/left - to move to all the way to the right/left
# option up/down - move the line up/down
# cmd / - comment or undo comment
# u can abreviate common functions - multiply to mtp (or to anythig that has the letters)


# Lists

from array import array
from collections import deque


Letters = ["a", "b", "c"]
matrix = [[0, 1], [1, 2]]
zeros = [0] * 5
combined = zeros + Letters
print(combined)
chars = list(range(20))
print(chars)
numbers = list('Hello World')
print(numbers)

# Lists unpacking
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *others = numbers
print(first, second)
print(others)

# Loop over lists
letters = ["a", "b", "c"]
for letter in enumerate(letters):  # gives index, give us a tuple in each iteration
    print(letter)


""" We can also unpack the tuple"""

lett = ['a', 'b', 'c']
for index, lett in enumerate(lett):
    print(index, lett)


# Adding/removing items

# Adding
letters.append('b')  # everythin in python is an object
letters.insert(0, '-')
print(letters)

# Removing
letters.pop(0)
letters.remove('b')
del letters[0:3]
letters.clear()
print(letters)


# Sorting Lists
numbers = [3, 52, 6, 22, 1, 12]
numbers.sort()  # sorts the number in ascending order, to mkae it descending order use numbers.sort(reverse=True)
print(numbers)


"""we can also use sorted funciton"""

print(sorted(numbers, reverse=True))  # returns a new sorted list
print(numbers)


"""Applicaito for processing orders"""

items = [("Product", 9),
         ("Product", 11),
         ("Product", 8),

         ]


def sort_item(item):
    return item[1]


# Uses key cause it is keyword arugment not positional arugment
items.sort(key=sort_item)
print(items)


"""Better to implmeent the function using lamba expression"""


items.sort(key=lambda item: item[1])  # Parameters:Expression
# with lambda funciton, we dont have to delcare a fn as we did here
print(items)


# Map Functions - executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

items = [("Product", 9),
         ("Product", 11),
         ("Product", 8),

         ]


prices = []
for item in items:
    prices.append(item[1])

"""Map funciton does the same thing """

x = map(lambda item: item[1], items)
print(x)
for item in x:
    print(item)

# Map object can be turned into list
price = list(map(lambda item: item[1], items))
print(price)

print(prices)


# Filter Funciton - returns an iterator where the items are filtered through a function to test if the item is accepted or not.

items = [("Product", 9),
         ("Product", 11),
         ("Product", 8),

         ]


filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


# List comprehensions - ez way instead of map or filter funcitons

items = [("Product", 9),
         ("Product", 11),
         ("Product", 8),

         ]
price = list(map(lambda item: item[1], items))
price = [item[1] for item in items]  # [expression for item in items ]


filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]

print(price)
print(filtered)


# Zip funcitons
list1 = [1, 20, 3]
list2 = [3, 9, 69]

print(list(zip(list1, list2, 'abc')))  # zip function adds lists


# Stacks - like putting books on top of each other, LIFI - last in first out in that order

browsingsession = []
browsingsession.append(1)  # adds item
browsingsession.append(2)
browsingsession.append(3)
last = browsingsession.pop()  # removes item
print(last)
print(browsingsession)
if not browsingsession:
    print("disable bc backspace cause it's exmpty")
# get the item that is on top of stack
print('redirect is', browsingsession[-1])


# falsy items give boolean false - 0, '', []
# We can use           not [] to get boolean tru


# Queues - que of ppl in a resturant, first person in que gets in, FIFO - first in first out
# deque object
# modules - buckets with reusuable code
# from collections (module) import deque (class)

que = deque([])
que.append(1)
que.append(2)
que.append(3)
que.append(4)
print(que)
que.popleft()
print(que)

if not que:
    print('no more ques')


# Tuples - read only list (cant do anythign to it)

point = 1, 2
point = (1, 2) + (1, 2)
print(type(point))
print(point)
print(tuple([1, 2]))


# Swapping Variables

x = 10
y = 11

z = x
x = y
y = z

"""OR the following below """

x, y = y, x                             # This is a tuple so this unpacks
a, b = 1, 2

print('a is ', a)
print('b is ', b)


print('x is ', x)
print('y is ', y)

# Array - dealing iwth large sequence of numbers and encounter performance problems

# from array import array
numbers = array('i', [1, 2, 3])
numbers.append(4)
print(numbers)


# Sets - colleciton with no duplicates
numbers = [1, 2, 2, 4, 5]
first = set(numbers)
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:     # cant use index to access sets
    print('yes')


# Dictionaries - colleciton of key-value pairs, use it to map a key to a value like (e.g map phone number (value) to person name(key))

point = {"x": 1, "y": 2}    # key must be immutable, value can be any type
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if a in point:
    print(point['a'])
print(point)
# OR
print(point.get("a", 0))  # If no key a then return 0

del point['x']
print(point)


for key in point:
    print(key, point[key])

"""another way to iterate"""
for x in point.items():  # tuple
    print(x)


for key, value in point.items():  # unpack
    print(key, value)


# Dictionary Comphresshions

values = []
for x in range(5):
    values.append(x*2)

print(values)

"""Instead of doing that we can do below and achieve same results"""

# [expression for .. in ..], not limited to lists can also with sets and dictionaries
valu = [x*2 for x in range(5)]
print(valu)

val = {x*2 for x in range(5)}  # Dict - key-value pairs separted by colons
print(val)

va = {x: x*2 for x in range(5)}   # Dict comprehension
print(va)


# Generator Expressions


# Unpacking

values = [1, 2, 3]
print(values)
print(*values)   # * - is the unpacking operator, ... - is one for javascript

list = [1, 32, 3]
values = [*'hello', *list]
print(values)

first = {'x': 10}
second = {'x': 1, 'y': 2}
combined = {**first, **second, 'z': 2}
print(combined)


# Excercise
sentence = 'This is a common interview question'


# My solution
# Must find the most repeated letter

word = [*sentence]
count = 0
for x in word:
    if x == 'i':
        count += 1

print(count)


# Solution

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] = + 1
    else:
        char_frequency[char] = 1

print(char_frequency)
