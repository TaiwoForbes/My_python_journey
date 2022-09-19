'''
Write a list comprehension to print a list which contains the multiplcation table of a user entered number
'''
num = int(input("Enter a number: "))
mult = [x * num for x in range(1, 13)]
table = ""
for index, i in enumerate(mult):
    table += "{} X {} = {}\n".format(num, index + 1, i)


# Store the multiplication table stored in this program in a file name table.txt
with open("table.txt", "w") as f:
    f.write(table)
