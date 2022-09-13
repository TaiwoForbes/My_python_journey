import random

def snake_water_gun(comp,mine):
    if comp == "s" and mine == "g":
        return True
    elif comp == mine:
        return None
    elif comp == "w" and mine == "s":
        return True
    elif comp == "g" and mine == "w":
        return True
    else:
        return False


choice = ("s", "w", "g")
comp = random.randint(0,2)
comp = choice[comp]
mine = input("Enter s for snake, w for water , g for gun")

win = snake_water_gun(comp,mine)
if win == True:
    print("You Win\nYou choose {} and the computer {}".format(mine,comp))
elif win == None:
    print("Draw\nYou choose {} and the computer choose {}".format(mine,comp))
else:
    print("You Lose\nYou choose {} and the computer choose {}".format(mine,comp))
    