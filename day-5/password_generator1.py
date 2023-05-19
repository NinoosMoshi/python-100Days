import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '^', '@']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

result_list = []

print("Welcome to the PyPassword Generator!\n")

letters_num = int(input("How many letters would you like in your password?\n"))
for temp in range(0, letters_num):
    random_letter = random.randint(0, letters_num)
    result_list.append(letters[random_letter])

symbols_num = int(input("How many symbols would you like?\n"))
for temp in range(0, symbols_num):
    random_symbol = random.randint(0, symbols_num)
    result_list.append(symbols[random_symbol])

numbers_num = int(input("How many numbers would you like?\n"))
for temp in range(0, numbers_num):
    random_number = random.randint(0, numbers_num)
    result_list.append(numbers[random_number])

# print(result_list)


string_password = ''.join(result_list)

# print(string_password)

result_str = ''.join(random.choice(string_password) for i in range(len(string_password)))

print(f"Here is your password: {result_str}")






