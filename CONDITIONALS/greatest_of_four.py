"""
    Write a program to check  the grestest of four number entered by the user
"""

num1,num2,num3,num4 = input("Enter four numbers:").split()
num1,num2,num3,num4 = int(num1),int(num2),int(num3),int(num4)


if num1 > num2 and num1 > num3 and num1 > num4:
    print("Num 1 is the greatest: {}".format(num1))
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("Num 2 is the greatest: {}".format(num2))
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("Num 3 is the greatest: {}".format(num3))
else:
    print("Num 4 is the greatest: {}".format(num4))

    