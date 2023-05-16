# The string module contains common string operations and constants.
from string import digits

print(digits)  # prints all the digit symbols

# The random module provides functions that let us make a random choice.
from random import choice

print(choice(['red', 'green', 'yellow']))  # print a random item from the list

# Import and use the platform module.
import platform

x = platform.system()
print("system",x)  # system Windows

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# List all the defined names belonging to the choice module:
x = dir(choice)
print(x)  # ['__call__', '__class__', '__delattr__',...]

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)  # 5
print(y)  # 25

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)  # 7.25

# The pow(x, y) function returns the value of x to the power of y (x^y).
x = pow(4, 3)  # 4 to the power of 3 (same as 4 * 4 * 4)
print(x)  # 64
