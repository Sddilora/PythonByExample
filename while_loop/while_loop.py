# Meet the loop command and one of the universal loops — the while loop.
# As the while loop requires the introduction of extra variables, iteration takes up more time.
# Thus, the while loop is quite slow and not that popular.

# The variable number plays here the role of a counter 
number = 0
while number < 5:
    print(number)
    number += 1
print('Now, the number is equal to 5')

# The infinite loop
dilo_says_stop = "?"
while True:
    print("I'm unstoppable")
    if dilo_says_stop == "stop":
        break
