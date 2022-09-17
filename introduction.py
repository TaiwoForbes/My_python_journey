ls = ["taiwo", "kehinde", 4,5,6,5,6,7,8]
for i,item in enumerate(ls):
    if i == 3 or i == 5 or i == 7:
        if item < len(ls):

            print(item,end= "")
        else:
            print()