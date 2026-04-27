# Mini loop practice program

#Take input
n = int(input("Enter a number: "))

#1. Print numbers from 1 to N
print("\n======1 to N======")
for i in range(1, n+1):
    print(i)

#2. Print odd numbers
print("\n======Odd Numbers======")
for i in range(1, n+1):
    if i%2 != 0:
        print(i)

#3. Sum of Numbers
print("\n======SUM======")
total = 0
for i in range(1, n+1):
    total += i
print("\nSum:", total)

#4. Factorial using while loop
print("\n======Factorial======")
fact = 1
temp = n
while temp > 0:
    fact *= temp
    temp -= 1
print("Factorial :", fact)

#5. Right triangle
print("\n======Right Triangle======")
for i in range(1,6):
    print("*" *i)

#6. Revers Triangle
print("\n======Reverse Triangle======")
for i in range(5, 0, -1):
    print("*" *i)

#7. Multiplication Table
print("\n======Multiplication table (1 to 5)======")
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end =" ")
    print()

#8. Continue example (skip 5)
print("======Skip 5======")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# 9. Break example (stop at 8)
print("\nStop at 8:")
for i in range(1, 10):
    if i == 8:
        break
    print(i)

# 10. Reverse a number
num = int(input("\nEnter number to reverse: "))
rev = 0
while num > 0:
    rev = rev * 10 + (num % 10)
    num //= 10
print("Reversed:", rev)

# 11. Loop through string
text = input("\nEnter a string: ")

print("Characters:")
for ch in text:
    print(ch)

# 12. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)

