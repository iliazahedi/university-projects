import random

player_name = input("What is your name? ")
print("Hello", player_name)
print("Welcome to Rock, Paper, Scissors game!")
print("Enter 'q' or 'quit' to exit the game.\n")

player_wins = 0
computer_wins = 0

while True:
    print(f"Score: {player_name}: {player_wins} | Computer: {computer_wins}")
    player_choice = input("Choose rock, paper, scissors (or 'q' to quit): ").lower()
    
    if player_choice == "q" or player_choice == "quit":
        print("\nThanks for playing! Goodbye!")
        break
    
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue
    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!\n")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print(f"{player_choice} beats {computer_choice}! You win!\n")
        player_wins += 1
    else:
        print(f"{computer_choice} beats {player_choice}! Computer wins!\n")
        computer_wins += 1

print("\nFinal Score:")
print(f"{player_name}: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print(f"*** {player_name} wins! Congratulations! ***")
elif player_wins < computer_wins:
    print("*** Computer wins. Better luck next time! ***")
else:
    print("*** It's a tie! ***")