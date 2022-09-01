cond = [x for x in range(10) if x % 2 == 0] 
print(cond)

# The above code can be done in the same manner below
even = []
for x in range(10):
    if x % 2 == 0:
        even.append(x)
print(even)


numbers = [] 
for x in range(10):    
    if x % 2 == 0:        
        temp = x
        print(temp,"if")  
    else:        
        temp = -1
        print(temp,"else")    
    numbers.append(2 * temp + 1) 
print(numbers) 