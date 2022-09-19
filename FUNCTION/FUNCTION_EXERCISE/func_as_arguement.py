def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def listOfOdd(list, func):
    oddlist = []
    for i in list:
        if func(i) == True:
            oddlist.append(i)
    return oddlist



lst = range(1,100,5)
print(listOfOdd(lst, is_odd))