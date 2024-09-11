"""Task 4 : Rock-Paper-Scissors Game

* User Input: Prompt the user to choose rock, paper, or scissors.
* Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.

* Game Logic: Determine the winner based on the user's choice and the computer's choice.
  Rock beats scissors, scissors beat paper, and paper beats rock.

* Display Result: Show the user's choice and the computer's choice. Display the result,
  whether the user wins, loses, or it's a tie.

* Score Tracking (Optional): Keep track of the user's and computer's scores for multiple
  rounds.

* Play Again: Ask the user if they want to play another round.
* User Interface: Design a user-friendly interface with clear instructions and feedback."""

import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to display the game result
def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}")

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        print("Type 'rock', 'paper', or 'scissors' to play.")
        print("Type 'quit' to exit the game.")
        
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "quit":
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScores: You - {user_score}, Computer - {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThank you for playing! Final scores:")
    print(f"You: {user_score} | Computer: {computer_score}")

if _name_ == "_main_":
    play_game()
