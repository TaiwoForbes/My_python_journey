# Replication 
lst = ["blair"] * 3
print(lst)

b = [1,2,3,4] * 5
print(b)
print()

# Element deletion
a = list(range(10))
del a[::2]
print(a)
print()

del a[-1]
print(a)

del a[:]
print(a)

# Copying
a = [1,2,3,4]
b = a
print(b)
b.append(6)
print(b)
print(a)
print()

# Creating a new copy of a list using list method or list_name[:]
b = list(a)
c = a[:]
print()

# Reversing a list
num = [1,2,3,4,5,6]
num.reverse()
print(num)
int = [24,45,67,90]
rev = int[::-1]
print(rev)
print()

# Insert to a specific index value
alist = [123, 'xyz', 'zara', 'abc'] 
alist.insert(3, [2009]) 
print("Final List :", alist)
print()

# Removing duplicate value from a list can be done  by converting the list a set
names = ["aixk", "duke", "edik", "tofp", "duke"] 
a = list(set(names))
print(a)
print()

# Accessing value in a nested list
alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
print(alist[1][1][2])
alist[0][0].append(11) 
print(alist[0][0][2])
print(alist)
print()
print()

for row in alist:
    for col in row:
        print(col)
print()


alist[1].insert(2, 15)
print(alist)

print()

# Using slice in nestec loop
print(alist[1][1:])

