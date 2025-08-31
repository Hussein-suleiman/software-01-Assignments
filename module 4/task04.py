import random

Secret = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < Secret:
        print("Too low")
    elif guess > Secret:
        print("Too high")
    else:
        print("Correct!")
        break
