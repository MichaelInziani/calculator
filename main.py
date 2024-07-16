from art import logo
#Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def subtract(n1, n2):
    return n1-n2

#Multiplicatiom
def multiply(n1, n2):
    return n1*n2

#Division
def divide(n1, n2):
    return n1/n2

operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    first_number = float(input("Enter the first number: "))

    for symbol in operator:
        print(symbol)

    should_continue = True
    while should_continue:
        operator_symbol = input("Select an operator from the ones above: ")
        second_number = float(input("Enter the next number: "))
        calculation_function = operator[operator_symbol]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operator_symbol} {second_number} = {answer} ")

        next_number = input(f"Enter 'y' to continue calculating with {answer} or 'n' to start a new calculation: ")
        if next_number == "y":
            first_number = answer
        elif next_number == "n":
            should_continue = False
            calculator()
        else:
            print("Invalid input. Please try again")
            should_continue = False
            calculator()

calculator()