# Type Conversion

# Implicit type conversion

# explicit type conversion

# implicit: Python does it atomatically.

# explicit : You tell Python exactly what to convert to using buit-in functions.

# Convert to int()

type1 = "49"

print(int(type1))
print(type(int(type1)))

a = 9
b = 9.43

print("type a" , type(a))
print("type b" , type(b))

c = a + b

print("type c" , type(c))

print(c)

x = "9"

y = "9.43"

z = x + y

print(z)

# print(int("42.5"))

# float() :  Convert to Decimal Number

print(float("3.14"))

print(int("42"))

print(float("5"))

print(float("-0.001"))

# bool(): Convert to Boolean Value

print(bool(1))
print(bool(0))
print(int(True))
print(int(False))
print(bool("Hello"))
print(bool(None))
print(bool(2.13))
print(bool(12))

# str() : Convert to string

print(type(str(100)))
print(str(3.1459))
print(str(True))
print(str([1 , 2 , 3]))

# Sequence Conversion : list() , tuple() , set()

text = "hhello"

print(list(text))

print(tuple(text))

print(set(text))

# safe conversion Pattern

user_input = input("Enter a number:")

try:
    number = float(user_input)
    print(f"Converted:{number} * 2 = {number * 2}")
except ValueError:
        print("Invalid input , Plase choose numeric value")






