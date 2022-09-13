import random
def playgame():
    num = 20

    num = random.randrange(num)
    attempt = 10
    amountOFguesses = 0
    while attempt != 0:
        try:
            attempt -= 1
            amountOFguesses += 1
            guess = int(input("Guess a number from 1-20: "))
            if guess < num:
                print("Number is too low, choose a higher number,you have {} attempts left".format(attempt))
            elif guess > num:
                print("Number is too high,choose a lower number,you have {} attempts left".format(attempt))
            elif guess == num:
                print("You guessed right in {} attempt".format(amountOFguesses))
                break
            
            
        except ValueError:
            print("Number must be  an interger")
    else:
                print("Sorry you have exausted your attempts")



    playagin = input("Would you like to play again. [y/n]").lower()
    while playagin != "y" and playagin != "n":
        input("Would you like to play again. [y/n]").lower()
    if playagin == "y":

        return True
    else:
        return False

if "__main__" == __name__:
    while playgame():
        pass

    