# ================================
# Python Practice File
# Topics: Type Casting + Data Types
# ================================

print("----- Task 1: Type Casting -----")

num_str = "100"
num_int = int(num_str)
print("String to Int:", num_int, type(num_int))

num_float = 45.67
float_to_int = int(num_float)
print("Float to Int:", float_to_int, type(float_to_int))

num = 50
num_to_str = str(num)
print("Int to String:", num_to_str, type(num_to_str))


print("\n----- Task 2: Boolean Conversion -----")

print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(-10):", bool(-10))
print("bool(''):", bool(""))
print("bool('Hello'):", bool("Hello"))


print("\n----- Task 3: List, Tuple, Set, Dict -----")

my_list = [1, 2, 3, 4, 5]
print("List:", my_list, type(my_list))

my_tuple = tuple(my_list)
print("Tuple:", my_tuple, type(my_tuple))

my_set = set(my_list)
print("Set:", my_set, type(my_set))

my_dict = {
    "name": "Isha",
    "age": 16,
    "city": "Surat"
}
print("Dictionary:", my_dict, type(my_dict))


print("\n----- Task 4: String to Collection -----")

text = "python"

print("List:", list(text))
print("Tuple:", tuple(text))
print("Set:", set(text))


print("\n----- Task 5: Remove Duplicates -----")

dup_list = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", dup_list)

unique_set = set(dup_list)
print("After Removing Duplicates (Set):", unique_set)


print("\n----- Task 6: Type Checking -----")

print("Type of num_str:", type(num_str))
print("Type of num_int:", type(num_int))
print("Type of num_float:", type(num_float))
print("Type of my_list:", type(my_list))
print("Type of my_tuple:", type(my_tuple))
print("Type of my_set:", type(my_set))
print("Type of my_dict:", type(my_dict))


print("\n----- END OF PRACTICE -----")
