# Comparison Operators
'''10 > 3
10 >= 3 
10 <= 20
10 < 20
10 != "10"
10 == 10 '''


# Conditional Statements
temperature = 15
if temperature > 30:
    print("It's warm outside")
elif temperature < 15:
    print("It's cold outside")
else:
    print("It's ok")

print("This will get printed either way")


# Ternary Operator
age = 15
if age > 18:
    print("Eligible")
else:
    print("Not eligible")

'''Method below is simpler'''

message = 'Eligible' if age > 18 else 'Not eligible'
print(message)


# For Loops - to create repetitions
for number in range(3):
    print("Attempt", number, number * ".")

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * '.')


# For...Else
succesful = True
for number in range(3):
    print("Attempt")
    if succesful:
        print("Succesful")
        break  # breaks out of the whole loop

'''Opposite shown below '''

succesful = False
for number in range(3):
    print("Attempt")
    if succesful:
        print("Succesful")
        break
else:
    print("Attempted three times and failed")


# Nested Loops
for x in range(5):
    for y in range(3):
        print(f'({x},{y})')


# Iterables

for items in "Python":
    print(items)


# While Loops - Evalute condition and repeat task
command = ''
while command.lower() != 'quit':
    command = input('>')
    print("Echo", command)

'''OR BELOW '''

while True:
    command = input('>')
    print('Echo', command)
    if command.lower() == "quit":
        break  # Must include this or else it will run forever


# EXERCISE
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'We have {count} even numbers')
