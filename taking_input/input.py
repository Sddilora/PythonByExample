#The input() function reads this value and returns it in a program as a string.
#It doesn't matter if you enter digits or letters, the input will be converted to a string.
user_name = input()
print('Welkom tu may çenıl' + user_name)

#the input() function may take an optional argument, that is, a message:
user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)

#Also we can print the message separately:
print('Enter your name pleaase: ')
user_name = input()
print('Hello, ' + user_name)

#If we want to take number we should write it expicitily:
print("What's your favorite number?")
value = int(input()) #in these circumstances, if a user enters a non-integer value, an Error will appear.