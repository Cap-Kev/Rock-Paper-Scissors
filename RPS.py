import sys
import random

#Take input from the user
playerChoice = input("Enter...\n1 for Rock\n2 for Scissors\n for \n3 for Paper\n\n")

#Cast the player's choice to an integer
player = int(playerChoice)

#Set up the parameters of the game between 1 and 3 and exit the program by importing the sys module
if player < 1 or player > 3:
    sys.exit("Please enter a number between 1 and 3")

#Set up the choice of the computer and randomise it by importing the random module
computerChoice = random.choice("123") 

#Cast the computer's choice to an integer
computer = int(computerChoice)

#Output the choice of each party before the results
print(f"You chose: {player}")
print(f"Computer chose: {computer}")

#Set up the game logic
if player == 1 and computer == 2:
    print("You win🏆.")
elif player == 2 and computer == 3:
    print("You win🏆.")
elif player == 3 and computer == 1:
    print("You win🏆.")
elif player == 2 and computer == 3:
    print("You win🏆.")
elif player == computer:
    print("It's a tie🤝.")
else:
    print("🐍Python wins.")
