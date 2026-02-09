
from math import floor, sqrt, log, cos, pi
import random as ran


from app.gacha.characters import Character



def rarity_roll(bonus:int):
    roll = ran.randint(1, 100)
<<<<<<< HEAD
    if roll >= 130 - bonus * 1:
        return 6
    elif roll >= 115 - bonus * 1:
        return 5
    elif roll >= 95 - bonus * 1.5:
        return 4
    elif roll >= 70 - bonus * 2:
        return 3
    elif roll >= 40 - bonus * 2.5:
=======
    if roll >= 100 - bonus * 0.2:
        return 6
    elif roll >= 94 - bonus * 0.6:
        return 5
    elif roll >= 84 - bonus * 1:
        return 4
    elif roll >= 65 - bonus * 1.4:
        return 3
    elif roll >= 30 - bonus * 2:
>>>>>>> origin/develop
        return 2
    else:
        return 1




def stats_roll(base:Character, rarity):

    char = Character(
        base.character,
        base.o_band,
        base.pos,
        floor(random_value(base.power) * (1 + (rarity - 1) * 0.1)),
<<<<<<< HEAD
        floor(random_value(base.speed) * (1 + (rarity - 1) * 0.1)),
=======
        base.speed,
>>>>>>> origin/develop
        floor(random_value(base.resistance) * (1 + max(rarity - 2, 0) * 0.1))



    )
    return char


    # normal distribution
def random_value(value):
    return ran.gauss(value, 0.05 * value)


        
    



    
    
