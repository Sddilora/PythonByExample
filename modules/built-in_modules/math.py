# Python has a math module that provides access to mathematical functions.
# The math module has a set of methods and constants.
import math as m

print(m.factorial(5))  # prints the value of 5!
print(m.log(10))  # prints the natural logarithm of 10

print(m.pi)  # math also contains several constants.
print(m.e)

# sqrt() method returns the square root of a number
x = m.sqrt(64) 
print(x)  # 8.0

# The math.ceil() method rounds a number upwards to its nearest integer,
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
x = m.ceil(1.4)  # returns 2
y = m.floor(1.4)  # returns 1
