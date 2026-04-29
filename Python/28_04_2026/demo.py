# List and Tuple in Python (Basics & Mutability)

# List - Mutable

my_list = [10 , 20 , 30 , "Isha"]

print("list :" , my_list)

my_list[1] = 99

print("list :" , my_list)

my_list[3] = 101

print("list: " , my_list)

#my_list[4] = 102

print("list: " , int)

# Tuple - Immutable

my_tuple = (10 , 20 , 30)

print("Tuple:" , my_tuple)
#my_tuple[0] = 40

#String Formatting

# Indexing and Slicing

text = "Python"

print("First Letter:" , text[5])
print("First Letter:" , text[-2])

# Slicing

print("First 3 Latter:" , text[:3])
print("First 2 Latter:" , text[::3])

# Using List with Slicing and Formatting

students = ["Grisha" , "Isha" , "Dharmi" , "Hetvi" , "Siya" , "Charmi"]

print("First two students:" , students[::2])

# string formatting useing list

for student in students:
    print(f"Welcome , {student}")








