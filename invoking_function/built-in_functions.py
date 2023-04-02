# In the python 3.8 version currently, the number of  built-in functions amounts to 69.
# str(), int(), float()
# round(), sum(), min(), max()
# type(), len()

# len()  counts the number of characters in the string, or any sequence (i.e. list, tuple, range, byte sequences, byte arrays.)
number = "888888"
print(len(number))  # 6

# Converting types
integer = int(number)  # 888888
float_number = float(number)  # 888888.0

# Adding numbers
my_sum = sum((integer, float_number))
print(my_sum)  # 1777776.0
print(round(my_sum))  # 1777776

# Finding the minimum and maximum values
print(min(integer, my_sum))  # 888888
print(type(max(integer, my_sum)))  # 1777776.0

# min() and max() help you to sort in alphabetical order.
min("alpha", "omega")  # "alpha"
max("alpha", "omega")  # "omega"

# help()
# Help function give you informations about the function.
help(len) 
# Help on built-in function len in module builtins:
#
# len(obj, /)
#    Return the number of items in a container.