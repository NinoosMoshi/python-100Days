import random

# 1 means Heads 0 means Tails

random_coin = random.randint(0, 1)

if random_coin == 0:
    print("Tails")
else:
    print("Heads")
