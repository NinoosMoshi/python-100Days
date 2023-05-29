from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n")

difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = random.randint(1, 100)
is_continue = False

print(random_number)

attempt_hard_num = 5
attempt_easy_num = 10
i = 1

if difficulty_type == 'hard':
    print(f"You have {attempt_hard_num} attempts remaining to guess the number.")
    while i <= attempt_hard_num:
        guess_number = int(input("Make a guess: "))
        if guess_number > random_number:
            print("Too high.\nGuess again.")
            attempt_hard_num -= 1
            print(f"You have {attempt_hard_num} attempts remaining to guess the number.")
        elif guess_number < random_number:
            print("Too low.\nGuess again.")
            attempt_hard_num -= 1
            print(f"You have {attempt_hard_num} attempts remaining to guess the number.")
        else:
            print(f"You ot it! The answer was {random_number}.")

elif difficulty_type == 'easy':
    print(f"You have {attempt_easy_num} attempts remaining to guess the number.")
    while i <= attempt_easy_num:
        guess_number = int(input("Make a guess: "))
        if guess_number > random_number:
            print("Too high.\nGuess again.")
            attempt_easy_num -= 1
            print(f"You have {attempt_easy_num} attempts remaining to guess the number.")
        elif guess_number < random_number:
            print("Too low.\nGuess again.")
            attempt_easy_num -= 1
            print(f"You have {attempt_easy_num} attempts remaining to guess the number.")
        else:
            print(f"You ot it! The answer was {random_number}.")

else:
    print("you write a wrong word, please choose word 'easy' or 'hard'")
