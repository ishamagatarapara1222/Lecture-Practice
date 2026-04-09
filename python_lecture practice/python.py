print("=== Python Practice Program ===")

# -------------------------------
# Variables
# -------------------------------
print("\n--- Variables ---")
name = "Isha"
age = 16
marks = 85.5
is_pass = True

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Passed:", is_pass)

# -------------------------------
# User Input
# -------------------------------
print("\n--- User Input ---")
user_name = input("Enter your name: ")
user_marks = float(input("Enter your marks: "))

# -------------------------------
# Conditions
# -------------------------------
print("\n--- Result ---")

if user_marks >= 90:
    grade = "A"
elif user_marks >= 75:
    grade = "B"
elif user_marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Hello", user_name)
print("Your Grade is:", grade)

# -------------------------------
# Operators
# -------------------------------
print("\n--- Calculator ---")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)

if y != 0:
    print("Division:", x / y)
else:
    print("Division: Cannot divide by zero")

# -------------------------------
# Loops
# -------------------------------
print("\n--- For Loop (Table) ---")
num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n--- While Loop ---")
i = 1
while i <= 5:
    print("Count:", i)
    i += 1

# -------------------------------
# Function
# -------------------------------
print("\n--- Function ---")

def square(n):
    return n * n

number = int(input("Enter number to find square: "))
print("Square is:", square(number))

# -------------------------------
# Lists
# -------------------------------
print("\n--- Lists ---")

marks_list = [60, 70, 80, 90]
print("Original List:", marks_list)

marks_list.append(100)
print("Updated List:", marks_list)

print("All Marks:")
for m in marks_list:
    print(m)

print("Highest Marks:", max(marks_list))
print("Lowest Marks:", min(marks_list))
