bill = int(input("Enter bill here: "))
discount = 0

if bill >= 5000:
    discount = bill * 0.2
elif bill >= 3000:
    discount = bill * 0.1
elif bill >= 1000:
    discount = bill * 0.05
else:
    print("No discount")
    
print(f"Your discount is {discount}")
total_bill = bill - discount
print(f"Final amount is {total_bill}")
