"""
Write a program to print third, fifth , and seventh element in a list using the enumerate function
"""

lst = [2,5,6,7,'Taiwo', "mariam","shola","tunde"]

for index,item in enumerate(lst):
    # Index + 1 to match the element in the list, since index starts from Zero
    if index + 1  == 3 or index +1 == 5 or index +1 == 7:
        print(item)