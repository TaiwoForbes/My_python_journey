"""
    Write a program to greet all person names stored in a list L1 and which starts with "s"
"""

L1 = ["Harry", "Saham", "Sacham","Rahaul"]

for names in L1:
    if names[0] == 'S':
        print("hello" + " " + names)