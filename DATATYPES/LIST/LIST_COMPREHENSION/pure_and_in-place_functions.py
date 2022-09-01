"""
An in place function wont work in a comprehension
since an in place function modifies the exsting object,
they are also call side effect function
"""
in_place = [x.sort() for x in [[2, 1], [4, 3], [0, 1]]]
#  This would return None
print(in_place)
print()

"""
A pure function when used with a comprehension would always return a value 
"""
pure = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
#  This would return the value
print(pure)
print()

"""
In some situation, in place function are suitable for  list  comprehension. For example - random.randrange() 
"""
from random import randrange
rand = [randrange(1,7) for _ in range(10)]
print(rand)
print()

'''' White spaces is allowed in a list comprehension'''
white_space  = [   
                    x for x    
                    in 'foo'    
                    if x not in 'bar' 
               ]
print(white_space)
print()
