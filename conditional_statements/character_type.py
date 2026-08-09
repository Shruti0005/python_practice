single_character = input("Enter only single characters: ")[0]

if "A" <= single_character <= "Z":
    print("Uppercase alphabet.")
elif "a" <= single_character <= "z":
    print("Lowercase alphabet.")
elif "0" <= single_character <= "9":
    print("Digit.")
else:
    print("Special character.")

