In python spaces are important.For ex, I wrote;
   print("Hello, World!") #This won't work :(
print("Hello, World!")  #This will :)

Names are case-sensitive in Python.(Print, print and PRINT are not the same.)

Like most of the languages we need to follow common conventions concerning programming style, so other programmers are able to read your code easily.
There is a document that is called PEP 8. The key idea of it is to use the same code style for all Python projects as if they were written by the same programmer.

Some of the rules(advices?) on PEP 8
-Do not use more than 79 characters in a line of code.
-Avoid extra spaces(within parentheses, before an opening parethesis etc.)
-Quotes("",'') should be used consistently and/or to avoid backslashes.
-For variables use lowercase and underscores to split words.
-For constants, it's common to write its name in all capital letters
-If the most suitable variable name is some Python keyword, add an underscore to the end of it.(class_ : "sth")
-Choose a name that is readable and descriptive, but not too wordy (1-3 words are enough).

We don't need package or func we just write something and they work :).

Every data object (a variable or a constant) has a type
Python has five standard data types
- Numbers (Numeric values)
- String
- List
- Tuple
- Dictionary

Python supports four different numerical types 
- int (signed integers) (10)
- long (long integers, they can also be represented in octal and hexadecimal)(51924361L)
- float (floating point real values)(0.0)
- complex (complex numbers)(3.14j)

People generally don't choose Python to write fast code. The main advantages of Python are readability and simplicity.

The reason sum((x, y)) works and sum(x, y) doesn't work is because the sum() function can only take iterable objects as its first argument, such as lists and tuples.
So when you try to run sum(x, y), Python looks at the x variable, which is defined to be an integer, and tries to iterate through it, which won't work since

There are several types of collections to store data in Python.
Positionally ordered collections of elements are usually called "sequences".
Both "strings" and "lists" belong to them.
Each element in them has an Index that corresponds to its position.
Indexes are used to access elements within a sequence.
Indexing is zero based. It means that you start the count from zero :).

Interpreter: During the interpretation part, the software goes through your program and executes the code, line by line. This software is called an interpreter.
An interpreter can be written in any programming language. The default Python interpreter is written in C, it is called CPython.

In Python to organize and reuse code called modules.
The module is simply a file that contains Python statements and definitions.
What really makes the module system powerful is the ability to "load" or "import" one module from another.

In order to be available for import, used_module.py should be located in the same directory as the file you are trying to import used_module.
At first, Python importing system looks for a module in the current directory, then it checks the built-in modules, and if nothing is found an error will be raised

A simple module that is written for direct execution is often called a "script".
The difference between a module and a script in Python is only in the way they are used.
Modules are loaded from other modules or scripts, and scripts are executed directly.

Python is an object oriented programming language.
