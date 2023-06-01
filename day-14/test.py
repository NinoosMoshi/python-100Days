import random
from game_data import data
from art import logo,vs


def format_a_b(account):
    account_a_name = account['name']
    account_a_description = account['description']
    account_a_country = account['country']
    return f"{account_a_name}, is {account_a_description}, located in {account_a_country}"


def check_followers(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare 'A' Followers: {format_a_b(account_a)}")
print(vs)
print(f"VS 'B' Followers: {format_a_b(account_b)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

followers_a = account_a['follower_count']
followers_b = account_b['follower_count']

print(f"followers 'A' is: {followers_a}")
print(f"followers 'B' is: {followers_b}")

is_correct = check_followers(guess, followers_a, followers_b)

if is_correct:
    print(f"You're right! Current score: ")
else:
    print(f"Sorry, That's wrong. Final score: ")