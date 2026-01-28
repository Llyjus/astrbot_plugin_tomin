import sys
import os
from pytest import raises
from time import sleep

from app.services import *
from app.schemas import *
from app.maintenance import Cleaner


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# from app.data_management.services.repository import Repository



def test_users_table(memory_db_connection):
    
    repo = memory_db_connection


    # Add and search user
    repo.add_user('test')
    result = repo.search_user('test')

    assert result['user_id'] == 'test' and result['fund'] == 10



    # Add Fund
    repo.add_fund('test', 20)

    repo.conn.commit()
    result = repo.search_user('test')

    assert result['fund'] == 30



    # Same user
    with raises(User_already_exists, match='用户已经存在') as error1:
        repo.add_user('test')



    # Illegal value
    with raises(Not_enough_fund, match='余额不足') as error2:
        repo.add_fund('test', -100)




def test_cards_table(memory_db_connection):
    repo = memory_db_connection
    uid1 = 'test'
    uid2 = 't'
    cid = 1

    repo.add_user(uid1)
    repo.add_user(uid2)

    cards = [(cid, uid1, 'ksm',
                  'ppp', 'voice',
                  3, 100,
                  100, 20, None, None, None),
            (cid, uid2, 'ksm',
                  'ppp', 'voice',
                  3, 100,
                  100, 20, None, None, None)]


    # Test adding&searching card
    repo.add_cards(cards)


    result1 = repo.search_card(cid, uid1)

    assert result1['card_id'] == cid
    assert result1['user_id'] == uid1


    cards = [(cid+1, uid1, 'ksm',
                  'ppp', 'voice',
                  3, 100,
                  100, 20, None, None, None)]

    repo.add_cards(cards)

    # uid1: card 1, 2
    # uid2: card 1

    result2 = repo.search_card_last('test')

    assert result2['card_id'] == 2


    result3 = repo.search_cards(uid1)

    for r in result3:
        assert r['card_id'] == 1 or r['card_id'] == 2




    #set_card_user

    #Should check the available card id in real circumstance 
    # but now may not

    repo.set_card_user(cid+1, uid2, cid, uid1)
    # uid1: 2
    # uid2: 1, 2


    repo.add_slots([(uid1, 1)])

    #Check slot
    result4 = repo.search_slots(uid1)
    # slot: 1

    for r in result4:
        assert r['slot'] == 1 and r['user_id'] == uid1


    # Delete slot
    repo.delete_slots([(uid1, 1)])


    # slot: []

    result5 = repo.search_slots(uid1)

    assert result5 == []

    repo.add_slots([(uid1, 1)])


    

    result6 = repo.search_card(cid+1, uid2)

    assert result6['user_id'] == 't' and result6['card_id'] == 2


    # Test methods of events table

    repo.add_event('test', 1)

    result7 = repo.search_event('test')

    assert result7['event_id'] == 'test'

    repo.delete_events(100)

    result8 = repo.search_event('test')

    assert result8 is None

    #error check

    # Card already exist
    with raises(Card_already_exists, match='卡牌id已经存在') as error1:
        cards = [(cid+1, uid1, 'ksm',
                  'ppp', 'voice',
                  3, 100,
                  100, 20, None, None, None)]
        repo.add_cards(cards)


    # Card doesn't exist
    with raises(Card_not_found, match='用户没有该卡牌') as error2:
        repo.set_card_user(cid+2, uid2, cid+2, uid1)


    # User doesn't exist
    with raises(Card_not_found, match='用户没有该卡牌') as error3:
        repo.set_card_user(cid+2, uid2, cid, 'tt')


    # New user
    with raises(User_not_found, match='转让用户不存在！请先让该用户至少操作一次来创建帐号') as error4:
        repo.set_card_user(cid, 'tt', cid+1, uid2)



    #service test
    card_ser = Card_service(repo)

    card_ser.ensure_user_exists('tes')

    result9 = repo.search_user('tes')
    assert result9['user_id'] == 'tes'

    card_dict = card_ser.get_avail_cards_id(uid1, 2)

    assert card_dict['cards_id'] == [1, 3] and card_dict['slots'] == [1]
    
    card_dict = card_ser.get_avail_cards_id(uid1, 1)
    
    assert card_dict['cards_id'] == [1] and card_dict['slots'] == [1]


    #repo.delete_slots([(uid1, 1)])

    card_ser.delete_slots(uid1, [1])

    card_dict = card_ser.get_avail_cards_id(uid1, 2)

    assert card_dict['cards_id'] == [3, 4] and card_dict['slots'] == []

    card_ser.set_slots(uid1, [1, 3, 4])
    
    result10 = repo.search_slots(uid1)

    for r in result10:

        assert r['slot'] == 1

    
    #fund check

    repo.add_fund(uid1, 50)

    fund_ser = Fund_service(repo)

    result11 = fund_ser.fund_check(uid1, 50)

    assert result11 == True

    with raises(Not_enough_fund) as error4:
        fund_ser.fund_check(uid1, 100)


    # Cleaner

    repo.add_event('test', 1)

    cleaner = Cleaner(time_record=1)

    cleaner.cleaning_check(repo.conn)

    result12 = repo.search_event('test')

    assert result12 is None



    # sign_in table

    repo.add_sign_in(uid1, date=99, timestamp=100)

    result13 = repo.search_sign_in(uid1)

    assert result13['user_id'] == uid1

    repo.update_sign_in_date(uid1, 
                             date=100, 
                             past_date=99, 
                             timestamp=101)

    result14 = repo.search_sign_in(uid1)

    assert result14['date'] == 100

    repo.update_sign_in_count(uid1, 1000000)

    result15 = repo.search_sign_in(uid1)

    assert result15['count'] == 2

    #sign_in error check

    with raises(Cooldown, match='正在冷却中，请勿重复操作！') as error5:
        
        repo.update_sign_in_date(uid1, 100, 99, 200)

    with raises(Cooldown, match='正在冷却中，请勿重复操作！') as error6:
        repo.update_sign_in_count(uid1, 1000001)

    with raises(Cooldown, match='正在冷却中，请勿重复操作！') as error7:
        for i in range(4):
            repo.update_sign_in_count('tt', 1000000 + 20000*i)
    
    # sign_in service

    sign_in_ser = Sign_in_service(repo)

    sign_in_ser.ensure_user_exists('tttt')

    sign_in_ser.check_availability('tttt', time_now= 8 * 3600)

    result16 = repo.search_sign_in('tttt')

    assert result16['user_id'] == 'tttt'

    sign_in_ser.check_availability(uid1, time_now= 12 * 3600 + 1)

    sign_in_ser.check_availability(uid1, time_now= 1 * 86400 + 8 * 3600 + 1)



