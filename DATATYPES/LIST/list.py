list = [1,2,3,"Taiwo",12.3]
list2 = ['hello', 'world']

print(list)

print(list2)
print(list * 2)
print(list + list2)


#Convert a list of  string to an integer
items = ["1","2","3","4"] 
print(map(float,items))
print(items)
con = [int(item) for item in items]
print(con)