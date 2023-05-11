- We'll use a decorator when you need to change the behavior of a function without modifying the function itself.

- To get a better understanding of how decorators work, We should understand a few concepts first.

##A function is an object. Because of that, a function can be assigned to a variable. The function can be accessed from that variable.

```
def my_function():

    print('I am a function.')

# Assign the function to a variable without parenthesis. We don't want to execute the function.

description = my_function

# Accessing the function from the variable I assigned it to.

print(description())

# Output: 'I am a function.'
```

##A function can be nested(tr. iç içe) within another function.

```
def outer_function():

    def inner_function():

        print('I came from the inner function.')

    #Executing the inner function inside the outer function.
    inner_function()

outer_function()

# Output: I came from the inner function.
```

!! Note that the inner_function is not available outside the outer_function. If I try to execute the inner_function outside of the outer_function I receive a NameError exception.

##Since a function can be nested inside another function it can also be returned.

```
def outer_function():
    '''Assign task to student'''

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()

homework()

# Output: 'Read Python book chapter 5.'
```

##A function can be passed to another function as an argument.
```
def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print('Don\'t forget to bring your wallet!')

def action():

    print('I am going to the store buy you something nice.')

# Calling the friendly_reminder function with the action function used as an argument.

friendly_reminder(action)

# Output: I am going to the store buy you something nice.
Don't forget to bring your wallet!
```

###Sooo here we are:
##How to Create a Python Decorator
- To create a decorator function in Python, We create an outer function that takes a function as an argument. There is also an inner function that wraps around the decorated function.
```
def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func
```
- To use a decorator ,you attach it to a function like you see in the code below. We use a decorator by placing the name of the decorator directly above the function we want to use it on. You prefix the decorator function with an @ symbol.
```
@my_decorator_func
def my_func():

    pass
```

##How to add Arguments to Decorators in Python
#Decorators can have arguments passed to them. To add arguments to decorators We add *args and **kwargs to the inner functions.

- *args will take an unlimited number of arguments of any type, such as 10, True, or 'Brandon'.

- **kwargs will take an unlimited number of keyword arguments, such as count=99, is_authenticated=True, or name='Brandon'.

```
def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        #Do something before the function.
        func(*args, **kwargs)
        #Do something after the function.
    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    '''Example docstring for function'''

    pass
```

- Decorators hide the function they are decorating. If I check the __name__ or __doc__ method we get an unexpected result.
```
print(my_func.__name__)
print(my_func.__doc__)

# Output:
# wrapper_func
# None
```

##We can use decorators with classes as well. Let's see how you use decorators with a Python class.
- In this example, notice there is no @ character involved. With the __call__ method the decorator is executed when an instance of the class is created.
```
import requests

class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return

@LimitQuery
def get_coin_price(limit):
    '''View the Bitcoin Price Index (BPI)'''
    
    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))

# Output:
# $35968.25
# $35896.55
# $34368.14
# $35962.27
# $34058.26
# No queries left. All 5 queries used.
```