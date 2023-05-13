# An iterator is an object that contains a countable number of values. ( They consist of __iter__() and __next__().)

## Lists, tuples, dictionaries, strings and sets are all iterable objects. They are iterable containers which you can get an iterator from.

```
# Example

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry

mystr = "banana"
myitstr = iter(mystr)
print(next(myitstr))  # b
print(next(myitstr))  # a
```
## Looping Through an Iterator
- We can also use a for loop to iterate through an iterable object:
- The for loop actually creates an iterator object and executes the next() method for each loop.
```
# Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# Output:
# apple
# banana
# cherry 

# Itarate the characters of a string
mystr = "way"
for x in mystr:
print(x)

# Output:
# w
# a
# y
```

## Create an Iterator
- To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

- As we have learnde in the Python Classs/Objects chapter(notes.md), all classes have a function called __init__(), which allows us to do some initializing when the object is being created.

- The __iter__() methods acts similar, we can do operations, but must always return the iterator object itself.

- The __next__() methood also allows us to do operations, and must return the next item in the sequence.

```
# Create an iterator that returns, starting with 1, and each sequence will increase by one(returning 1,2,3,4...):

class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

numclass = Numbers()
numiter = iter(numclass)

print(next(numiter))
print(next(numiter))
```

## Stop Iteration
- The example above would continue forever if we had enough next() statements, or if it was used in a for loop.

- To prevent that we can use   **StopIteration** statement.

- In the __next__() method, we can add a terminating condition to raise an errır if the iteration is done a specified number of times.
```
# Stop after 20 iterations:

class ItStNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

stclass = ItStNumbers()
stiter = iter(stclass)

for x in stiter:
    print(x)
```
