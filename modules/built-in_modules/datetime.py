# Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print("now",x)  # now 2023-05-15 12:58:50.088636

# Return the year and name of weekday:
print("year",x.year)  # year 2023
print("name of weekday",x.strftime("%A"))  # name of weekday Monday

# Create a date object:
x = datetime.datetime(2020, 5, 17)
print("date object",x)  # date object 2020-05-17 00:00:00

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))  # June
