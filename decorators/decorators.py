# Example1
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # This will greet Alice three times

# In this example, the repeat decorator takes an argument n.

# Example2
from datetime import datetime

def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   

     
daily_backup()

# Output:
# Daily backup job has finished.
# Function: daily_backup
# Run on: 2021-06-06 06:54:14
# ---------------------------

# Example3

from functools import wraps
import tracemalloc
from time import perf_counter 


def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list1():
    '''Range'''

    my_list = list(range(100000))


@measure_performance
def make_list2():
    '''List comprehension'''

    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    '''Append'''

    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    '''Concatenation'''

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


print(make_list1())
print(make_list2())
print(make_list3())
print(make_list4())

# Output:
# Function: make_list1
# Method: Range
# Memory usage:            0.000056 MB
# Peak memory usage:       3.991944 MB
# Time elapsed is seconds: 0.082043
# ----------------------------------------
# None
# Function: make_list2
# Method: List comprehension
# Memory usage:            0.000000 MB
# Peak memory usage:       3.992888 MB
# Time elapsed is seconds: 0.107368
# ----------------------------------------
# None
# Function: make_list3
# Method: Append
# Memory usage:            0.000000 MB
# Peak memory usage:       3.992736 MB
# Time elapsed is seconds: 0.099516
# ----------------------------------------
# None
# Function: make_list4
# Method: Concatenation
# Memory usage:            0.000000 MB
# Peak memory usage:       4.791808 MB
# Time elapsed is seconds: 20.096789
# ----------------------------------------