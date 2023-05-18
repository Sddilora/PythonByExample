b = "Hello World!"
print(b)

str = 'Hello World'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5]    ) # Prints characters starting from 3rd to 5th
print (str[2:]     ) # Prints string starting from 3rd character
print (str * 2     ) # Prints string two times
print (str + "TEST") # Prints concatenated string

### String Formatting
# The format() method allows us to format selected parts of a string.
# To control values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # Output: My name is John, and I am 36

# we can add parameters inside the curly brackets to specify how to convert the value:
# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(49.123))  # Output: The price is 49.12 dollars

# Multiple Values
# If we want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))  # Output: I want 3 pieces of item 567 for 49.95 dollars

# Index Numbers
# We can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
myorder = "I want to pay {2:.2f} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  # Output: I want to pay 49.95 dollars for 3 pieces of item 567.

# Also we can refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))  # Output: His name is John. John is 36 years old.

# Named Indexes
# We can also use named indexes by entering a name inside the curly brackets {carname},
# but then we must use names when we pass the parameter values txt.format(carname = "Ford"):
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))  # Output: I have a Ford, it is a Mustang.
