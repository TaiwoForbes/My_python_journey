n = int(input("Enter your num : "))

"""
    This prints pyramid
"""
for i in range(n+1):
    for j in range(n,i,-1):
        print(" ",end = "")
    for j in range(i):
        print("*",end="")
    for j in range(i-1):
        print("*",end="")
    print()

print()

"""
    This prints reverse stairs
"""
for i in range(n):
    for j in range(n,i,-1):
        print("*",end = "")
    print()

"""
    This prints stairs
"""
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()

print()

"""
    This prints reverse pyramid
"""
for i in range(n+1):
    for j in range(i):
        print(" ",end= "")
    for j in range(n,i,-1):
        print("*",end = "")
    for j in range(n,i-1,-1):
        print("*",end = "")
    print()

print()

"""
    This prints diam
"""
for i in range(n):
    for j in range(n,i,-1):
        print(" ",end = "")
    for j in range(i):
        print("*",end="")
    for j in range(i-1):
        print("*",end="")
    print()
for i in range(n+1):
    for j in range(i):
        print(" ",end= "")
    for j in range(n-1,i,-1):
        print("*",end = "")
    for j in range(n-1,i-1,-1):
        print("*",end = "")
    print()


