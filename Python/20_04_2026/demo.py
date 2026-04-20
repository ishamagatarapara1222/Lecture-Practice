#==============================
#TYPE CONVERSION PRACTICE FILE
#==============================

print("-----String to integer-----")
num_str1 = "100"
num_str2 + "45"

result = int(num_str1) + int(num_str2)
print("Addition:",result)

print("\n----- FLOAT TO INT -----")
float_num = 9.99
print("Before:", float_num)
print("After int():", int(float_num))


print("\n----- BOOLEAN TO INT -----")
print("True + True =", int(True) + int(True))
print("True + False =", int(True) + int(False))

print("\n----- INT/FLOAT TO STRING -----")
num = 25
flt = 5.5

print("Concatenation:", str(num) + str(flt))


print("\n----- STRING TO LIST/TUPLE/SET -----")
text = "hello"

print("List:", list(text))
print("Tuple:", tuple(text))
print("Set:", set(text))   # notice duplicates removed


print("\n----- LIST / TUPLE / SET DIFFERENCE -----")
list_ex = [1, 2, 2, 3]
tuple_ex = (1, 2, 2, 3)
set_ex = {1, 2, 2, 3}

print("List:", list_ex)
print("Tuple:", tuple_ex)
print("Set:", set_ex)   # duplicates removed


print("\n----- DICTIONARY PRACTICE -----")
keys = ['a', 'b', 'c']
values = [1, 2, 3]

dict_from_zip = dict(zip(keys, values))
print("Dictionary:", dict_from_zip)


print("\n----- ID() FUNCTION (IMMUTABLE) -----")
x = 10
y = 10

print("x id:", id(x))
print("y id:", id(y))   # same memory (small int optimization)


print("\n----- ID() FUNCTION (MUTABLE) -----")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 id:", id(list1))
print("list2 id:", id(list2))
print("list3 id:", id(list3))  # same as list1


print("\n----- MUTABLE CHANGE TEST -----")
list3.append(4)

print("list1:", list1)  # will change
print("list3:", list3)


print("\n----- USER INPUT PRACTICE -----")
# Uncomment to test
# user_input = input("Enter a number: ")
# print("Square:", int(user_input) ** 2)


print("\n----- MINI TASKS -----")

# Task 1: Convert string to int and multiply
a = "6"
b = "7"
print("Task1:", int(a) * int(b))

# Task 2: Convert float to int and add 10
f = 8.76
print("Task2:", int(f) + 10)

# Task 3: Remove duplicates using set
nums = [1, 1, 2, 3, 3, 4]
print("Task3:", list(set(nums)))

# Task 4: Convert list to tuple
lst = [10, 20, 30]
print("Task4:", tuple(lst))

# Task 5: Check same memory or not
a = [1, 2]
b = a
c = [1, 2]

print("a == b:", a == b)
print("a is b:", a is b)

print("a == c:", a == c)
print("a is c:", a is c)


