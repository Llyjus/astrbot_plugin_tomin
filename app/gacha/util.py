
from math import floor
from app.gacha.characters import Character
from random import randint





def rarity_roll(bonus:int):
    roll = randint(1, 100)
    if roll >= 100 - bonus * 0.1:
        return 6
    elif roll >= 94 - bonus * 0.15:
        return 5
    elif roll >= 84 - bonus * 0.2:
        return 4
    elif roll >= 65 - bonus * 0.25:
        return 3
    elif roll >= 30 - bonus * 0.3:
        return 2
    else:
        return 1




def stats_roll(base:Character, rarity):

    base.power = floor(random_value(base.power) * (1 + (rarity - 1) * 0.1))
    base.resistance = floor(random_value(base.resistance) * (1 + max(rarity - 2, 0) * 0.1))

    return base







def random_value(value):
    import numpy

    result_li = numpy.random.normal(value, 0.05*value, 1)
    result = float(result_li[0])

    return result
        
    



    
    
