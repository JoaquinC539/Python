# String data type

# Literal assignment
import math
first = "Dave"
last = "Bob"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = first+" " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting a number into a string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the "+decade+"s."
# print(statement)

# Multiple lines
multiline = '''
# Hey, how are you?

# I was just checking in.
#                     All good?


 '''
# print(multiline)

# Escaoing special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                 "
multiline = "               "+multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Cofee".ljust(16, ".")+"$1".rjust(4))
print("Muffin".ljust(16, ".")+"$2".rjust(4))
print("Cheesecake".ljust(16, ".")+"$4".rjust(4))

print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])


# Some method return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))


# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for number
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Creating a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
