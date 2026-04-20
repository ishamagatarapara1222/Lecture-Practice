import random

while True:
    print("\n==== MENU ====")
    print("1. Simple Calculator")
    print("2. Rock Paper and Scissors")
    print("3. Bill Generator")
    print("4. Age Calculator")
    print("5. Even/odd + Positive/Negative Check")
    print("6. Exit")

    print("\n")
    choice = input("Enter your choice: ")

    if choice == "1":

        a = int(input("Enter first number - "))
        b = int(input("Enter second number - "))

        print("Addition - ", a + b)
        print("Subtraction - ", a - b)
        print("Division - ", a / b)
        print("Multiplication- ", a * b)
        print("Modulus - ", a%b)
        print("Expontiation - ", a**b)
        print("Floor Division - ", a//b)

    elif choice == "2":

        choices = ["Rock", "Paper", "Scissors"]
        computer = random.choice(choices)
        player = input("Choose Rock, Paper, Scissors: ")

        print("Computer chose:", computer)

        if player == computer:
            print("It's a tie")
        elif (player == "Rock" and computer == "Scissors") or \
            (player == "Paper" and computer == "Rock") or \
            (player == "Scissors" and computer == "Paper"):
             print("You win!")
        else:
            print("You lose!")
    
    elif choice == "3":

        a = int(input("Enter Date - "))
        b = input("Enter Company name - ")
        c = int(input("Enter Payment Amount - "))
        d = int(input("Enter Due Date - "))

        print("\n")
        print(f"A {b}, Has to Pay , {c}  Before , {d} Bill Generated on , {a} ")
    

    elif choice == "4":

        a = int(input("Enter your Born Year - "))
        b = int(input("Enter Current Year - "))

        c = b-a

        print(f"You are {c} yeras old")

    elif choice == "5":

        a = int(input("Enter the Number - "))

        print("\n")

        if a%2 == 0 and a>0:
            print("Number is Even and Positive.....")

        elif a%2 == 0 and a<0:
            print("Number is Even and Nagative.....")

        elif a%2 != 0 and a>0:
            print("Number id Odd and Positive......")

        elif a%2 != 0 and a<0:
            print("Number is Odd and Nagative......")

        elif a==0:
            print(" Zero is neither positive nor negative,It is nuteral....")

        else:
            print("Invalid choice...!!!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
            print("Invalid choice, try again.")
