# Phone Book, Create a dictionary like:
phone_book = {
    "Rahul": 9876543210,
    "Amit": 9123456780,
    "Neha": 9988776655,
    "Nova": 8458283858,
    "Akshay": 6800210500
}
# Ask the user to enter a name.
# If the name exists, print the phone number.
# Otherwise, print "Contact not found".

name = input("Enter your name: ")

if name in phone_book:
    print(phone_book.get(name))
else:
    print("Contact not found.")