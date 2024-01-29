import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        #print(random_number)
        guess = int(input(f"Guess a number between 1 and {x}: "))
        #print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low :C')
        elif guess > random_number:
            print('Sorry, guess again. Too high :C')

    print(f"Yay! Congrats! You have guess the number: {random_number}")

guess(10)