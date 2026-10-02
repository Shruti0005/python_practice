#Check whether a number is prime.
number = int(input("Enter number: "))
is_prime = True

if number < 2:
    is_prime = False
    
else:
    for i in range(2, number):   
        if number % i == 0:
           is_prime = False
    
    if is_prime:
        print("Prime number")
    
    else:
        print("Not prime number")
