#Syntax
def function_name(parameters):
    """Docstring"""
    # Function body
    return 0

# Why function
num=24
if num%2==0:
    print("Even")
else:
    print("Odd")

def even_or_odd(num):
    """This function fund even or odd number"""
    if num%2==0:
        print("This number is Even")
    else:
        print("This number is Odd")
even_or_odd(num)

def add(a,b):
    return a+b
result = add(5,6)
print(result)

#Default Parameters
def greet(name="Guest"):
    print(f"Hello {name}, Welcome to Python")

greet("Sakti")
greet()

### Variable Length Arguments
### Positional and Keywords arguments

def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(1,2,3,4,5,6,7,8,9,"Sakti","Prasad","Behera")

### Keywords arguments
def printDetails(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
printDetails(name="Sakti",age="30",country="India")

def printDetails1(*args, **kwargs):
    for val in args:
        print(f"Postional argument: {val}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printDetails1(1,2,3,4,"Sakti",name="Sakti",age="30",country="India")

## Return multiple parameter
def multiply(a,b):
    return a*b,a
result = multiply(5,6)
print(result)