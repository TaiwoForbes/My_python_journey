import random
head_or_Tail = []

for i in  range(1,101):
    choice = random.choice(["H","T"])
    head_or_Tail.append(choice)

    
print(head_or_Tail.count("H"))
print(head_or_Tail.count("T"))

