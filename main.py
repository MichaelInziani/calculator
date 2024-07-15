
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

first_number = int(input("Enter the first number: "))

for symbol in operator:
    print(symbol)

operator_symbol = input("Select an operator from the ones above: ")

second_number = int(input("Enter the second number: "))

calculation_function = operator[operator_symbol]
answer = calculation_function(first_number, second_number)

print(f"{first_number} {operator_symbol} {second_number} = {answer} ")