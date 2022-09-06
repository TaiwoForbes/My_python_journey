import sys
services = input("Are you traveling: [y/n]")
user_info = []
while services == "y":
    num = int(input("Enter the number of people traveling: \n"))
    for i in range(1,num+1):
        name = input("Enter name: ")
        sex = input("Enter Sex: ")
        age = input("Age: ")
        user_info.append(name)
        user_info.append(sex)
        user_info.append(age)
    print(user_info)
    sys.exit()