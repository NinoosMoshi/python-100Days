import random

# random integer
random_int = random.randint(1, 10) # random between 1 and 10 including 1 and 10
print(random_int)


# random float
# random() : generate random between 0 and 1 but not include 1 actually will be '0.999999'
random_float = random.random()
print(random_float)

# random between 0 - 5
print(random_float * 5)  # 0.00000 - 4.99999
