# Polymorphism in Python

# Polymorphism mean "many forms" in Object-Oriented Programming(OOP)

# polymorphism allows the same method name to perform diffrent task depending on the object or argument used.

# Method Overloading
# Method Overriding

# It also Provide built-in functions

# issubclass()
# super()


#1 . Method Overloading

# Method overloading mean creating multiple methods with the same name but with diffrent parameter.

class Calculator:
    def multiply(self , a , b , c = 1):
        return a * b * c

# Object

calc = Calculator()

print("Multiplication of 2 Numbers:" , calc.multiply(2 , 4))

print("Multiplication of 3 Numbers:" , calc.multiply(2 , 4 , 3))

# If only 2 arguments are passed , c takes default value 1.

# if 3 arguments are passed, all values are multiplied.

# same method name multiply() perform diffrent operations.

#2. Method Overriding

# Method overriding occurs when a child class provides a specific implementation of a method already defined in the parent class.

class Animal:

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):

    def speak(self):
        print("Dog barks")

class Cat(Animal):

    def speak(self):
        print("Cat meow.")

# object

a = Animal()
d = Dog()
c =  Cat()

a.speak()
d.speak()
c.speak()

# Dog and Cat inherite from Animal,

# Both child classes override the speak() method.

# issubclass() function

# issubclass() is a built-in Python function used to check weather one class is derived from another class.

# syntax issubclass(child_class , parent_class)

# It's return

# True -->  if inhetitance exists
# Flase --> otherwise

class Person:
    pass

class Student():
    pass

# Student inerites from Person

print(issubclass(Student , Person))


# Polymorphism in function

def add(a , b):
    return a + b

print("Addition of integers:" , add(10 , 20))

print("Concatenation of String: " , add("Hello"  , "World"))




