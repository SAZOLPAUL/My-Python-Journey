import random

while True:

    secret_number = random.randint(1, 25)

    while True:

        user_number = int(input("Enter a number between 1-25: "))

        if user_number < secret_number:
            print("Too Low")

        elif user_number > secret_number:
            print("Too High")

        else:
            print("Your answer is correct")
            break

    play_again = input("Play Again? (y/n): ")

    if play_again.lower() != "y":
        print("Thanks for playing!")
        break