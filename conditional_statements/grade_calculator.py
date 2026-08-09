student_mark = int(input("Enter your mark here: "))

if student_mark < 0 or student_mark > 100:
    print("Invalid Marks")
elif student_mark >= 90:
    print("A grade")
elif 80 <= student_mark < 90:
    print("B grade")
elif 70 <= student_mark < 80:
    print("C grade")
elif 60 <= student_mark < 70:
    print("D grade")
else:
    print("Fail")
