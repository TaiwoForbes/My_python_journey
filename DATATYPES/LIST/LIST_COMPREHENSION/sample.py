a =[x*x for x in (1,2,3,4) if x % 2 == 0  ]
print(a)

a =[x*x for x in (1,2,3,4)]
print(a)

squares = []
for x in [1,2,3,4]:
    squares.append(x*2)
print(squares)


# Get the list of uppercase character of a string
string =[s.upper() for s in "hello world"]
print(string)

# Strip of comma or any symbols from end of a string using the strip function
string2= [s.strip(',') for s in ["these,", "words,","mostly" ,"have,comma,"]]
print(string2)

# Organize letters in words  more reasonably - in alphabetical order
sentence = 'Beautiful is better than ugly'
order = ["".join(sorted(word,key = lambda x : x.lower())) for word in sentence.split()]
print(order)