lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for i in lst[1::2]:
    print(i)
""" Both loop behaves in the same manner """
for i in range(1,len(lst),2):
    print(lst[i])

