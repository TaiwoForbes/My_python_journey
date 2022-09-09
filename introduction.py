def func(params):
    for value in params:
        print ('Got value {}'.format(value))
        if value == 1:
        # Returns from function as soon as value is 1
            print (">>>> Got 1")
            return
        print ("Still looping")
    return "Couldn't find 1"
print(func([5, 3, 2, 8, 9]))