# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code if no errors were raised. 
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

### Exception Handling
# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occurred")  # An exception occurred ((Because x is undefined))

### Many Exceptions
# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")  # Variable x is not defined
except:
    print("Something else went wrong")

### Else
# We can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")  # Nothing went wrong

### Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")  # Something went wrong
finally:
    print("I'm independent!")  # I'm independent!

# Finally is used to close objects and clean up resources, even if there is an error.
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")  # Something went wrong when writing to the file
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
# The program can continue, without leaving the file object open

### Raise an exception
# We can choose to throw an exception if a condition occurs.
# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")  # Traceback (most recent call last): File "try-except.py", line 70, in <module> raise Exception("Sorry, no numbers below zero") Exception: Sorry, no numbers below zero

# We can define what kind of error to raise, and the text to print to the user.
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")  # Traceback (most recent call last): File "try-except.py", line 76, in <module> raise TypeError("Only integers are allowed") TypeError: Only integers are allowed