from app.gacha import Gacha, Character

def test_gacha():

    def fake_char():
        return Character('ksm', 'ppp', "singer", 100, 100, 100)
    
    def fake_rarity(bonus):
        return 6

    def fake_stats(char, rarity):
        char.power = 170
        char.resistance = 30

        return char
    
    result = Gacha(fake_char, fake_rarity, fake_stats).initial(user_id='test', card_id=1, bonus=0)

    assert result.character == 'ksm'
    assert result.rarity == 6
    assert result.power == 170
    
