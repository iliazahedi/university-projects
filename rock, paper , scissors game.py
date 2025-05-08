import random

player_name = input("What is your name? ")
print("Hello", player_name)
print("Welcome to Rock, Paper, Scissors game!")

# Computer makes a random choice
computer_choice = random.choice(["rock", "paper", "scissors"])

# Player makes their choice
player_choice = input("Please choose rock, paper, or scissors: ").lower()

print(f"\nYou chose: {player_choice}")
print(f"Computer chose: {computer_choice}\n")

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! Computer wins!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cut paper! Computer wins!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cut paper! You win!")
    else:
        print("Rock smashes scissors! Computer wins!")
else:
    print("Invalid choice. Please try again with rock, paper, or scissors.")
