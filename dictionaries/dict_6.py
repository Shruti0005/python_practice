# Problem 2: Product Details
# Take input for: Product Name, Price, Quantity
# Store them in a dictionary.
# Then calculate and print:

product = {}

product['p_name'] = input("Enter product name: ")
product['price'] = float(input("Enter product price: "))
product['quantity'] = int(input("Enter product quantity: "))

total_cost = product['price'] * product['quantity']

print(f"Total cost = {total_cost}")
