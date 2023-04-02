# else doesnt't require any condition.
today = input("If today is a holiday, than type holiday")
if today == "holiday":
    print("Hurray!")
else:
    print("Oh nooo :(")

# if-else can be written in one line. It's called "Ternary Operator"
# <first_alternative> if <condition> else <second_alternative>
print("Hurray!") if today == "holiday" else print("Oh nooo :(")

# Nested if-else
x = int(input())
if x < 100:
    print("x < 100")
else:
    if x == 100:
        print( "x = 100")
    else:
        print("x > 100")