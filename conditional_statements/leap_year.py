check_year_type = int(input("which year's do you want to check? "))

if (check_year_type % 4 == 0 and check_year_type % 100 != 0) or check_year_type % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")
