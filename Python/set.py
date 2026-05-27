# Set with Delete Keyword

'''
Variable
Objectd
entire set
'''
'''
colors = {"red" , "blue" , "pink"}

print(colors)

del colors

print(colors)
'''
numbers = {1 , 2 , 3 , 4}

print(numbers)

# remove()

numbers.remove(2)

print(numbers)

# discard()

numbers.discard(5)

print(numbers)

# pop()

numbers.pop()

numbers.pop()

print(numbers)

# Convert two list into dictonary using zip()

keys = ["name" , "age" , "city"]

values = ["Alice" , 25 , "New York"]

data= dict(zip(keys , values))

print(data)

# Python :  Functions , Recursion , Lamda Function , Global Keyword and Multiple return values

# Function

# Function are reusable block of code used to perform a specific task.

# Reusability , Cleaner code , Better Organization , Reduce repetation 
def greet():
   
    print("Welcome Python Students!")

greet()

# Function with parameter

def add(a , b):
    print(a + b)

add(10 , 20)
add(20 , 20)

# Recursion

# A function calling itself.

# Factorial , tree structure , problem solving

# Base Case , Recursive Call

# Factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Sun of Numbers

def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(2))

# Anonymous / Lambda Function

# Lambda Function:

# small anonymous function
# written in one line
#no function name

# syntax

# lambda argument : expression

square = lambda x: x * x

print(square(5))

add = lambda a , b: a + b

print(add(10 , 20))

# List with lambda & map()

nums = [1 , 2 , 3 , 4 , 5]

result = list(map(lambda x : x * 2 , nums))

print(result)

# List with lambda & filter()

nums = [1 , 2 , 3 , 4 , 5 , 6]

odd  = list(filter(lambda x: x % 2 != 0 , nums))

print(odd)

# Global Keyword

# Variables creted outside function are called Global Variables

x = 10

def show():
    print(x)

show()

count = 0

def increment():
    global count
    count += 1  # count = count + 1

increment()
increment()
increment()

print(count)

# Return Multiple Values

# Python function can return : single values , multiple values

# Multiple Values are returned as tuple.

def calc(a , b):
    return  a + b , a-b
result = calc(10 , 5)

print(result)

def students():
    name="Chris Gayle"
    marks = 90
    return name , marks

result1 , result2 = students()

print(result1)
print(result2)

count = 10

def write(str):
    global count
    count+=1
    return str , count

print(write("Hello Python!!!"))






