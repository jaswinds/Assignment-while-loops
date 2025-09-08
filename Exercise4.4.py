import random

num = random.randint(1, 10)  # Computer picks a number

while True:
    guess = int(input("Guess a number (1-10): "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print("Correct! You got it!")
        break
