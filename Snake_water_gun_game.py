# SNAKE , WATER , GUN GAME

import random

# List of components
component = ["snake", "water", "gun"]

# Mapping components to numeric values
component_map = {"snake": 1, "water": -1, "gun": 0}

# Computer's choice
computer_choice = random.choice(component)  # Randomly select "snake", "water", or "gun"
computer = component_map[computer_choice]   # Map it to a numeric value

# User's choice
n = input("Enter Your Choice (Snake, Water, Gun): ").lower()

# Validate user input
if n not in component_map:
    print("Invalid choice! Please choose from 'Snake', 'Water', or 'Gun'.")
else:
    user = component_map[n]

    # Display choices
    print(f"Computer chose: {computer_choice.capitalize()}")
    print(f"You chose: {n.capitalize()}")

    # Check results
    if computer == user:
        print("The game is a draw!")
    else:
        if (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
            print("You win!")
        else:
            print("You lose!")
