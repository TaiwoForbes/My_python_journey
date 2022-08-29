num = int(input("Ener your number:"))

for i in range(0,num+1):
    for j in range(num - i):
        print(' ',end = '')
    for j in range(2*i -1):
        print("#",end = "")
    print()
numb = num / 2
for i in range(num-1):
    print(" ",end = "")
print("#",end='')
print()