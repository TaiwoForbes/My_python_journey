"""
    Write a program to calculate the factorial of a given number
"""

num = int(input("Enter your number: "))

factorial = 1
for i in range(1,num + 1):
    factorial *= i 
    print("The factorial of {} is {}".format(num, factorial))