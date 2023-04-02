# To access an element of a list by its index, we need to use square brackets. "[]"
colors = ["red", "blue", "black"]
first_elem = colors[0]
second_elem = colors[1]

# Strings work in the same way
pet = "dog"
first_char = pet[0]  # 'd'

# We'll get an error if we try to acces an element with a non-existing index.(IndexError)
print(colors[3])  # IndexError: list index out of range

# We can change the elements in a "list".
colors[1] = "violet"

# Strings doesn't have this feature.
pet[1] = "L" # TypeError: 'str' object does not support item assignment.

# Negative Indexes
# The easier way to access the elements at the end of a list.
# Remember that we are starting to count from -1 not zero from right to left.
last_elem = colors[-1]
first_elem = [-len(colors)]

last_char = pet[-1]
first_char = pet[-3]
