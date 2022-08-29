"""
    Write a program to sum the first natural number using while loop
"""

i = 0
sum = 0
num = int(input("Enter your number:"))
while i <= num:
    sum += i
    i += 1
print("The sum of first natural number is {}".format(sum))
    