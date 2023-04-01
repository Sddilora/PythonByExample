# We know that Python treats inputs as a String value.
# For numerical values
# As a general rule, they are explicitly converted to corresponding numerical types.
# If user types an inaccurate input (like some string for int input) "ValueError" will ocur.
integer = int(input())
floating_point = float(input())

# Basic Example
# Free air miles bonus program:

# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per unit of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)