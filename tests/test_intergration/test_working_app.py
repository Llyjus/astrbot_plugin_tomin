from pytest import raises

from app.application import start_working_app, user_working_status_app, stop_working_app, card_working_status_app, finish_working_app
from app.data_management import Repository
from app.schemas.errors import *

def test_working_app(memory_db_connection: Repository):
    repo = memory_db_connection

    # Add user and card
    user1 = 'test1'

    cards = [(1, user1, 'ksm', 'ppp', 'voice', 3, 100, 100, 20, None, None, None),
            (2, user1, 'ksm', 'ppp', 'voice', 3, 100, 100, 20, None, None, None),
            (3, user1, 'ksm', 'ppp', 'voice', 3, 100, 100, 20, None, None, None),
            (4, user1, 'ksm', 'ppp', 'voice', 3, 100, 100, 20, None, None, None)]

    repo.add_user(user1)
    repo.add_cards(cards)

    # Start working
    result1 = start_working_app(user_id=user1, 
                                card_id=1, 
                                place='SPACE', 
                                hours=1,
                                connect=memory_db_connection.conn,
                                time_now=0)
    assert "已经开始工作了！" in result1['txt']

    # Check working status
    result2 = user_working_status_app(user_id=user1, 
                                      connect=memory_db_connection.conn)
    assert "结算" in result2['txt']
    assert "ksm" in result2['txt']

    result3 = card_working_status_app(user_id=user1, 
                                        card_id=1, 
                                        connect=repo.conn)
    assert "结算" in result3['txt']
    assert "ksm" in result3['txt']

    with raises(Card_not_found, match='ksm 已经停止工作了！目前没有卡牌在工作和休息了哦！') as error1:
        result4 = stop_working_app(user_id=user1, 
                                    card_id=1, 
                                    time_now=0, 
                                    connect=repo.conn)
        



    start_working_app(user_id=user1,
                      card_id=1,
                      place='SPACE',
                      hours=1,
                      connect=memory_db_connection.conn,
                      time_now=0)
    
    result = finish_working_app(user_id=user1, 
                      time_now=3600, 
                      connect=memory_db_connection.conn)
    assert "结束" in result['txt']



    with raises(Card_not_found, match='卡牌没工作过呢！猪...') as error1:
        card_working_status_app(user_id=user1, 
                                    card_id=2, 
                                    connect=repo.conn)

    with raises(Card_not_found, match='没有找到该卡牌！猪...') as error2:
        stop_working_app(user_id=user1, 
                            card_id=999, 
                            connect=repo.conn)
        
    start_working_app(user_id=user1,
                      card_id=1,
                      place='SPACE',
                      hours=1,
                      connect=memory_db_connection.conn,
                      time_now=20000)
        
    start_working_app(user_id=user1, 
                      card_id=2, 
                      place='SPACE', 
                      hours=1,
                      connect=memory_db_connection.conn,
                      time_now=20000)
    
    start_working_app(user_id=user1,
                      card_id=3, 
                      place='SPACE', 
                      hours=1,
                      connect=memory_db_connection.conn,
                      time_now=20000)
    
    with raises(Working_card_limit, match='您已经有3张卡牌在工作中了哦，不能再多啦！') as error3:

        start_working_app(user_id=user1, 
                      card_id=4, 
                      place='SPACE', 
                      hours=1,
                      connect=memory_db_connection.conn,
                      time_now=20000)