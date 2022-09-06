add_tuple = [x + y for x,y in  [(1, 2), (3, 4), (5, 6)]]
print(add_tuple)
for x,y in  [(1, 2), (3, 4), (5, 6)]:
    print(x + y)
print()

#  Count the numbers in `range(1000)` that are even and contain the digit `9:
sum = 0
for i in range(1000):
    if i % 2 == 0 and "9" in str(i):
            sum = sum + 1
            
print((sum))