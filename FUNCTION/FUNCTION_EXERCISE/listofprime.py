import enum
from prime import isPrime

def listofprime(start, end):
    prime_list = []
    for i in range(start,end + 1):
        if isPrime(i):
            prime_list.append(i)
    total = 0    
    for i,num in  enumerate(prime_list):
        total += 1
        print("{}.  ".format(i+1),num)


    if total < 2:
        print("There are {}  prime number between {} and {}.  ".format(total,start,end))
    else:
        print("There are {}  prime numbers between {} and {}.  ".format(total,start,end))


print(listofprime(10,14))


