try:
    f = open("a.txt", encoding= "utf-8")
    line = f.read()
    
except FileNotFoundError as ex:
    print("This file doesnt exit")
    print(ex.filename)
else:
    print(line)
    f.close()
finally:
    print("I will always get executed no matter what")


