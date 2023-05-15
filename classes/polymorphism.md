# Python Polymorphism
## The word refers to methods/functions/operators with the same name that can be executed on many objects or classes.

## Function Polymorphism

```
# For strings len() returns the number of characters:

x = "Hello World!"

print(len(x))  # 12
```

```
# For tuples len() returns the number of items in the tuple:

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))  # 3
```

```
# For dictionaries len() returns the number of key/value pairs in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))  # 3
```
## Class Polymorphism
- Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
```
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
```