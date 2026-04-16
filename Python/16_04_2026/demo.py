# Rock Paper Scissors - Advanced Practice

import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
rounds = 3

def play_round():
    global user_score, computer_score

    computer = random.choice(choices)
    player = input("\nChoose rock, paper or scissors: ").lower()

    # Input validation
    if player not in choices:
        print("Invalid input! Try again.")
        return

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print(" Computer wins this round!")
        computer_score += 1


# Game Loop
print(" Welcome to Rock Paper Scissors Game")

for i in range(rounds):
    print(f"\n--- Round {i+1} ---")
    play_round()

# Final Result
print("\n===== FINAL RESULT =====")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print(" You are the final winner!")
elif user_score < computer_score:
    print("Computer is the final winner!")
else:
    print(" It's a draw!")
