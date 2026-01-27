from pytest import raises

import pytest


from app.application import *
from app.card_system import Card
from app.schemas.errors import Not_enough_fund


def test_gacha_process(memory_db_connection):
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
                        conn=memory_db_connection.conn)
    
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
                        conn=memory_db_connection.conn)
    
    result3 = repo.search_card(2, 'test')

    assert result3['o_band'] == 'ppp'
    

    # Multi
    cards = normal_gacha(user_id='test', 
                        fund_spent=0, times=2,
                        gacha_cls=Fake_gacha, 
                        conn=memory_db_connection.conn)
    
    result4 = repo.search_card(4, 'test')

    assert result4['character'] == 'ksm'
    


    
    # Fund issue
    with raises(Not_enough_fund) as error:

        card3 = normal_gacha(user_id='test', 
                        fund_spent=10, times=1, 
                        gacha_cls=Fake_gacha, 
                        conn=memory_db_connection.conn)




    # Test free gacha
    result5 = free_gacha(user_id='test', 
                        gacha_cls=Fake_gacha, 
                        conn=memory_db_connection.conn) 
    
    assert '今日首次打卡成功！+10资金' in result5

    result6 = repo.search_user('test')

    assert result6['fund'] == 10