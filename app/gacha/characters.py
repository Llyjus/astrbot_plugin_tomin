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
    "kasumi": {
        "o_band": "popipa",
        "pos": "singer, guitar",
        "power": 100,
        "speed": 107,
        "resistance": 15,
    },
    "arisa": {
        "o_band": "popipa", 
        "pos": "keyboard",
        "power": 100,
        "speed": 93, 
        "resistance": 25,
    },
    "rimi": {
        "o_band": "popipa",
        "pos": "bass",
        "power": 100,
        "speed": 96, 
        "resistance": 19,
    },
    "saaya": {
        "o_band": "popipa",
        "pos": "drummer",
        "power": 100,
        "speed": 99, 
        "resistance": 18,
    },
    "tae": {
        "o_band": "popipa",
        "pos": "guitar",
        "power": 100,
        "speed": 105,
        "resistance": 23,
    },

    "layer": {
        "o_band": "RAS",
        "pos": "singer, bass",
        "power": 100,
        "speed": 103,
        "resistance": 25,
    },
    "lock": {
        "o_band": "RAS", 
        "pos": "guitar",
        "power": 100,
        "speed": 93, 
        "resistance": 15,
    },
    "chuchu": {
        "o_band": "RAS",
        "pos": "DJ",
        "power": 100,
        "speed": 103, 
        "resistance": 23,
    },
    "mask": {
        "o_band": "RAS",
        "pos": "drummer",
        "power": 100,
        "speed": 98, 
        "resistance": 22,
    },
    "pareo": {
        "o_band": "RAS",
        "pos": "keyboard",
        "power": 100,
        "speed": 103,
        "resistance": 15,
    },

    "tomori": {
        "o_band": "mygo",
        "pos": "singer",
        "power": 100,
        "speed": 92,
        "resistance": 15,
    },
    "anon": {
        "o_band": "mygo", 
        "pos": "guitar",
        "power": 100,
        "speed": 103, 
        "resistance": 20,
    },
    "soyo": {
        "o_band": "mygo",
        "pos": "bass",
        "power": 100,
        "speed": 93, 
        "resistance": 19,
    },
    "riki": {
        "o_band": "mygo",
        "pos": "drummer",
        "power": 100,
        "speed": 97, 
        "resistance": 16,
    },
    "laana": {
        "o_band": "mygo",
        "pos": "guitar",
        "power": 100,
        "speed": 110,
        "resistance": 30,
    },

    "sakiko": {
        "o_band": "ave mujica",
        "pos": "keyboard",
        "power": 100,
        "speed": 103,
        "resistance": 23,
    },
    "umirin": {
        "o_band": "ave mujica", 
        "pos": "keyboard",
        "power": 100,
        "speed": 98, 
        "resistance": 15,
    },
    "otsune": {
        "o_band": "ave mujica",
        "pos": "bass",
        "power": 100,
        "speed": 105, 
        "resistance": 30,
    },
    "muzumi": {
        "o_band": "ave mujica",
        "pos": "guitar",
        "power": 100,
        "speed": 94, 
        "resistance": 15,
    },
    "nyamu": {
        "o_band": "ave mujica",
        "pos": "drummer",
        "power": 100,
        "speed": 100,
        "resistance": 17,
    },
    "nina": {
        "o_band": "toge",
        "pos": "singer",
        "power": 100,
        "speed": 110,
        "resistance": 27,
    },
    "momoka": {
        "o_band": "toge",
        "pos": "guitar",
        "power": 100,
        "speed": 102,
        "resistance": 21,
    },
    "subaru": {
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
    "rupa": {
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

