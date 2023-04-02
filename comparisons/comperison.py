# Comparison or relation operations let you compare two values and determine the relation between them.
# There are ten comparison operators in Python:
# <, <=, >, >=, ==, !=
# is(object identity), is not(negated object identity)
# in(membership), not in(negated membership)
# The result of applying these operators is always "bool".
 
a = 5
b = -10
c = 15

result_1 = a < b   # False
result_2 = a == a  # True
result_3 = a != b  # True
result_4 = b >= c  # False

# Any expression that returns an integer is a valid comparison operand too:
calculated_result = a == b + c

# Comparison operations can be joint with logical operators.
logical_result = b < a and a <= c  # True and True --> True

# In Python, there is a way to write complex comparisons. It's called "chaining".
chain = b < a <= c  

# Comparison chaining should be use carefully.
a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

print(b + c <= e or f + g >= e == f == 5)      # False
print((b + c <= e or f + g >= e) == (f == 5))  # (True) = (True) so result is True

# If there is a "logical" and "arithmetic" part in an expression, we might see unusual behavior,
# Due to logical operators in Python being short-circuited, or lazy.
a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

# True and-expressions return the result of the last operation:
print((b + c * f >= e) and ((f + g) * c))  # (17 >= 4 is True) and 33 -> 33
print(((f + g) * c) and (b + c * f >= e))  # 33 and (17 >= 4 is True) -- > True

# False and-expressions return a boolean False value:
print((b + c * f <= e) and ((f + g) * c))  # (17 <= 4 is False) and 33 --> False
print(((f + g) * c) and (b + c * f <= e))  # 33 and (17 <= 4 is False) --> False

# True or-expressions return the result of the first operation:
print((b + c * f >= e) or ((f + g) * c))  # (17 >= 4 is True) or 33 --> True
print(((f + g) * c) or (b + c * f >= e))  # 33 or (17 >= 4 is True) --> 33

# True-False or-expressions return the True part:
print(((f + g) * c) or (b + c * f <= e))  # 33 or (17 <= 4 is False) --> 33
print((b + c * f <= e) or ((f + g) * c))  # (17 <= 4 is False) or 33 --> 33