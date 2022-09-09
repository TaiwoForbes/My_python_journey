f = open("forbes.txt", "r")
# By specifing the amount of character to read using the read() method will get the amount of the ccharacter requested
#text = f.read(21)
#text = f.readline() # Note: Read line is more like a generator, to get the next line of a file you will need to call the readline again
text = f.readlines() # Note: Read line acts like an iterator, which means it will keeping on reading the content of a file until the last line
print(text)
# Without using the close method, the interpreter will assume that some action will still be done with the file. Hence, leaving the file open 
f.close()