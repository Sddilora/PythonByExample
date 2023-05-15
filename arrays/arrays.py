# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# This module will demonstrate how to use Python Lists as Arrays.
# Arrays are used to store multiple values in one single variable:

animals = ["Cat", "Dog", "Fox"]

# Access the Elements of an Array
# We refer to an array element by referring to the index number.
# Get the value of the first array item:
x = animals[0]
print(x)

# Modify the value of the first array item:
animals[0] = "Lion"

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
x = len(animals)

# Looping Array Elements
# We can use the for in loop to loop through all the elements of an array.
for x in animals:
  print(x, ", has index",animals.index(x))

# Adding Array Elements
# We can use the append() method to add an element to an array.
animals.append("Tiger")

# Removing Array Elements
# We can use the pop() method to remove an element from the array.
animals.pop(0)

# We can also use the remove() method to remove an element from the array.
# Note: The list's remove() method only removes the first occurrence of the specified value.
animals.remove("Dog")

print(animals)  # ['Fox', 'Tiger']