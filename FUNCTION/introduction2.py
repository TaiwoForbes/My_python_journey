#  Defining a function with arguments
def divide(dividend,divisor):
    # This can be done like this, 
    #return dividend / divisor
    print(dividend / divisor)

print(divide(9,2)) # This will return 4.5

# Defining s function with multiple arguments
def func(value1,value2,value3 = 40):
    return "{} {} {}".format(value1,value2,value3)
print(func(1,2,60))
print(func(1,"a"))

# Defining function with list arguments
def func2(mylist):
    for i in mylist:
        print(i,end= " ")
print(func2([1,4,"a"]))
# It can be paased as a function call itself
func2([1,2,3,5,7])
