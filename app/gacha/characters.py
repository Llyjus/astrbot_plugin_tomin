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

    "ran": {
        "o_band": "afterglow",
        "pos": "singer, guitar",
        "power": 100,
        "speed": 110,
        "resistance": 27,
    },
    "moka": {
        "o_band": "afterglow", 
        "pos": "guitar",
        "power": 100,
        "speed": 92, 
        "resistance": 18,
    },
    "himari": {
        "o_band": "afterglow", 
        "pos": "bass",
        "power": 100,
        "speed": 97, 
        "resistance": 17,
    },
    "tomoe": {
        "o_band": "afterglow",
        "pos": "drummer",
        "power": 100,
        "speed": 107, 
        "resistance": 23,
    },
    "tsugu": {
        "o_band": "afterglow",
        "pos": "keyboard",
        "power": 100,
        "speed": 94,
        "resistance": 15,
    },

        "aya": {
        "o_band": "pastel palettes",
        "pos": "singer",
        "power": 98,
        "speed": 100,
        "resistance": 22,
    },
    "hina": {
        "o_band": "pastel palettes", 
        "pos": "guitar",
        "power": 100,
        "speed": 110, 
        "resistance": 17,
    },
    "chisato": {
        "o_band": "pastel palettes", 
        "pos": "bass",
        "power": 100,
        "speed": 102, 
        "resistance": 21,
    },
    "maya": {
        "o_band": "pastel palettes",
        "pos": "drummer",
        "power": 100,
        "speed": 93, 
        "resistance": 23,
    },
    "eve": {
        "o_band": "pastel alettes",
        "pos": "keyboard",
        "power": 100,
        "speed": 95,
        "resistance": 17,
    },

    "yukina": {
        "o_band": "roselia",
        "pos": "singer",
        "power": 100,
        "speed": 115,
        "resistance": 28,
    },
    "sayo": {
        "o_band": "roselia", 
        "pos": "guitar",
        "power": 100,
        "speed": 97, 
        "resistance": 16,
    },
    "lisa": {
        "o_band": "roselia", 
        "pos": "bass",
        "power": 100,
        "speed": 97, 
        "resistance": 17,
    },
    "ako": {
        "o_band": "roselia",
        "pos": "drummer",
        "power": 100,
        "speed": 103, 
        "resistance": 23,
    },
    "rinko": {
        "o_band": "roselia",
        "pos": "keyboard",
        "power": 100,
        "speed": 88,
        "resistance": 16,
    },

    "kokoro": {
        "o_band": "hello happy world",
        "pos": "singer",
        "power": 100,
        "speed": 107,
        "resistance": 25,
    },
    "kaoru": {
        "o_band": "hello happy world", 
        "pos": "guitar",
        "power": 100,
        "speed": 93, 
        "resistance": 19,
    },
    "hagumi": {
        "o_band": "hello happy world", 
        "pos": "bass",
        "power": 100,
        "speed": 104, 
        "resistance": 21,
    },
    "kanon": {
        "o_band": "hello happy world",
        "pos": "drummer",
        "power": 100,
        "speed": 94, 
        "resistance": 13,
    },
    "misaki": {
        "o_band": "hello happy world",
        "pos": "dj",
        "power": 100,
        "speed": 102,
        "resistance": 22,
    },

    "mashiro": {
        "o_band": "morfonica",
        "pos": "singer",
        "power": 100,
        "speed": 101,
        "resistance": 16,
    },
    "tsukushi": {
        "o_band": "morfonica", 
        "pos": "guitar",
        "power": 100,
        "speed": 97, 
        "resistance": 16,
    },
    "nanami": {
        "o_band": "morfonica", 
        "pos": "bass",
        "power": 100,
        "speed": 100, 
        "resistance": 22,
    },
    "touko": {
        "o_band": "morfonica",
        "pos": "drummer",
        "power": 100,
        "speed": 107, 
        "resistance": 18,
    },
    "rui": {
        "o_band": "morfonica",
        "pos": "violin",
        "power": 100,
        "speed": 95,
        "resistance": 28,
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
    "masking": {
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
    "taki": {
        "o_band": "mygo",
        "pos": "drummer",
        "power": 100,
        "speed": 97, 
        "resistance": 16,
    },
    "raana": {
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
    "hatsune": {
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

    "hitori": {
        "o_band": "kessoku band",
        "pos": "guitar",
        "power": 100,
        "speed": 101,
        "resistance": 12,
    },
    "nijika": {
        "o_band": "kessoku band", 
        "pos": "drummer",
        "power": 100,
        "speed": 102, 
        "resistance": 18,
    },
    "ryo": {
        "o_band": "kessoku band", 
        "pos": "bass",
        "power": 90,
        "speed": 90, 
        "resistance": 30,
    },
    "kita": {
        "o_band": "kessoku band",
        "pos": "singer, guitar",
        "power": 93,
        "speed": 107, 
        "resistance": 20,
    },

}



def random_character():
    character = choice(list(CHARACTERS.keys()))
    config = CHARACTERS[character]
    return Character(character, **config)

