# All type of Python Functions

# T - Take Argument
# N - No Argument
# R - Return Value
# N - No return Value

'''
TNRN : Take no argument , return no value
TSRN : Take some argument , return no value
TNRS : Take no argument , return some value
TSRS : Take some argument  . return some value
'''

# TNRN

def greet():
    print(" Welcome Python Students!!")

greet()

# TSRN

def add(a , b):
    print("Addition = " , a + b)

add(20 , 30)

# TNRS

def message():
    return "Hello Python!!!"

print(message())

# TSRS

def multiply(x , y):
    return x * y

print(multiply(12 , 22))

#Diagram

#Argument : TNRN

# return : TNRS , TSRN

# both : TSRS

# return ends function execution

def calc(a , b):
    return a + b , a-b

x , y = calc(12 , 13)

print(x)
print(y)

#  1D Array in Python

# in python, a list is used to store multiple values in a single variable.

# Example

Marks = [89 , 59 , 98 , 65 , 100]

'''
78 is at index 0
52 is at index 1
98 is at index 2
24 is at index 3
100 is at index 4
'''

print(Marks)

# Accessing Elements
# Using Index

numbers  = [1 , 2 , 3 , 4 , 5 , 6]

print(numbers[0])
print(numbers[2])

# Nagative Indexing

numbers  = [1 , 2 , 3 , 4 , 5 , 6]

print(numbers[-1])
print(numbers[-2])

# Changing List Elements

numbers  = [1 , 2 , 3 , 4 , 5 , 6]

numbers[1] = 20

print(numbers)

# List Traversing using loop

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

for i in numbers:
    print(i)

# Using range() with indexing

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

print("Length of List : " , len(numbers))

for i in range(len(numbers)):
    print("Index:" , i , "Value:" , numbers[i])


# Add Element at end of the List.

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

numbers.append(11)

print(numbers)

# insert() in List


numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

numbers.insert(3 , 30)

print(numbers)


# Remove Elements

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

numbers.remove(1)

print(numbers)

# Remove Elements at end of the list


numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

numbers.pop()
numbers.pop()
numbers.pop()

print(numbers)


# Searching in List

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

if 20 in numbers:
    print("Found")

# List Slicing

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]

print(numbers[3:7])

# sum of List Elements

numbers  = [1 , 2 , 3 , 4 , 5 , 6,  7 , 8 , 9 , 10]
'''
total = 0

for i in numbers:
    total += i

print(total)
'''
total = sum(numbers)

print(total)






    
        













    
