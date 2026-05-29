# Hierarchical  Inheritance

# Hierarchical Inheritance mean multiple child classes inherit from one parent class.

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meow")


d = Dog()
c = Cat()


d.eat()
d.bark()
c.eat()
c.meow()

# Hybrid Inheritance

# Hybrid Inheritance is a combination of multiple and diffrent multilevel inheritance.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(C , B):
    def display(self):
        super().show()

obj = D()

obj.display()

# super() follow MRO (Method Resolution Order).
# in class D(B , C) , python first check class B.

# type() function

# the type() function returns the datatype of a variable or Object.

a = 10
b = 5.5
c = "python"

print(type(a))
print(type(b))
print(type(c))

# dir() function

# the dir() function lists all attributes and methods of a class or object.

class Student:

    def __init__(self):
        self.name = "Ramesh"

    def show(self):
        print("Student Name:" , self.name)


obj = Student()

print(dir(obj))

# isinstance() function

# the isinstance function checks weather an object belongs to a class.

class Person:
    pass

class Student:
    pass

obj = Student()

print(isinstance(obj , Student))


# help() function

# the help() function display the documentation string of a class or function.

class Demo():
    """This is a demo class"""

    def show(self):
        """This is method display message"""
        print("Hello")

help(Demo)



















