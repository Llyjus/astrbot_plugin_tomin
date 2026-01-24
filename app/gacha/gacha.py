from app.card_system.cards import Card
from app.gacha.util import *
from app.gacha.characters import random_character

class Gacha():
    def __init__(self, char_func=random_character, rarity_func=rarity_roll, stats_func=stats_roll):
        self.char_func = char_func
        self.rarity_func = rarity_func
        self.stats_func = stats_func


    def initial(self, user_id, card_id, bonus):

        char = self.char_func()
        rarity = self.rarity_func(bonus)

        #skill set part: not complete

        stats = self.stats_func(char, rarity)



        card = Card(card_id=card_id, 
                        user_id=user_id,
                        character=stats.character,
                        o_band=stats.o_band,
                        pos=stats.pos,
                        rarity=rarity,
                        power=stats.power,
                        speed=stats.speed,
                        resistance=stats.resistance,
                        skill_1=None,
                        skill_2=None,
                        skill_3=None   )
        return card
        
        



