from pytest import raises

import pytest


from app.application import *
from app.card_system import Card
from app.schemas.errors import Not_enough_fund


def test_card_in_out(memory_db_connection):
    class Fake_gacha():
        def __init__(self):
            pass

        def initial(self, user_id, card_id, fund_spent):
            return Card(card_id, user_id, 'ksm', 'ppp',
                        'singer', 3, 100, 100, 20)
        
        
    repo = memory_db_connection

    # Mock user processes gacha
    repo.add_user('test')

    r = repo.search_user('test')


    # Test normal gacha
    card1 = normal_gacha(user_id='test', 
                        fund_spent=10, times=1,
                        gacha_cls=Fake_gacha, 
                        connect=memory_db_connection.conn)
    
    # Check the user's fund
    result1 = repo.search_user('test')

    assert result1['fund'] == 0


    # Check if card in the table 
    result2 = repo.search_card(1, 'test')

    assert result2['character'] == 'ksm'

    # Check auto increasement
    repo.add_fund('test', 10)

    card2 = normal_gacha(user_id='test', 
                        fund_spent=10, times=1,
                        gacha_cls=Fake_gacha, 
                        connect=memory_db_connection.conn)
    
    result3 = repo.search_card(2, 'test')

    assert result3['o_band'] == 'ppp'
    

    # Multi
    cards = normal_gacha(user_id='test', 
                        fund_spent=0, times=2,
                        gacha_cls=Fake_gacha, 
                        connect=memory_db_connection.conn)
    
    result4 = repo.search_card(4, 'test')

    assert result4['character'] == 'ksm'
    


    
    # Fund issue
    with raises(Not_enough_fund) as error:

        card3 = normal_gacha(user_id='test', 
                        fund_spent=10, times=1, 
                        gacha_cls=Fake_gacha, 
                        connect=memory_db_connection.conn)




    # Test free gacha
    result5 = free_gacha(user_id='test', 
                        gacha_cls=Fake_gacha, 
                        connect=memory_db_connection.conn) 
    
    assert '今日首次打卡成功！+10资金' in result5['txt']

    result6 = repo.search_user('test')

    assert result6['fund'] == 10

    #sell card and record slot
    result7 = sell_card_app('test', 1, connect=memory_db_connection.conn)
 
    assert '出售成功！获得3资金。' in result7['content']['intro']

    result8 = repo.search_slots('test')

    for r in result8:
        assert r['slot'] == 1

    repo.add_user('t')

    give_away_cards_app('test', 2, 't', connect=memory_db_connection.conn)

    result9 = repo.search_slots('test')

    for r in result9:
        assert r['slot'] == 1 or r['slot'] == 2

    