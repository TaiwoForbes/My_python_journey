def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def getPrime(max_num):
    list_of_prime = []
    for num in range(2, max_num):
        if isPrime(num):
            list_of_prime.append(num)
    return list_of_prime


prime = int(input("Enter the max value of primes you wanna check: "))
list_of_prime = getPrime(prime)
print(list_of_prime)

