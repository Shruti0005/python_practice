# Create an empty dictionary.
# Ask the user: Name, Age, gender, status
# Store info in the dictionary.
# Example:
# {
# 'name':'Rahul',
# 'age':20
# }

user = {}

user['name'] = input("Enter your name: ")
user['age'] = int(input("Enter your age: "))
user['gender'] = input("Enter your gender: ")
user['status'] = input("Enter you status ex: single or married: ")

print(user)