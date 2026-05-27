
import sys
print(sys.executable)

# Built-in functions vs User defined Functions(UDF)

# Built-in Functions

numbers = [10,  20 , 30 , 40]

print("Length:" , len(numbers))
print("Maximum:" , max(numbers))
print("Minimum:" , min(numbers))

# These are pre-defined inside python , you don't need to create them.

# User-defined Functions

def greet(name):
    return "Hello" + name

print(greet(" Yaksh"))
print(greet(" Isha"))

# you define these function using def.

# Arbitratry Arguments

# When number of inputs is unkown

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(12 , 22 , 33))

print(add_numbers(10 , 12 , 13 , 14 , 15))

# Keyword Arguments(**kwargs)

# When pass is named value

def student_info(**kwargs):
    for key ,  value in kwargs.items():
        print(key , ":" , value)

student_info(name = "Isha" , age = 28 , course = "Python")

# **kwargs stores data in a dictionary

# doc (documentation string)

# used to describe functions

def multiply(a , b):
    """this function return the multiplication of two numbers"""
    return a * b

print(multiply(5 , 3))

print(multiply.__doc__)





    



                        
