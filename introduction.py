list = [1,"tunde",3,4]

for i in list:
    print(i)
    if type(i) is not int:
        break
else:
    print("no exceptions")