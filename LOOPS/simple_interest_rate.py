investment = int(input("Enter your investment: "))
rate = int(input("Enter your rate: "))
rate = rate / 100
print(rate)


for i in range(10):
    investment = investment + investment * rate
    earnings = investment
print("Earnings after 10 years period is {:.2f}".format(earnings))