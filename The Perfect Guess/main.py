
import random

def play_guessing_game():
    target = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100!")
    
    while True:
        guess = int(input("Guess the number: "))
        attempts += 1
        
        if guess == target:
            print(f"You have guessed the number {target} correctly in {attempts} attempts")
            break
        elif guess > target:
            print("Lower number please")
        else:
            print("Higher number Please")

play_guessing_game()