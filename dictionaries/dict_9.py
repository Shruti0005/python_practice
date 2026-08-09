# Count the frequency of each word in a sentence.
# Example:
# Input: "python is easy python is fun"
# Output:
# {
#     'python': 2,
#     'is': 2,
#     'easy': 1,
#     'fun': 1
# }

sentence = input("Write sentence here: ").split(" ")
word = {}

for i in sentence:
    word_count = 0
    for j in sentence:
        if i == j:
            word_count += 1
    word[i] = word_count

print(word)