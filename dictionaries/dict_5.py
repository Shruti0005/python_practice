# Student Marks, Take input for: Name, Math Marks, Science Marks, English Marks
# Store them in a dictionary.
# Then print:

student = {}

student['name'] = input("Enter your name: ")
student['math'] = float(input("Enter math marks: "))
student['science'] = float(input("Enter science marks: "))
student['english'] = float(input("Enter english marks: "))

count_subject = 0
total_marks = 0

for keys, value in student.items():
    if keys == 'name':
        continue
    
    count_subject += 1
    total_marks += value

average = total_marks/count_subject

print(f"Name : {student.get('name')}\nTotal Marks : {total_marks}\nAverage : {average}")
