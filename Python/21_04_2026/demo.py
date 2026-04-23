#======================================
#PYTHON STRING PRACTICE PROGRAM
#======================================

#-------TASK : 1 Basic string operation-------

print("-----Task 1-----")

text = "Hello, Python world!"

print("Upper case:-",text.upper())
print("Lower case:-",text.lower())
print("Count of (o):-",text.count("o"))
print("Find 'Python':-",text.find("Python"))
print("Starts with 'Hello':-",text.startswith("Hello"))

#---------Task : 2 Slicing-----------

print("\n-----Task 2-----")

s = "Programming"

print("First character:",s[0])
print("Last character:",s[-1])
print("slice 'gram' :",s[3:7])
print("Reversed:",s[::-1])

#---------Task : 3 String Formmating-----------

print("\n-----Task 3-----")

name = "Isha"
course = "Python"

print(f"My name is {name} and i am learning {course}")
print("My name is {} and i am learning {}".format(name,course))

#---------Task : 4 Join & Split---------------

print("\n-----Task 4-----")

data = "apple,banana,mango"

fruits = data.split(",")
print("Split list :",fruits)

print("Join with |:","|".join(fruits))

#----------Task  : 5 Mini project
print("\n-----Task 5-----")

user_name = input("Enter your full name:")

print("Upper case:-",user_name.upper())
print("Lower case:-",user_name.lower())
print("Length:-",len(user_name))
print("Reversed:-",user_name[::-1])


