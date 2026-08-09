student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python",
    "city": "Pune"
}
# Remove the "course" key.
del student["course"]
print(student)

# Remove the last inserted item using a dictionary method.
student.popitem()
print(student)

# Delete only the "age" key using another approach (not pop()).
del student['age']
print(student)

# Delete the entire dictionary, then try printing it. Observe and explain what happens.
"""after use del student dictionary completly delete. 
Whenever we try to print student dictionary it show error: 
NameError: name 'student' is not defined
"""
del student 
