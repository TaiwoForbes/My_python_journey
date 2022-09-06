dick1 = {"color": 22, "age": 21, "amount":24}
dick2= {"male": 24, "children": 18, "adults":90}
dick3 = {"books": 55, "cities": 60, "school":68}

concat = {}

for i in (dick1,dick2,dick3):
    concat.update(i)
print(concat)
# OR
con = {**dick1, **dick1, **dick3}
print(con)
