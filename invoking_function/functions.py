# A function is a structured fragment of code we may want to use in more than one place and more than one time.
# Simple function call: multiply(1, 7) --> multiply is the name of the function. (1, 7) are its arguments.
# Arguments will be used inside the function body.

# Let's create our own function
def function_name(parameter1, parameter2):
    # function's body
    return "return value"

# multiply function tkaes two argument and returns their multiplication.
def multiply(x, y):
    return x * y

# Function calls
a = multiply(3, 5)  # 15

# We don't have to pass arguments.
def welcome():
    print("Hello, people!")

# We can also declare a sort of empty function.
# This function does nothing (yet)
def lazy_func(param):
    pass

# Parameters vs Arguments.
# This function is a reusable piece of code, which can be executed with different arguments.
def send_postcard(address, message):
    print("Sending a postcard to", address)
    print("With the message:", message)

send_postcard("Hilton, 97", "Hello, bro!")
# Sending a postcard to Hilton, 97
# With the message: Hello, bro!

# This function takes exactly 2 arguments, so you will not be able to execute it with more or less than 2 arguments:
send_postcard("Big Ben, London")  # TypeError: send_postcard() missing 1 required positional argument: 'message'

def celcius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)

# Convert the boiling point of water
water_bp = celcius_to_fahrenheit(100)
print(water_bp)  # 212.0

# Functions do not necessarily have return values.
# For example print() function doesn't have.
chant = print("I don't know what chant means :)")  # I don't know what chant means :)
print(chant)  # None (None means that called function had nothing to return. The value of chant is None object)

# This function takes a number as an argument and check that if it is even or odd.
def parity(number):
    if number % 2 == 0:
        return "Your number is even"
    return "Your number is odd"
