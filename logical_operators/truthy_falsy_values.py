# We can use non-boolean values in a logical context.
# When used with logical operators they called "truthy" or "falsy".(non-booelan variables)
# It depends on whether they are interpreted as True or False.

# This values are evaluated to "False" in Python:
# constants defined to be false: "None" and "False",
# zero of any numeric type: "0", "0.0",
# empty sequences and containers: "", [], {}.

# Anything else generally evaluates to True.

print(0.0 or False)     # False
print("True" and True)  # True
print("" or False)      # False

# The logical operators in Python are short-circuited. That's why they are also called lazy. 
# That means that the second operand in such an expression is evaluated only if the first one is not sufficient to evaluate the whole expression.
# The operators or and and return one of their operands, not necessarily of the boolean type.!!
# "and" returns the first value if it evaluates to False, otherwise it returns the second value.
a = False and True  # False
a = True and True   # True
a = True and False  # False

# "or" returns the first value if it evaluates to True, otherwise it returns the second value.
b = True or False   # True
b = False or True   # True
b = True or True    # True
b = False or False  # False

# Difference in operator precedence(tr.öncelik):
# `not` has a highest priority and `and` has a higher priority than `or`
truthy_integer = False or 5 and 100  # 100
tricky = not (False or '')           # True

