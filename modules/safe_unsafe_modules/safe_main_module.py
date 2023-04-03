# In general, if you have more than just one line to execute in a script
# It's convenient to move all that code into a function called main
# And then call it like that:
name = "Mr.Bee"

def main():
    print("Hello,", name)

if __name__ == "__main__":
    main()

# Note, that the naming itself doesn't affect the way a function is executed,
# It's just a convention to indicate that this function is run only when the file is used as a script