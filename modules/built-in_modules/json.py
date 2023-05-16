# Python has a built-in package called json, which can be used to work with JSON data.
import json

# If we have a JSON string, we can parse it by using the json.loads() method.
# The result will be a Python dictionary.

# Convert from JSON to Python:
x = '{ "name":"John", "age":30, "city":"New York"}'  # a JSON object
y = json.loads(x)  # a Python dictionary
print(y["age"])  # 30

# Convert from Python to JSON:
# If we have a Python object, we can convert it into a JSON string by using the json.dumps() method.
x = {"name": "John", "age": 30, "city": "New York" }  # a Python object (dict)
y = json.dumps(x)  # a JSON string
print(y)  # {"name": "John", "age": 30, "city": "New York"}

# The json.dumps() method has parameters to make it easier to read the result:
# Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4) 

# Use the separators parameter to change the default separator:
# The default separator is (", ", ": ") : {"name": "John", "age": 30, ...}
json.dumps(x, indent=4, separators=(". ", " = "))

# Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True) # keys sorted in alphabetical order
