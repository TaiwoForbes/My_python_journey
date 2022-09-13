def check(string, value):
    """ This count the occurence of character in a string"""
    count = 0
    for i in string:
    
        if i == value:
            count = count + 1
    return(count)
        

string = "taaaiwo"
value = "a"
c = check(string, value)
print(c)