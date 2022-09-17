"""
Write a program to open a file.
If the file is not present,
a message without exiting the program should be printed
"""

try:
    with open("text.txt", "r" ) as f:
        d = f.read()
        print(d)
except FileNotFoundError:
    print("File not found")