# The loop is used for repeat some block of code a certain number of times.
# Pretty often they have special variables called "counters" alongside them.
counter = 1
step = int(input())  # let it be 3
counter += step
print(counter)  # it should be 4

# In this case we need only non-negative integers from the user (we are increasing the counter after all :))
# We can prevent  incorrect inputs by using the abs() function.
# It is a Python built-in function that returns the absolute value of a number.
counter = 1
step = abs(int(input()))  # user types -3
counter += step
print(counter)  # it's still 4
