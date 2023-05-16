# A file containing a set of functions you want to include in your application.

- Note: When using a function from a module, use the syntax: module_name.function_name.
- Also variables of all types (arrays, dictionaries, objects etc): module_name.dict_name

## We can re-name a module when importing with keyword "as"
```
import module_name as waa

a = waa.person1["age"]
```
## We can choose to import only parts from a module, by using "from" keyword.
```
# Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])
```