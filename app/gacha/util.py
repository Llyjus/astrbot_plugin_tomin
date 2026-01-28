
from math import floor, sqrt, log, cos, pi
from random import randint, random


from app.gacha.characters import Character



def rarity_roll(bonus:int):
    roll = randint(1, 100)
    if roll >= 100 - bonus * 0.1:
        return 6
    elif roll >= 94 - bonus * 0.3:
        return 5
    elif roll >= 84 - bonus * 0.5:
        return 4
    elif roll >= 65 - bonus * 0.7:
        return 3
    elif roll >= 30 - bonus * 1.0:
        return 2
    else:
        return 1




def stats_roll(base:Character, rarity):

    char = Character(
        base.character,
        base.o_band,
        base.pos,
        floor(random_value(base.power) * (1 + (rarity - 1) * 0.1)),
        base.speed,
        floor(random_value(base.resistance) * (1 + max(rarity - 2, 0) * 0.1))



    )
    return char







def random_value(value):

    # normal distribution
    def norm_random(mean=0.0, std=1.0):

        u1 = random.random()
        u2 = random.random()
        z = sqrt(-2.0 * log(u1)) * cos(2.0 * pi * u2)
        return mean + z * std


    result_li = norm_random(value, 0.05*value)
    result = float(result_li[0])

    return result
        
    



    
    
