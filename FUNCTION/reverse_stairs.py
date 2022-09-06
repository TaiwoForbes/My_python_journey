def reverse_stairs(num):
    """This function prints a reverse stairs
    """
    for i in range(num):
        for j in range(num - i):
            print("*",end = "")
        print()
print(reverse_stairs(11))