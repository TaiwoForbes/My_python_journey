from dice import Dice

test = Dice(2,6)
for i in range(1,11):
        
    test.roll()
    print("Roll {}".format(i))
    print("RESULT :",test)
    print("TOTAL VALUE : ",test.getTotal())
    print("End of Roll {}\n".format(i))
        