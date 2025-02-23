
from art import logo

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
    "/": divide,
}

def calculator():
    print(logo)
    continue_accumulate = True
    num1 = float(input("Enter first number: "))
    while continue_accumulate:
        for operator in operations:
            print(operator)
        operator = input("Choose an operation: ")
        num2 = float(input("Enter the next number: "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        should_continue = input(f"Enter 'y' to continue working with {answer}, or enter 'n' to exit the program.")
        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            continue_accumulate = False
            print("\n"*20)
            calculator()
        else:
            return print("Invalid input")

calculator()



