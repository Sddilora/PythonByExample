# A variable is only available from inside the region it is created this is called "scope".
# Local Scope
# A variable created inside a function is available inside that function:
def scfunc():
    x = 450
    print(x)

scfunc()

# Variables are reachable for any function inside the function.
def scfunc2():
    x = 500
    def scfunc3():
        print(x)
    scfunc3()

scfunc2()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 600

def scfunc4():
    print(x)

scfunc4()

print(x)

# Global Keyword
# If we need to create a global variable, but are stuck in the local scope, we can use the global keyword.
# The global keyword makes the variable global.
def scfunc5():
    global x 
    x = 700

scfunc5()

print(x) # Global x changed and its 700 now.
