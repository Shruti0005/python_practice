# Count the frequency of each character in a string.
# Example:
# Input: banana
# Output:
# {
#     'b': 1,
#     'a': 3,
#     'n': 2
# }

text = input("Enter word: ")
char = {}

for i in text:
    char_count = 0
    for j in text:
        if i == j:
            char_count += 1
    char[i] = char_count
    
print(char)