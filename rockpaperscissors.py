import random

def game():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid input. Please enter rock, paper or scissors: ").lower()

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nUser choice: {user_choice}")
        print(f"Computer choice: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose.")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
                if play_again == "no":
                    print("Thank you! Play again with me someday")
                break
        
if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Battlefield Champpp!")
    game()
