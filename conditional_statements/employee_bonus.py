service_year = int(input("How many years have you worked in this company? "))
emp_salary = int(input("Enter your salary: "))
bonus = 0

if service_year > 5:
    if emp_salary < 20000:
        bonus = emp_salary * 0.2
    elif emp_salary < 50000:
        bonus = emp_salary * 0.1
    else:
        bonus = emp_salary * 0.05
        
    emp_salary += bonus
    
    print(f"Bonus Amount: {bonus}")
    print(f"Including bonus final salary is {emp_salary}")
else:
    print("Sorry! you are not eligible for bonus.")
