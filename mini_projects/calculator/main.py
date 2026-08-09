import art

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

def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input(f"What's the operator?: ")
        num2 = float(input("What's the second number?: "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new: ").lower()
        if choice == "y":
            num1 = result
        else:
            should_continue = False
            print("\n"*50)
            calculator()

calculator()

