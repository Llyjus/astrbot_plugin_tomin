from random import choice















class Character:
    def __init__(self, character, o_band, pos, power, speed, resistance):
        self.character = character
        self.o_band = o_band
        self.pos = pos
        self.power = power
        self.speed = speed
        self.resistance = resistance






from random import choice

CHARACTERS = {
    "ksm": {
        "o_band": "ppp",
        "pos": "singer, guitar",
        "power": 100,
        "speed": 107,
        "resistance": 15,
    },
    "ars": {
        "o_band": "ppp", 
        "pos": "keyboard",
        "power": 100,
        "speed": 93, 
        "resistance": 25,
    },
    "rimi": {
        "o_band": "ppp",
        "pos": "bass",
        "power": 100,
        "speed": 96, 
        "resistance": 19,
    },
    "saaya": {
        "o_band": "ppp",
        "pos": "drummer",
        "power": 100,
        "speed": 99, 
        "resistance": 18,
    },
    "tae": {
        "o_band": "ppp",
        "pos": "guitar",
        "power": 100,
        "speed": 105,
        "resistance": 23,
    },
    "nina": {
        "o_band": "toge",
        "pos": "singer",
        "power": 100,
        "speed": 110,
        "resistance": 27,
    },
    "mmk": {
        "o_band": "toge",
        "pos": "guitar",
        "power": 100,
        "speed": 102,
        "resistance": 21,
    },
    "sbr": {
        "o_band": "toge",
        "pos": "drummer",
        "power": 100,
        "speed": 105,
        "resistance": 13,
    },
    "tomo": {
        "o_band": "toge",
        "pos": "keyboard",
        "power": 100,
        "speed": 90,
        "resistance": 24,
    },
    "nina": {
        "o_band": "toge",
        "pos": "singer",
        "power": 100,
        "speed": 93,
        "resistance": 15,
    },
}



def random_character():
    character = choice(list(CHARACTERS.keys()))
    config = CHARACTERS[character]
    return Character(character, **config)

