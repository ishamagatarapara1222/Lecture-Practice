# ===============================
# Python Operators Practice File
# ===============================

# Task 1: Arithmetic Operator
print("----- Task 1: Arithmetic -----")
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Task 2: Comparison Operator
print("\n----- Task 2: Comparison -----")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("Both are equal")


# Task 3: Logical Operator
print("\n----- Task 3: Driving Check -----")
age = int(input("Enter your age: "))
license = input("Do you have license (yes/no): ")

if age >= 18 and license.lower() == "yes":
    print("Can Drive")
else:
    print("Cannot Drive")


# Task 4: Even / Odd
print("\n----- Task 4: Even/Odd -----")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Task 5: Marks Checker
print("\n----- Task 5: Grade -----")
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Task 6: Membership Operator
print("\n----- Task 6: Fruits Check -----")
fruits = ["apple", "banana", "mango"]

fruit = input("Enter fruit name: ")

if fruit.lower() in fruits:
    print("Fruit is available")
else:
    print("Fruit is not available")


# Task 7: Calculator
print("\n----- Task 7: Calculator -----")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", n1 + n2)
elif op == "-":
    print("Result:", n1 - n2)
elif op == "*":
    print("Result:", n1 * n2)
elif op == "/":
    print("Result:", n1 / n2)
else:
    print("Invalid Operator")


# Task 8: Identity Operator
print("\n----- Task 8: Identity -----")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)
print("a is b:", a is b)
print("a is c:", a is c)


# Task 9: String Check
print("\n----- Task 9: String Check -----")
text = input("Enter a string: ")

print("'a' in text:", "a" in text)
print("'z' in text:", "z" in text)


# Task 10: Login System
print("\n----- Task 10: Login -----")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
