""" Write a program to check whether the word twinkle exit in a file or not """

with open("poem.txt", "r") as f:
    line = f.read()

    if "twinkle" in line:
        print("True")
    else:
        print("False")