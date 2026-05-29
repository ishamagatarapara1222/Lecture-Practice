# Python OOP Student Logic

# Topic Covered:
'''
1. Class and Object
2. self keyword
3. del keyword
4. Encapsulation

'''
# Class and Object

class Car:
    comp_name = None
    model = None
    color = None
    year = None

car1 = Car()
car2 = Car()

car1.comp_name = "Tata"
car1.model = "Sierra"
car1.color = "Pink"
car1.year = 2024

car2.comp_name = "Audi"
car2.model = "R8"
car2.color = "Blue"
car2.year = 2026

print("Car 1 Details")
print(car1.comp_name)
print(car1.model)
print(car1.color)
print(car1.year)

print("___________________")

print("Car 2 Details")

print(car2.comp_name)
print(car2.model)
print(car2.color)
print(car2.year)

# Student

class StudentData:
    std_name = None
    std_id = None
    std_age = None
    std_course = None

student1 = StudentData()
student2 = StudentData()

student1.std_name = "Isha"
student1.std_id = "7045"
student1.std_age = 17
student1.std_course = "AI/ML"

print("Student1 Details:")

print(student1.std_name)
print(student1.std_id)
print(student1.std_age)
print(student1.std_course)

class Student:
    def studentData(self):
        name = input("Enter Name: ")
        age  = int(input("Enter Age:"))
        course = input("Enter Course:")

        print("\n Student Details")
        print("Name :" , name)
        print("Age: " , age)
        print("Course: " , course)


s1 = Student()
s2 = Student()

s1.studentData()
s2.studentData()


# Concept

# class blueprint / template
# object real instance
# Student()   object creation


#  self Keyword

# self refers to current object.

class Student:

    def setData(self , name , marks):

        self.name = name
        self.marks = marks


    def display(self):

        print("Name:" , self.name)
        print("Marks:" , self.marks)


s1 = Student()
s2 = Student()

s1.setData("Rahul" , 45)
s1.display()

s2.setData("Ronak" , 26)
s2.display()

# Delete Keyword

# Used for:

# delete variable
# delete object
# delete property

class Student:

    def show(self):
        print("Student Object")

s1 = Student()

del s1

s1.show()

class Student:
    def setData(self):
        self.name=  "Rahul"

s1 = Student()

s1.setData()

del s1.name

print(s1.name)

# Encapsulation

# Hiding Data from direct access.

# security
# data protection

class Student:

    def __init__(self):

        self.__marks = 90

    def showMarks(self):
        print("Marks:" , self.__marks)

s1 = Student()

s1.showMarks()

#print(s1.__marks)





















