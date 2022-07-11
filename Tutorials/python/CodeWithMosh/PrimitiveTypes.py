import math


# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

courses = "Python \"Programming\" "  # escape sequence
print(courses)

# \"  \'  \\   \n

# Formatted Strings
first = "Ankar"
last = "Ahmat"
full = F"{first} {last}"
print(full)

# String Methods
cours = "Python Programming"
print(cours.lower())
print(cours.upper())
print(cours.title())
print(cours.strip())  # makes it like a title
print(cours.find("Pro"))
print(cours.replace("p", "j"))
print("pro" in course)

# Numbers
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)  # modulus
print(10**3)  # exponent


x = 10
x = x+3
x += 3

# Working with Numbers

print(round(2.6))
print(abs(-2.8))

print(math.ceil(2.2))

# Type Conversions
x = input("x is ")
y = int(x) + 1
print(f"x:{x} y:{y}")
