from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")  # key  +

num2 = float(input("What's the second number?: "))

calculation_function = operations[operation_symbol]  # get a value of key ex: add

#   add(22, 11)
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

flag = False
while not flag:
    symbol_check = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ").lower()
    if symbol_check == 'y':
        operation_symbol = input("Pick an operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(first_answer, num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        first_answer = second_answer
    elif symbol_check == 'n':
        flag = True
    else:
        print("you have to write 'y' or 'n'")
