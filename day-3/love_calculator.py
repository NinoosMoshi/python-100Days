print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_names = (name1 + name2).lower()

t = combine_names.count('t')
r = combine_names.count('r')
u = combine_names.count('u')
e = combine_names.count('e')

true = t + r + u + e

l = combine_names.count('l')
o = combine_names.count('o')
v = combine_names.count('v')
e = combine_names.count('e')

love = l + o + v + e

true_love = str(true) + str(love)

true_love_int = int(true_love)

if true_love_int < 10 or true_love_int > 90:
    print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif 40 < true_love_int < 50:
    print(f"Your score is {true_love_int}, you are alright together.")
else:
    print(f"Your score is {true_love_int}.")
