import random
num = 20

num = random.randrange(num)
attempt = 10
guess = 0
while attempt != 0:
    try:
        attempt -= 1
        guess += 1
        guess = int(input("Guess a number from 1-20: "))
        if guess < num:
            print("Number is too low, choose a higher number,you have {} attempts left".format(attempt))
        elif guess > num:
            print("Number is too high,choose a lower number,you have {} attempts left".format(attempt))
        elif guess == num:
            print("You guessed right in {} attempt".format(attempt - (guess + 1)))
            break
        
        
    except ValueError:
        print("Number must be  an interger")
else:
            print("Sorry you have exausted your attempts")