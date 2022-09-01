list = [1,2,2,2,3,4,5]
list.append(10)
print(list)

list.extend({6,7,8})
print(list)

list.extend(range(89,95))
print(list)

x =list.index(7)
print(x)

print(list.index(7,7))
list.insert(0,22)
print(list)

list.pop(1)
print(list)

list.pop()
print(list)

list.remove(22)
print(list)

list.reverse()
print(list)

a = list.count(2)
print(a)
list.sort()
print(list)

list.sort(reverse = True)
print(list)