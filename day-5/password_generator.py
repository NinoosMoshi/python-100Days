import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '^', '@']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# # Easy way
# password = ""
#
# print("Welcome to the PyPassword Generator!\n")
#
# letters_num = int(input("How many letters would you like in your password?\n"))
# for temp in range(0, letters_num):
#     random_letters = random.choice(letters)  # choice(): give you random letters list
#     password += random_letters
#
# symbols_num = int(input("How many symbols would you like?\n"))
# for temp in range(0, symbols_num):
#     random_symbols = random.choice(symbols)
#     password += random_symbols
#
# numbers_num = int(input("How many numbers would you like?\n"))
# for temp in range(0, numbers_num):
#     random_numbers = random.choice(numbers)
#     password += random_numbers
#
# print(password)

# Hard way
password_list = []

print("Welcome to the PyPassword Generator!\n")

letters_num = int(input("How many letters would you like in your password?\n"))
for temp in range(0, letters_num):
    random_letters = random.choice(letters)  # choice(): give you random letters list
    # password_list += random_letters  # it's working as well
    password_list.append(random_letters)

symbols_num = int(input("How many symbols would you like?\n"))
for temp in range(0, symbols_num):
    random_symbols = random.choice(symbols)
    # password_list += random_symbols
    password_list.append(random_symbols)

numbers_num = int(input("How many numbers would you like?\n"))
for temp in range(0, numbers_num):
    random_numbers = random.choice(numbers)
    # password_list += random_numbers
    password_list.append(random_numbers)

print(password_list)
random.shuffle(password_list)  # random elements in list
print(password_list)

password = ""
for temp in password_list:
    password += temp
print(password)

# for temp in range(0, len(password_list)):
#     random_password = random.choice(password_list)
#     print(random_password, end='')
