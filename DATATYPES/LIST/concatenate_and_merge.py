import itertools


alist = ['a1', 'a2', 'a3'] 
blist = ['b1', 'b2', 'b3']

for a,b in zip(alist,blist):
    print(a,b)
print(len(list(zip(alist, blist))))

# Concatenating list with different length
import itertools
alist = ['a1', 'a2', 'a3'] 
blist = ['b1'] 
clist = ['c1', 'c2', 'c3', 'c4']

for a,b,c in itertools.zip_longest(alist,blist,clist):
    print(a,b,c)
print(len(list(zip(alist,blist,clist))))
