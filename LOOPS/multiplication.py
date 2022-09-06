"""
    Write a program to print the multiplication of a given number
"""
num = int(input("Enter your number: "))

for i in range(1,13):
    multiple = i * num
    print("{:d} X {:d} = {:d}".format(num,i,multiple))
    