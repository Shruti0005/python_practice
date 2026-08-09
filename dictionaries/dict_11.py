# Reverse a Dictionary (convert keys to values)
student = {
    "Rahul": 101,
    "Amit": 102,
    "Neha": 103,
    "Hari": 104,
    "Nayra": 105,
    "Aahan": 106
} 

temp = {}
for k, v in student.items():
    temp[v] = k

student = dict(temp)

print(student)