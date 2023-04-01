# A piece of code that should be executed only under some condition should be placed within the body of an if statement.
# if + condition: + (indentation)expressions to execute
biscuits = 17
if biscuits >= 5:
    print("It's time for tea!")
print("This string will be printed independently from if statement")

#Nested(tr.iç içe) if statement
rainbow = "red, orange, yellow, green, blue, indigo, violet"
warm_colors = "red, yellow, orange"
my_color = "orange"

if my_color in rainbow:
    print("Wow, your color is in the rainbow!")
    if my_color in warm_colors:
        print("Oh, by the way, it's a warm color.")
