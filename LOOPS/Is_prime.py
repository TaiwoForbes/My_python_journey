"""
    Write a program to check whether a given number is prime or not
"""

num = int(input("Ener your number:"))

for i in range(2,num):
    if num % i == 0:
        print("Is not prime")
        break
else:
    print("Is prime")