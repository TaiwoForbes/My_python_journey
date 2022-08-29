"""
    Write a multiplication table of 10 in reversed order
"""
num = int(input("Ener your number:"))

for i in range(num,0,-1):
    multiple = i * num
    print("{} X {} = {}".format(num,i,multiple))