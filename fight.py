"""
Very basic fighting game which will be a base for a more complex game I plan on making

"""

import time
from random import randint

Health1 = 100
Health2 = 100
Attack1 = 10
Attack2 = 10

while Health1 > 0 and Health2 > 0:
    
    input("Press to attack!")
    Action_p1 = Attack1 + (randint(1,6))
    Health2 = Health2 - Action_p1
    print(f"You did {Action_p1} damage and your opponent is down to {Health2} health")
    time.sleep(1)
    Action_p2 = Attack2 + (randint(1,6))
    Health1 = Health1 - Action_p2
    print(f"Your opponent did {Action_p2} damage and you are down to {Health1} health")
    time.sleep(1)

if Health1 <=0 and Health2 <= 0:
    print("It's a draw")

elif Health1 <= 0:
    print("You lose!")

elif Health2 <= 0:
    print("You win!")
