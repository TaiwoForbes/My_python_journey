list = ['name','age','school']
list2 = [1,2,3]
dict = {key:val for (key,val) in zip(list,list2)}
print(dict)



dict = {"color": 22, "age": 21, "amount":24}
dict = {key:val for (key,val) in dict.items() if val % 2 == 0}
print(dict.values())



