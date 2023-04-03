# To load a module, just use an import statement. In its basic form, it has the following syntax: import module.
import calendar

day = calendar.weekday(2023, 4, 3)  # calling a function defined in super_module

print(day)  # accessing a variable defined in super_module

# It's also common to only import the required functions or variables from a module but not the module itself.
# We can do this by using from in the import statement.
from binascii import a2b_base64

str_byte = a2b_base64("dilo")
print(str_byte)  # b'v)h' (The b prefix before the string indicates that it is a bytes object in Python.)

decoded_str = str_byte.decode('utf-8')
print(decoded_str)  # v)h

# Wildcard Import:
# A special form of import statement allows you to load all the names defined in a module.
# Has the syntax "from calendar import *".
# Avoid that it may cause so many problems.
