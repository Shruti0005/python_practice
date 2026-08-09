print("Welcome! to rollercoster.")
Height = int(input("Enter you Height: "))
bill = 0

if Height >= 120:
    print("Your welcome! You'r eligible for ride.")
    age = int(input("Enter your age: "))

    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Hey! Everything going to be ok. Here is free ticket from us.")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_Photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_Photo == "y":
        bill += 3
    
    print(f"Your final bill is ${bill}")

else:
    print("Sorr! your hight not match to our policy. So, you'r not eligible for ride.")
