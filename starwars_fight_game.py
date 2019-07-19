"""
This is a fighting game I made to try and understand a few of the concepts I've learnt so far and especially to try and understand Classes and OOP in Python. 
It has ended up being Star Wars themed because it is fun and that was just because that was what entered my head when I thought up the idea. 
"""

# Import libraries
import time
from random import randint

# Define classes

class Melee():
    def __init__(self, name):
        self.name = name
        self.base_atk = 10

    def normal_atk(self):
        atk_dmg = self.base_atk + self.atk + (randint(1,10))
        print(f"{self.name} performs a slashing attack on his opponent for {atk_dmg} damage")
        return atk_dmg

    def heavy_atk(self):
        atk_dmg = (self.base_atk - 2) + self.atk + (randint(1,15))
        print(f"{self.name} stabs his weapon hard at his opponent and deals {atk_dmg} damage")
        return atk_dmg


class Ranged():
    def __init__(self, name):
        self.name = name
        self.base_atk = 10

    def normal_atk(self):
        atk_dmg = self.base_atk + self.atk + (randint(1,10))
        print(f"{self.name} fires his blaster at his opponent and deals {atk_dmg} damage")
        return atk_dmg

    def heavy_atk(self):
        atk_dmg = (self.base_atk - 2) + self.atk + (randint(1,15))
        print(f"{self.name} charges his blaster before firing and deals {atk_dmg} damage to his opponent")
        return atk_dmg


class Jedi(Melee):
    def __init__(self, name):
        self.atk = 2
        self.health = 110
        super().__init__(name)

    def special_atk(self):
        atk_dmg = (self.base_atk - 4) + self.atk + (randint(1,20))
        print(f"{self.name} uses the force to push away his oppenent and deals {atk_dmg} damage")
        return atk_dmg

class Sith(Melee):
    def __init__(self, name):
        self.atk = 4
        self.health = 100
        super().__init__(name)

    def special_atk(self):
        atk_dmg = (self.base_atk - 4) + self.atk + (randint(1,20))
        print(f"{self.name} starts force choking the life out of his opponent and deals {atk_dmg} damage")
        return atk_dmg

class Soldier(Ranged):
    def __init__(self, name):
        self.atk = 1
        self.health = 120
        super().__init__(name)

    def special_atk(self):
        atk_dmg = (self.base_atk - 4) + self.atk + (randint(1,20))
        print(f"{self.name} throws a grenade at his oppenent and deals {atk_dmg} damage")
        return atk_dmg

class Bounty_Hunter(Ranged):
    def __init__(self, name):
        self.atk = 3
        self.health = 105
        super().__init__(name)

    def special_atk(self):
        atk_dmg = (self.base_atk - 4) + self.atk + (randint(1,20))
        print(f"{self.name} fires a rocket from his wrist at his oppenent and deals {atk_dmg} damage")
        return atk_dmg

# Create chars
Yoda = Jedi("Yoda")
Vader = Sith("Darth Vader")
Appo = Soldier("Commander Appo")
Fett = Bounty_Hunter("Boba Fett")

# Input select char

# Player's character
print("""\nChoose you character!
Press 1 for Yoda
Press 2 for Darth Vader
Press 3 for Commander Appo
Press 4 for Boba Fett
""")

while True:
    Human = int(input())
    if Human == 1:
        Human = Yoda
        print(f"You chose {Human.name}\n")
        break

    elif Human == 2:
        Human = Vader
        print(f"You chose {Human.name}\n")
        break

    elif Human == 3:
        Human = Appo
        print(f"You chose {Human.name}\n")
        break

    elif Human == 4:
        Human = Fett
        print(f"You chose {Human.name}\n")
        break

    else:
        print("That was not a valid input")

# Computer's character
print("""Choose which character you will face!
Press 1 for Yoda
Press 2 for Darth Vader
Press 3 for Commander Appo
Press 4 for Boba Fett
""")

while True:
    Computer = int(input())
    if Computer == 1:
        Computer = Yoda
        print(f"You chose to face {Computer.name}\n")
        break

    elif Computer == 2:
        Computer = Vader
        print(f"You chose to face {Computer.name}\n")
        break

    elif Computer == 3:
        Computer = Appo
        print(f"You chose to face {Computer.name}\n")
        break

    elif Computer == 4:
        Computer = Fett
        print(f"You chose to face {Computer.name}\n")
        break

    else:
        print("That was not a valid input")


# Decide who goes first

print("Roll to see who goes first!\n")

while True:
    input("Press any button\n")
    human_roll = randint(1,6)
    comp_roll = randint(1,6)

    print(f"You rolled a {human_roll}\n")
    print(f"You opponent rolled a {comp_roll}\n")

    if human_roll > comp_roll:
        print("You get to go first!\n")
        Player1 = Human
        Player2 = Computer
        break

    elif comp_roll > human_roll:
        print("Your opponent gets to go first!\n")
        Player1 = Computer
        Player2 = Human
        break

    else:
        print("You both got the same number. Reroll!")


# Choose attacks until someone wins

Health1 = Player1.health
Health2 = Player2.health

print("Get ready to fight!\n")
time.sleep(2)

while Health1 > 0 and Health2 > 0:
    while Player1 == Human and Health1 > 0 and Health2 > 0:

        # Human turn
        print("""\tChoose you action!
        Press 1 for normal attack
        Press 2 for heavy attack
        Press 3 for special attack
        """)

        action = int(input("Which attack will you perform? \n"))

        if action == 1:
            Health2 = Health2 - Player1.normal_atk()
            time.sleep(1)
            print(f"{Player2.name} is down to {Health2} health\n")
            time.sleep(2)
            break

        elif action == 2:
            Health2 = Health2 - Player1.heavy_atk()
            time.sleep(1)
            print(f"{Player2.name} is down to {Health2} health\n")
            time.sleep(2)
            break

        elif action == 3:
            Health2 = Health2 - Player1.special_atk()
            time.sleep(1)
            print(f"{Player2.name} is down to {Health2} health\n")
            time.sleep(2)
            break

        else:
            print("That was not a valid input!")
            continue


    while Player2 == Computer and Health1 > 0 and Health2 > 0:

        # Computer turn
        comp_action = randint(1,3)

        if comp_action == 1:
            Health1 = Health1 - Player2.normal_atk()
            time.sleep(1)
            print(f"{Player1.name} is down to {Health1} health\n")
            time.sleep(2)
            break

        elif comp_action == 2:
            Health1 = Health1 - Player2.heavy_atk()
            time.sleep(1)
            print(f"{Player1.name} is down to {Health1} health\n")
            time.sleep(2)
            break

        elif comp_action == 3:
            Health1 = Health1 - Player2.special_atk()
            time.sleep(1)
            print(f"{Player1.name} is down to {Health1} health\n")
            time.sleep(2)
            break

    while Player1 == Computer and Health1 > 0 and Health2 > 0:

        # Computer turn
        comp_action = randint(1,3)

        if comp_action == 1:
            Health2 = Health2 - Player1.normal_atk()
            time.sleep(1)
            print(f"{Player2.name} is down to {Health2} health\n")
            time.sleep(2)
            break

        elif comp_action == 2:
            Health2 = Health2 - Player1.heavy_atk()
            time.sleep(1)
            print(f"{Player2.name} is down to {Health2} health\n")
            time.sleep(2)
            break

        elif comp_action == 3:
            Health2 = Health2 - Player1.special_atk()
            time.sleep(1)
            print(f"{Player2.name} is down to {Health2} health\n")
            time.sleep(2)
            break

    while Player2 == Human and Health1 > 0 and Health2 > 0:

            # Human turn
            print("""\tChoose you action!
            Press 1 for normal attack
            Press 2 for heavy attack
            Press 3 for special attack
            """)

            action = int(input("Which attack will you perform? \n"))

            if action == 1:
                Health1 = Health1 - Player2.normal_atk()
                time.sleep(1)
                print(f"{Player1.name} is down to {Health1} health\n")
                time.sleep(2)
                break

            elif action == 2:
                Health1 = Health1 - Player2.heavy_atk()
                time.sleep(1)
                print(f"{Player1.name} is down to {Health1} health\n")
                time.sleep(2)
                break

            elif action == 3:
                Health1 = Health1 - Player2.special_atk()
                time.sleep(1)
                print(f"{Player1.name} is down to {Health1} health\n")
                time.sleep(2)
                break

            else:
                print("That was not a valid input")
                continue


if Health1 <=0 and Health2 <= 0:
    print("It's a draw")

elif Player1 == Human and Health1 <= 0:
    print("You lose!")

elif Player2 == Human and Health2 <= 0:
    print("You lose!")

elif Player1 == Human and Health2 <= 0:
    print("You win!")

elif Player2 == Human and Health1 <= 0:
    print("You win!")
