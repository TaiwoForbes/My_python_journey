# The regular expression is used to find a particular character in a string
# In order to use this, we need to import a library called re
# The "r" in from of the specified characters is used to get the raw string, meaning the literal string
import re
test_strings = "123abc456789abc1234ABC"
pattern = re.compile(r"abc") # Note: That the regular expression re method is case sensitive
matches = pattern.finditer(test_strings)
#matches = pattern.search(test_strings)
#matches = pattern.match(test_strings)
#matches = pattern.findall(test_strings)
# The above code can also be written like this
#matches = re.finditer(r"abc", test_strings) # This will also give similar result to the one above

# We have three main method under the re module
# finditer() --> This get all the pattern and where they care found
# match() -----> This check if the pattern to find is at the beginning of the string. This is not iteratble
# findall() ---> This find all the pattern and print it on the console without showing where they are found. Not iterable as well
# search() ----> This scans through the string and return any location the patterns are found
#print(matches)


# We can also be more specific with our patterns output by using
# span()
# group()
# start()
# end()
for match in matches:
    print(match.span())
    print(match.start())
    print(match.end())
    print(match.group())
    #print(match)
print()

# To modify a string, we two method to do that, which are:
# split() ---> This will split the expression into a list
# sub()   ---> This will find all the sub strings

test_strings = "123abc456789abc1234ABC"
pattern = re.compile(r"abc") 
split = pattern.split(test_strings)
print(split) # Any where abc is encountered, it split it from the strings
print()

test_strings = "hello world, you are the best world"
pattern = re.compile(r"world") 
sub_string = pattern.sub("planet",test_strings)
print(sub_string) # world will be switched with planet