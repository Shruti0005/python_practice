user_name = "admin"
pass_word = "1234"

username = input("Enter you username: ")
password = input("Enter you password: ")

if user_name == username and pass_word == password:
    print("Login Successful.")
elif user_name != username:
    print("Invalid Username.")
else:
    print("Invalid Password.")
