""" The game() function in a program let a user play a game and returns the score as an integer. 
    You need to read a file  "Hiscore.txt" whcih is either blank or contain the previous hi-score.
    You need to write a program to update the hi_score whenever game() break the hi-score.
"""

import random
# A function that generate a random number
def game():
    score = random.randrange(1,1000)
    print("The score is {}".format(score))
    return score
# setting the number generated in a variable
score = game()

# opening the file which contains the previous score
with open("hi-score.txt", 'r') as f:
    #converting the number to an integer
    hi_score = int(f.read())

# Giving the condition where the hi-score will be updated/changed
if score > hi_score:
    with open("hi-score.txt", 'w') as f:
        f.write(str(score))

