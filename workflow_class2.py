import random
import math
"""GAME OF FIGHT"""
'''????????????????????????????????????????????????????????????'''
'''Real World Objects : Attributes & Capabilities
(Fields are basically variables)
(Attributes are called Fields)
Dag Attributes (Fields / Variables) : Height, Weight, Favorite Food
(Methods are basically Functions)
(Capabilities are called Methods)
Dog Capabilities (Methods / Function) : Run, walk, Eat '''

'''
Sam Attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks sam and dels 7 damage
Sam attacks Paul and deas 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
'''

#Warrior & Battle Class

class Warrior:
#Warriors will have names, health, and attack and block maximus
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

#They will have the capabilities to attack and block random amounts

#Attack random() 0.0 to 1.0 * maxAttack + .5

#Block will use random()
    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

class Battle:
    
#Battle Class capability of looping until 1 warrior dies 
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
#'''staticmethod is a method or capability of a class''' 
    @staticmethod
#Warriors will each get a turn to attack each other 
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        
        else:
            return "Fight Again"


def main():
    maximus = Warrior("Maximus", 50,20,10)

    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)

main()
#Function gets 2 warriors
#1 warrior attacks the other
#Attacks and Blocks be integers