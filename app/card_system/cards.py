from dataclasses import dataclass

@dataclass
class Card:
    card_id: int
    user_id: int
    character: str
    o_band: str
    pos: str
    rarity: str
    power: int
    speed: int
    resistance: int
    skill_1: str=None
    skill_2: str=None
    skill_3: str=None


