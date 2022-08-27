"""
    Write a program to check whether a username  contain less than 10 character
"""
username = input("Enter your Username: ")
if len(username) < 10:
    print("Less than 10,your username is {} character long".format(len(username)))
else:
    print("greater than 10,your username is {} character long".format(len(username)))