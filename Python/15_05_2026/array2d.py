# Python Lecture Topic : 2D array with List
# Array inside another array

# Stores Data : rows , columns

# It looks like a table or Matrix.

# Examples



arr1 = [1 , 2 , 3 , 4 , 5]

arr2 = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

print(arr1)
print(arr2)

# Accessing Elements in 2D Array

# Syntax: array[row][column]

print(arr1[0])
print(arr2[1][0])
print(arr2[2][2])


# Taking Input in 2D Array

arr = []

rows = int(input("Enter rows:"))
cols = int(input("Enter columns:"))

for i in range(rows):
    row  = []
    for j in range(cols):
        value = int(input(f"arr[{i}][{j}] = "))
        row.append(value)
    arr.append(row)
print(arr)


# Printing 2D Array using Nested Loop

arr = [
    [1 , 2 , 3],
    [3 , 4 , 5]
]

for i in arr:
    for j in i:
        print(j , end="  ")
    print()

# Sum of All Elements in 2D Array

arr = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7,  8 , 9]
]

total = 0

for i in arr:
    for j in i:
        total += j
print("Total:" , total)

# Sorting Collection Datatypes

# Sorting Mean : Arranging data in order

# Types : 1. Ascending
#         2.Descending

# Syntax : list.sort()

numbers = [5 , 8 , 2 , 7 , 9 , 1]

numbers.sort()

print(numbers)


numbers = [5 , 8 , 2 , 7 , 9 , 1]

numbers.sort(reverse = True)

print(numbers)

# Sorting in String

fruits = ["Mango",  "Banana" , "Apple" , "Kiwi"]

fruits.sort()

print(fruits)



