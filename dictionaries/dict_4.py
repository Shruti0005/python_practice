student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}
# Print the value of "age" using get().
print(student.get('age'))

# Print the value of "course" using get().
print(student.get('course'))

# Print the value of "city" using get(). Observe what happens.
if 'city' in student:
    print(f"city exists: {student.get('city')}")
else:
    print("city key not found.")