# Student Information + Calculator Program

# Variable Assignment
student_name = "Vishal"
student_age = 20
marks_math = 85
marks_science = 90
marks_english = 78

# Display student info
print("----- Student Information -----")
print("Name:", student_name)
print("Age:", student_age)

# Arithmetic Operators (Total & Average)
total_marks = marks_math + marks_science + marks_english
average_marks = total_marks / 3
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Comparison Operators
print("\n----- Result Status -----")
print("Passed in all subjects?", marks_math >= 40 and marks_science >= 40 and
marks_english >= 40)

# Logical Operator
is_topper = average_marks > 85 and total_marks > 250
print("Is Topper:", is_topper)

# Assignment Operators
bonus_marks = 5
total_marks += bonus_marks # total_marks = total_marks + bonus_marks

# Data Types Check
print("\n----- Data Types -----")
print("Type of Name:", type(student_name))
print("Type of Age:", type(student_age))
print("Type of Average:", type(average_marks))
print("Type of Result:", type(is_topper))

# User Input (optional extra)
print("\n----- Simple Calculator -----")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)
print("Floor Division:", num1 // num2)

