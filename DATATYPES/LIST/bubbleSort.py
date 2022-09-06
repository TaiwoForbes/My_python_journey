import random
lst = []
for i in range(5):
    lst.append(random.randrange(1,9))

for i in range(len(lst)-1):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            tmp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = tmp
        print(lst)
