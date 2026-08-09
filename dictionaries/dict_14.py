# Student Grade System
# Create another dictionary: convert marks into grade example: "Math": 70 -> "Math": "B" using conditions.
marks = {
    "Math": 85,
    "Science": 72,
    "English": 91,
    "History": 83,
    "Geography": 90
}

def convert_Grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 65:
        return "B"
    elif mark >= 45:
        return "C"
    else: 
        return "Fail"
    
grade = {}
for k, v in marks.items():
    grade[k] = convert_Grade(v)
    
print(grade)
