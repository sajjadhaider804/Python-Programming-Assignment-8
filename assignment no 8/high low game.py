import random

def play_high_low_game() -> None:
    NUM_ROUNDS = 5  # Total number of rounds to play
    score = 0  # Player's score

    print("Welcome to the High-Low Game!")
    print("You will be given a number, and you must guess if it's higher or lower than the computer's number.")

    # Milestone #4: Play multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}/{NUM_ROUNDS}")
        print("-" * 20)

        # Milestone #1: Generate random numbers
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Milestone #2: Get the user choice
        print(f"Your number is: {player_number}")
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's number? ").strip().lower()

        # Input validation
        while guess not in ["higher", "lower"]:
            print("Invalid input! Please type 'higher' or 'lower'.")
            guess = input("Try again: ").strip().lower()

        # Milestone #3: Write the game logic
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print("Correct guess!")
            score += 1  # Milestone #5: Update score if the guess is correct
        elif player_number == computer_number:
            print("It's a tie! The computer wins this round.")
        else:
            print("Wrong guess!")

        print(f"The computer's number was: {computer_number}")
        print(f"Your current score: {score}")

    # Final score after all rounds
    print("\nGame Over!")
    print(f"Your total score: {score}/{NUM_ROUNDS}")

# Run the game
play_high_low_game()
