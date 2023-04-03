# It is used to additional conditions(else if)
# Basic elif syntax:
price = 10000 # there should be some int value
if price > 5000:
    print("That's too expensive!")
elif price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")

# "I can afford that!" will be printed if the price <= 5000 and > 500

# multiple elifs example
light = "red"  # there can be any other color
if light == "green":
    print("You can go!")
elif light == "yellow":
    print("Get ready!")
elif light == "red":
    print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")

# Nested elifs example
traffic_lights = "green, yellow, red"
light = input("Type a color name")
if light in traffic_lights:
    if light == "green":
        print("You can go!")
    elif light == "yellow":
        print("Get ready!")
    else:
        print("Just wait.")
else:
    print("No such traffic light color, do whatever you want")
