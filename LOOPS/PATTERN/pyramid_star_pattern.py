num = int(input("Ener your number:"))

for i in range(0,num):
    for j in range(num - i):
        print(' ',end = '')
    for j in range(2*i -1):
        print("*",end = "")
    print("\n",end = '')

print()


