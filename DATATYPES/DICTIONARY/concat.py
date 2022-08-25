dick1 = {"color": 22, "age": 21, "amount":24}
dick2= {"color": 22, "age": 21, "amount":24}
dick3 = {"color": 22, "age": 21, "amount":24}

concat = {}

for i in (dick1,dick2,dick3):
    concat.update(i)
    print(concat)
