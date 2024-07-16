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
    if n2 == 0:
        return 0
    return n1/n2

operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def takeOperation():
    operator_symbol = input("Select an operator from the ones above: ")

    if operator_symbol not in operator.keys():
        print("Invalid input. Please select an operator from the ones given.")
        return takeOperation()
    else:
        return operator_symbol

def calculator():
    print(logo)
    #first_number = float(input("Enter first number: "))
    first_number = ''
    while first_number is not float:
        try:
            first_number = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    should_continue = True
    while should_continue:
        for symbol in operator:
            print(symbol)
        #operator_symbol = input("Select an operator from the ones above: ")
        operation = takeOperation()
        second_number = ''
        while second_number is not float:
            try:
                second_number = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        #second_number = float(input("Enter the next number: "))
        calculation_function = operator[operation]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer} ")

        next_number = input(f"Enter 'y' to continue calculating with {answer} or 'n' to start a new calculation: ").lower()
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