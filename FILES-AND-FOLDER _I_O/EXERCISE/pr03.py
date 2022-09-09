""" Write a program to generate a multiplication table from 2- 20
    and write this to a diffrent files. Place this files in a folder for a 13 years old.
"""

for i in range(2, 21):
    tables = ''
    for j in range(1, 13):
        multiple = i * j
        tables += "{:d} X {:d} = {:d}\n".format(i, j, multiple)

    with open("tables/multiplication_table_of_{:d}.txt".format(i), 'w') as f:
        f.write(tables)
