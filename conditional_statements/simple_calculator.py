number_1 = int(input("Enter the first value: "))
number_2 = int(input("Enter the second value: "))

operator = input("Enter the operetor as given: \n+ for addition\n- for subtraction\n* for multiplication\n/ for division\n")
result = 0

if operator == "+":
    result = number_1 + number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "*":
    result = number_1 * number_2
elif operator == "/":
    if number_2 != 0:
        print("Can't divide by zero.")
    else:
        result = number_1 / number_2
else:
    print("You enter symbol which is not in option.")

print(result)