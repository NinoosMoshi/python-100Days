import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # [ninos, nahrain, matthew, daniel]

names_length = len(names)

random_number = random.randint(0, names_length - 1)

print(f"{names[random_number]} is going to buy the meal today!")

