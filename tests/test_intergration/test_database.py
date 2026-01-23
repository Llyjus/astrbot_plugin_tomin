import sys
import os
from pytest import raises


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
    with raises(ValueError, match='用户已经存在') as error1:
        repo.add_user('test')



    # Illegal value
    with raises(ValueError, match='余额不足或用户不存在') as error2:
        repo.add_fund('test', -100)




def test_cards_table(memory_db_connection):
    repo = memory_db_connection
    uid1 = 'test'
    uid2 = 't'
    cid = 1

    repo.add_user(uid1)
    repo.add_user(uid2)


    # Test adding&searching card
    repo.add_card(card_id=cid, user_id=uid1, character='ksm',
                  o_band='ppp', pos='voice',
                  rarity=3, power=100,
                  speed=100, resistance=20, skill_1=None, skill_2=None, skill_3=None)
    repo.add_card(card_id=cid, user_id=uid2, character='ksm',
                  o_band='ppp', pos='voice',
                  rarity=3, power=100,
                  speed=100, resistance=20, skill_1=None, skill_2=None, skill_3=None)



    result1 = repo.search_card(cid, uid1)

    assert result1['card_id'] == cid
    assert result1['user_id'] == uid1


    repo.add_card(card_id=cid+1, user_id=uid1, character='ksm',
                  o_band='ppp', pos='voice',
                  rarity=3, power=100,
                  speed=100, resistance=20, skill_1=None, skill_2=None, skill_3=None)


    result2 = repo.search_card_last('test')

    assert result2['card_id'] == 2


    result3 = repo.search_cards(uid1)

    for r in result3:
        assert r['card_id'] == 1 or r['card_id'] == 2




    #set_card_user

    #Should check the available card id in real circumstance 
    # but now may not

    repo.set_card_user(cid+1, uid2, cid+1, uid1)

    result4 = repo.search_card(cid+1, uid2)

    assert result4['user_id'] == 't' and result4['card_id'] == 2





    #error check

    # Card already exist
    with raises(Exception, match='卡牌id已经存在') as error1:
        repo.add_card(card_id=cid, user_id=uid1, character='ksm',
                  o_band='ppp', pos='voice',
                  rarity=3, power=100,
                  speed=100, resistance=20, skill_1=None, skill_2=None, skill_3=None)


    # Card doesn't exist
    with raises(ValueError, match='原用户不存在或用户没有该卡牌') as error2:
        repo.set_card_user(cid+2, uid2, cid+2, uid1)


    # User doesn't exist
    with raises(ValueError, match='原用户不存在或用户没有该卡牌') as error3:
        repo.set_card_user(cid+2, uid2, cid, 'tt')


    # New user
    with raises(ValueError, match='转让用户不存在！请先让该用户至少操作一次来创建帐号') as error4:
        repo.set_card_user(cid, 'tt', cid+1, uid2)





    

    
    


    



    
   