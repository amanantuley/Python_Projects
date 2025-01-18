import random

print("Welcome to the number guessing game ...")

comp = random.randint(1,100)
n = -1
guesses = 0
while(n != comp):
    guesses = guesses + 1
    n = int(input("Guess a Number (1-100)::"))
    if(n > comp):
        print("Guess a Smaller number..")
    elif(n < comp):
        print("Guess a Higher Number..")
    

print(f"You have Guessed the correct number {comp} in {guesses} chance")

