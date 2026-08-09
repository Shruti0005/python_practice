# Second Highest Marks
students = {
    "Rahul": 450,
    "Amit": 420,
    "Neha": 480,
    "Shree": 470,
    "Riya": 460
}

highest = 0
secondHighest = 0

for mark in students.values():
 
    if mark > highest:
        second_highest = highest
        highest = mark
    
    elif highest > mark > second_highest:
        secondHighest = mark
        
print(secondHighest)