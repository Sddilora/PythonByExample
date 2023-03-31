a = 85
print(a)
# We don't indicate the variables type so if we wanna check this will print the variables type
print (type(a)) # <class 'int'>

float(a)
print (type(a))

d = 1.0
print(type(d)) # <class 'float'>

#Python allows you to assign a single value to several variables simultaneously
#All three variables are assigned to the same memory location.
e = f = g = 1

#You can also assign multiple objects to multiple variables.
h, i, j = 1, 2, "Dilo"
