from sys import argv
"""Sum the number of argument which should not be greater than 2 and only + sign"""
if len(argv) == 4:
    if argv[2] == "+":
        a = int(argv[1])
        add = argv[2]
        b = int(argv[3])
        print(f"{a} + {b} =", a+b)
    else:
        print("Additions only")
else:
    print('You must provide two arguments')