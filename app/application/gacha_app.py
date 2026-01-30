from dataclasses import asdict, astuple
from time import time

from app.gacha import Gacha
from app.data_management import Repository, connection
from app.services import *
from app.maintenance import event_creater



def normal_gacha(user_id, fund_spent, times, message_id=None, gacha_cls = Gacha, connect = None):
    # Use async function for the window of the future 
    
    # transaction atomic
        # Create event
    event_creater(message_id, connect)

    # Find the available card_id and insert into database
    if connect == None:
        connect = connection()
    with connect as conn:

        repo = Repository(conn)

        fund_ser = Fund_service(repo)

        fund_ser.ensure_user_exists(user_id)

        fund_ser.fund_check(user_id, fund_spent * times)

        repo.add_fund(user_id, -fund_spent * times)

        card_ser = Card_service(repo)

        
        # find card id available
        id_dict = card_ser.get_avail_cards_id(user_id, times)

        cards = ''
        cards_tu = []

        for i in id_dict['cards_id']:

            cards += '\n'
            

        # Generate card
            card = gacha_cls().initial(user_id, i, fund_spent)

            # Convert and save
            card_di = asdict(card)
            card_tu = astuple(card)
            cards += f'''\n
卡牌id：{card_di['card_id']}\n
用户id：{card_di['user_id']}\n
角色：{card_di['character']}\n
乐队：{card_di['o_band']}\n
位置：{card_di['pos']}\n
稀有度：{card_di['rarity']}\n
综合力：{card_di['power']}\n
速度：{card_di['speed']}\n
抗性：{card_di['resistance']}\n
技能1：{card_di['skill_1']}\n
技能2：{card_di['skill_2']}\n
技能3：{card_di['skill_3']}\n
'''
            cards_tu.append(card_tu)

        try:

            repo.add_cards(cards_tu)

            id_dict['slots'] = [(user_id, n) for n in id_dict['slots']]

            repo.delete_slots(id_dict['slots'])

        except Exception as e:

            #rollback the fund to user, raise to let conn rollback the operation
            
            raise RuntimeError('抽卡成功，连接数据库失败，请稍后再试') from e
        
    return cards



def free_gacha(user_id, message_id=None, gacha_cls = Gacha, connect = None):

    if connect is None:
        with connection() as conn:
            avail = Sign_in_service(Repository(conn))
            avail.ensure_user_exists(user_id)
            result = avail.check_availability(user_id)
            result += '成功抽取卡牌:\n'

        result += normal_gacha(user_id, 0, 1, message_id, gacha_cls)
        
    else:
        with connect as conn:
            avail = Sign_in_service(Repository(conn))
            avail.ensure_user_exists(user_id)
            result = avail.check_availability(user_id)
            result += '成功抽取卡牌:\n'
            result += normal_gacha(user_id, 0, 1, message_id, gacha_cls, connect=connect)
    
    return result










