"""Write a program that checks the type of a variable"""

a = int(input("Enter 1 for int:\nEnter 2 for string:\nEnter 3 for float:\n"))

if a == 1:
    try:
        a = int(input("Enter a number: "))
        print(type(a), a)
    except ValueError:
        print("Only Integers is allowed")
elif a == 2:
    a = (input("Enter a string: "))
    print(type(a), a)
elif a == 3:
    a = float(input("Enter a number with decimals: "))
    print(type(a), a)