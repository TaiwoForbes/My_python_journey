import sys
services = input("Are you traveling: [y/n]")
user_info = []
while services == "y":
    num = int(input("Enter the number of people traveling: \n"))
    for i in range(1, num+1):
        name = input("Enter name: ")
        sex = input("Enter Sex: ")
        age = input("Age: ")
        user_info.append({"information{:d}".format(i): (name, sex, age)})

    print((user_info))
    sys.exit()
