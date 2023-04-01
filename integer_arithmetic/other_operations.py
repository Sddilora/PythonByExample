#The remainder of a division. Python modulo operator % is used to get the remainder of a division.
print(7 % 2)  # 1
print(8 % 2)  # 0

# Divide the number by itself
print(4 % 4)     # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)   # 55
# With negative numbers, it preserves the DIVISOR sign.!!!!!
print(-11 % 5)    # 4
print(11 % -5)    # -4
#Taking the remainder of the division by 0 also leads to "ZeroDivisionError".

#Exponentiation(tr.üs alma). Here is a way to raise a number to a power:
#This operation has a higher priority over multiplication.
print(10 ** 2)  # 100 (10^2)

#PEP Time!
#So first, remember to surround a binary operator with a single space on both sides.
number=30+12      # No!

number = 30 + 12  # It's better this way

# "Operators" are symbols
# "Operands" are values that the operation is performed on.
# Operators and their operands should be in the same line.
# In Python code, it is permissible to break before or after a binary operator.

# No: operators sit far away from their operands
income = (number +
          number +
          (number - number) -
          number -
          number)

# Yes: easy to match operators with operands   
income = (number  
        + number   
        + (number - number)  
        - number  
        - number) 
