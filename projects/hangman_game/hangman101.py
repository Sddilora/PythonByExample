# Hangman is a popular, funny, yet very grim game.
# A cruel computer hides a word from you and you need to guess it, letter by letter. 
# If you fail, you'll be hanged, if you win, you'll survive.

print("""H A N G M A N
The game will be available soon.""")

# In the first stage the only ture word is "python" :).

guess = input()
if guess == "python":
    print("You survived!")
else:
    print("You lost!")