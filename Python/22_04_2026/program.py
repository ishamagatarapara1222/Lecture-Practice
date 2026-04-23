def check_door():
    doorOpen = False

    if doorOpen:
        print("Welcome to Home...!")
    else:
        print("Meet me again tomorrow.")

def check_number():
    num = int(input("\nEnter a number:"))

    if num>0:
        print(f"{num} is positive.")
    elif num<o:
        print(f"{num} is nagative.")
    elif num==0:
        print("f{num} is zero.")
    else:
        print("Invaid input.")


def find_largest():

    a = int(input("\nEnter first number:"))
    b = int(input("Enter secon number: "))

    if a>b:
        print("Largest number is", a)
    elif b>a:
        print("Largest number is",b)
    elif b == a:
        print("Both number are same")
    else:
        print("Invalid input")

def check_leap_year():
    year = int(input("\nEnter a year:"))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap year")

def while_loop_demo():
    print("\nWhile loop (0 to 6):")
    i=0
    while i <= 6:
        print(i)
        i += 1

def for_loop_demo():
    print("\nfor loop (0 to 9):")

    for i in range(10):
        print(i)

def list_demo():
    print("List example:")

    fruits = ["Apple" , "Banana" , "Orange" , "Watermelon"]

    for fruit in fruits:
        print(fruit)

# MAIN MENU

while True:
    print("\n-----Python practice Menu-----")
    print("1. Check door status")
    print("2. Check number (Positive / Nagative / Zero)")
    print("3. Find largest of two numbers")
    print("4. Check leap year")
    print("5. While loop demo")
    print("6. For loop demo")
    print("7. list demo")
    print("0. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        check_door()
    elif choice == "2":
        check_number()
    elif choice == "3":
        find_largest()
    elif choice == "4":
        check_leap_year()
    elif choice == "5":
        while_loop_demo()
    elif choice == "6":
        for_loop_demo()
    elif choice == "7":
        list_demo()
    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, Try again...!")
        
    


        
        
    
        
    

        
        
