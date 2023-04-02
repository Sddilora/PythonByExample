list = ['dilo', 123, 1.2, "john"]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# All the elements are printed in the same order as they were stored in the list because lists are ordered.
# Simple list that stores several names of dogs' breeds:
dog_breeds = ['corgi', 'labrador', 'poodle', 'jack russell']
print(dog_breeds)  # ['corgi', 'labrador', 'poodle', 'jack russell']

# Another way to create a list is to invoke the list function.
# It is used to create a list out of an iterable object:
list_out_of_string = list('danger!')
print(list_out_of_string)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

list_out_of_integer = list(235)  # TypeError: 'int' object is not iterable

# The difference between the list function and creating a list using square brackets:
multi_element_list = list('danger!')
print(multi_element_list)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

single_element_list = ['danger!']
print(single_element_list)  # ['danger!']

# The square brackets and the list function can also be used to create empty lists.
# We can fill them later
empty_list_1 = list()
empty_list_2 = []

# Lists can store duplicate values as many time as needed.
on_off_list = ['on', 'off', 'on', 'off']
print(on_off_list)  # ['on', 'off', 'on', 'off']

# Lists can contain different types of elements, including other lists.
different_objects = ['a', 1, [1, 2, 3]]
print(len(different_objects))  # 3
