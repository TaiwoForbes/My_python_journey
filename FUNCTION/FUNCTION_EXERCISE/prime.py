def isPrime(num):
    if num < 2: # Any number less than 2 is not consider a prime number. Hence, the program returns False 
        return False
   
    else: # otherwise, if the number is greater than 2
        for i in range(2,num):
            if num % i == 0: # If the number is prime, return True. Otherwise return False
                return False
             
        return True

#print(isPrime(9))