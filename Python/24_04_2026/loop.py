# Sum of first N Natural Numbers

n = int(input("Enter N Numbers:"))
sum = 0

for i in range(1 , n + 1):
    sum+= i
print("Sum:", sum)

# Count digit in Numbers

num = int(input("Enter number:"))
count = 0

for i in num:
    if i.isdigit():
        count += 1
print("Number of digits:" , count)

while num != 0:
    num //= 10
    count += 1
print("Number of digit:" , count)

#find largest number of list

numbers = list(map(int , input("Enter numbers:")))

lergest = numbers[0]  # 0 is index from list

for num in numbers:
    if num > lergest:
        lergest = num
print("Largest:" , lergest)




