# super() function

# super() is used to call method or constructor of the parent class from the child class.

class Employee:

    def __init__(self , name):
        self.name = name
        print("Employee Constructor Called.")

class Manager(Employee):

    def __init__(self , name , department):

        # calling parent constructor

        super().__init__(name)

        self.department = department

        print("Manager constructor called.")

    def display(self):
        print("Name:" , self.name)
        print("Department:" , self.department)

m = Manager("Akhil" , "HR")

m.display()

# Manager inherits from employee
# super().__init__(name) calls the perent constructor.
# Parent class data is reused in child class.


# Polymorphism in class Inheritance

class Shape:
    def area(self):
        print("Area calculation")

class Circle(Shape):
    def __init__(self , redius):
        self.redius = redius

    def area(self):
        print("Area of Circle :" , 3.14 * self.redius * self.redius)

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle : " , self.length * self.width)

c = Circle(10)
r = Rectangle(5 , 10)

c.area()
r.area()


# Polymorphism with built-in function len()

# string

text = "Python "

# list

numbers = [10 , 20 , 30 , 40 ,  50]

# dictionary

student = {"name":"zeel" , "age":20}

print("Length of string : " , len(text))
print("Length of List : " , len(numbers))
print("Length of Disct: " , len(student))

# Polymorphism using transport Interface

class Transport:
    def travel(self):
        print("Travel Method")

class Train(Transport):
    def travel(self):
        print("Train travels on tracks.")

class Plane(Transport):
    def travel(self):
        print("Plane travels in air.")

t = Train()
p = Plane()

t.travel()
p.travel()



    






