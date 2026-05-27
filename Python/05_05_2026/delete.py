# Write a recursive function to calculate the factorial of a given number.
# Ensure the program handles edge cases (e.g., negative inputs)

def Factorial(n):
    if n < 0:
        return "Invalid Value"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

print(Factorial(5))
print(Factorial(10))

#Implement a recursive function to calculate the nth Fibonacci number.
#Test the function with various inputs.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# Develop a program using recursion to reverse a string

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

# Write a recursive function to find the sum of all digits of a given number until a single-digit number remains.

def sum_digit(n):
    if n < 10:
        return n
    return n % 10 + sum_digit(n // 10)

print(sum_digit(123456))
