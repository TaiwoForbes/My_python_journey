"""
    Write a program to find the grade of a student from the following schemes
    90 ---- 100 ----> A
    80 ----- 90 ----> B
    70 ----- 80 ----> C
    60 ----- 70 ----> D
    < 50 -----------> F

"""


scores = int(input("Enter your score: "))

if scores >= 90 and scores <= 100:
    print("A")
elif scores >= 80 and scores <= 90:
    print("B")
elif scores >= 70 and scores <= 80:
    print("c")
elif scores >= 60 and scores <= 70:
    print("D")
elif scores < 50:
    print("F")