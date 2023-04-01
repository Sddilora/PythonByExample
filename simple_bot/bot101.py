print('Hello! My name is Bot101.')
print('I was created in 2023.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is " + str(age) + " ; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
number = int(input())
counter = 0
while counter <= number:
    print(str(counter) + "!")
    counter += 1

print('Completed, have a nice day!')