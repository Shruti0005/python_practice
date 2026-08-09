# Inventory System
# Ask the user for a product name.
# If it exists, print the quantity.
# Otherwise, print "Product not available".

inventory = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 10
}

p_name = input("Enter the product name: ")

if p_name in inventory:
    print(f"Quantity: {inventory[p_name]}")
else: 
    print("Product not available.")
