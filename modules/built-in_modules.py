# Python has a math module that provides access to mathematical functions.
import math as m

print(m.factorial(5))  # prints the value of 5!
print(m.log(10))  # prints the natural logarithm of 10

print(m.pi)  # math also contains several constants.
print(m.e)

# The string module contains common string operations and constants.
from string import digits

print(digits)  # prints all the digit symbols

# The random module provides functions that let you make a random choice.
from random import choice

print(choice(['red', 'green', 'yellow']))  # print a random item from the list
