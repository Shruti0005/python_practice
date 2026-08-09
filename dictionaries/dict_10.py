# Find the student with the highest marks from a dictionary like:
students = {
    "Rahul": 450,
    "Amit": 420,
    "Neha": 480,
    "Shree": 470
}

highest_marks = max(students, key=students.get)

print(highest_marks)
