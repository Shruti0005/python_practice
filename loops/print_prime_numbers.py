#Print all prime numbers from 1 to 100.

for i in range(1, 100):
    is_prime = True
    
    if i < 2:
        is_prime = False
        
    else:
        for j in range(2, i):
            if i % j == 0:
               is_prime = False
               break
        
        if is_prime:
            print(i)
    
    
