# Encapsulation
# Constructor and destructor

# Encapsulation

# Binding data and methods together inside a class and restricting direct access to data.

# Public members
# Protected members (_variable)
# Private members (__variable)

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self , m):
        self.__marks = m

    def get_marks(self):
        return self.__marks

s = Student()

s.set_marks(90)

print("Marks:" , s.get_marks())

# Protected Data
# Prevent Direct Modification
# Improve security and maintainability

# Access Specifiers

# Public

class Student:

    def __init__(self):
        self.name = "Rahul"

s = Student()

print(s.name)

# Protected

class Student:

    def __init__(self):
        self._marks = 85

class Result(Student):

    def show(self):
        print("Marks:" , self._marks)

r = Result()

r.show()


# Private

class BankAccount:

    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print("Balance:" , self.__balance)
        
b = BankAccount()

b.show_balance()

# Real-Life Analogy

# You cannot directly access money inside ATM Hardware.

# PIN , Withdraw , Balance check

# Constructor in Python

# A special method automatically executed when an object is created.

# initialize variables
# Assign default value
# Execute setup code automatically

class Laptop:

    def __init__(self):
        print("laptop  object created")

lap = Laptop()

# Parameterized Constructor

class Student:

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def display(self):

        print("Name" , self.name)
        print("Age" , self.age)

s1 = Student("aman" , 21)

s1.display()


