number = int(input("Enter number to check: "))

if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif number < 0:
    if number % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")
    
