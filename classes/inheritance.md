## Create a Parent Class
```
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

## Create a Child Class
```
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass
```

### Now the Student class has the same properties and methods as the Person class.
```
# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()
```

## Add the __init__() Function
- When we add the __init__() function, the child class will no longer inherit the parent's __init__() function.
```
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
```
- To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
```
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

## Use the super() Function
- super() function makes the child class inherit all the methods and properties from its parent:
```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

## Add Properties
```
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
```
- In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
```
# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
```

## Add Methods
```
# Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
```

