import random
import math
"""
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health 
Sam attacks Paul and deas 19 damage
Paul is down to -9 health 
Paul has died and Sam is victorious 
Game Over
"""

# Create a Warrior and a Battle class


class Warrior:
    # Warrior will have name, health and attack and block maximums

    def __init__(self, name="warrior", health=0, AttMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.AttMax = AttMax
        self.blockMax = blockMax

    # They will have the capabilities to attack and block random

    # Attack random() 0.0 1.0 * maxAttack + .5
    # Block random()
    def attack(self):
        attAmt = self.AttMax * (random.random() + .5)
        return attAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt


# Battle class will have the capabilities of looping until one warrior dies
# Warrior will each get a turn to attack each other

class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "GAME OVER" or self.getAttackResult(warrior2, warrior1) == "GAME OVER":
                print("GAME OVER")
                break
            '''if self.getAttackResult(warrior2, warrior1) == "GAME OVER":
                print("GAME OVER")
                break'''


    # Function gets 2 warriors
    # 1 warrior attacks the other
    # Attacks and Blocks should  be integers
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        
        warriorA_attackAmount = warriorA.attack() # Getting the attack amount of warriorA
        warriorB_blockAmount = warriorB.block()  # Getting the block amount of warriorB
        damage2warriorB = math.ceil(warriorA_attackAmount - warriorB_blockAmount)
        warriorB.health = warriorB.health - damage2warriorB
        
          
        print("{} attacks {} and deal {} damage".format(warriorA.name, warriorB.name, damage2warriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} victorious".format(
                warriorB.name, warriorA.name))
            return "GAME OVER"
        else:
            print("FIGHT AGAIN")


if __name__ == "__main__":
    scorpion = Warrior("scorpion", 50,20,10)
    raiden = Warrior("raiden", 50,20,10)
   
    
    

    battle = Battle()
    battle.start_fight(scorpion,raiden)