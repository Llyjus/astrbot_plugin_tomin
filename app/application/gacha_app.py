from dataclasses import asdict, astuple
from time import time

from app.gacha import Gacha
from app.data_management import Repository, connection
from app.services import *
from app.maintenance import event_creater



<<<<<<< HEAD
def normal_gacha(user_id, fund_spent, times, *, db_path=None, gacha_cls = Gacha, connect = None):
    # Use async function for the window of the future 


    # Find the available card_id and insert into database
    if connect == None:
        connect = connection(path=db_path)
=======
def normal_gacha(user_id, fund_spent, times, message_id=None, gacha_cls = Gacha, connect = None):
    # Use async function for the window of the future 
    
    # transaction atomic
        # Create event
    event_creater(message_id, connect)

    # Find the available card_id and insert into database
    if connect == None:
        connect = connection()
>>>>>>> origin/develop
    with connect as conn:

        repo = Repository(conn)

        fund_ser = Fund_service(repo)

        fund_ser.ensure_user_exists(user_id)

        fund_ser.fund_check(user_id, fund_spent * times)

        repo.add_fund(user_id, -fund_spent * times)

        card_ser = Card_service(repo)

        
        # find card id available
        id_dict = card_ser.get_avail_cards_id(user_id, times)

<<<<<<< HEAD
        cards_txt = f'您花费{fund_spent * times}资金成功抽取到了{times}张卡牌：'
        cards_tu = []
        cards_li = []

        for i in id_dict['cards_id']:

            cards_txt += '\n'
=======
        cards = ''
        cards_tu = []

        for i in id_dict['cards_id']:

            cards += '\n'
>>>>>>> origin/develop
            

        # Generate card
            card = gacha_cls().initial(user_id, i, fund_spent)

            # Convert and save
            card_di = asdict(card)
            card_tu = astuple(card)
<<<<<<< HEAD

            cards_txt += f'''
卡牌id：{card_di['card_id']}
用户id：{card_di['user_id']}
角色：{card_di['character']}
乐队：{card_di['o_band']}
稀有度：{card_di['rarity']}
'''
            cards_li.append([f"卡牌id：{card_di['card_id']}",
                             f"用户id：{card_di['user_id']}",
                             f"角色：{card_di['character']}",
                             f"乐队：{card_di['o_band']}",
                            f"稀有度：{card_di['rarity']}"])
            
=======
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
>>>>>>> origin/develop
            cards_tu.append(card_tu)

        try:

            repo.add_cards(cards_tu)

            id_dict['slots'] = [(user_id, n) for n in id_dict['slots']]

            repo.delete_slots(id_dict['slots'])

        except Exception as e:

            #rollback the fund to user, raise to let conn rollback the operation
            
            raise RuntimeError('抽卡成功，连接数据库失败，请稍后再试') from e
        
<<<<<<< HEAD
    result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':cards_li,
                              'title':'抽卡结果',
                              'intro':f'您花费{fund_spent * times}资金成功抽取到了{times}张卡牌：'},
                  'txt':cards_txt}
    return result



def free_gacha(user_id, *, db_path=None, gacha_cls = Gacha, connect = None):

    context_bit = 0

    if connect is None:
        connect = connection(path=db_path)
        context_bit = 1

    with connect as conn:

        if context_bit == 1:
            connect = None

        repo = Repository(conn)

        avail = Sign_in_service(repo=repo)
        avail.ensure_user_exists(user_id)

        cards_intro = avail.check_availability(user_id)

        # gacha
        card_ser = Card_service(repo)

        
        # find card id available
        id_dict = card_ser.get_avail_cards_id(user_id, 1)

        cards_intro += '抽取到了：'
        cards_tu = []
        cards_li = []



        cards_txt = cards_intro + '\n'
            

        # Generate card
        card = gacha_cls().initial(user_id, id_dict['cards_id'][0], 0)

            # Convert and save
        card_di = asdict(card)
        card_tu = astuple(card)

        cards_txt += f'''
卡牌id：{card_di['card_id']}
用户id：{card_di['user_id']}
角色：{card_di['character']}
乐队：{card_di['o_band']}
稀有度：{card_di['rarity']}
'''
        cards_li.append([f"卡牌id：{card_di['card_id']}",
                             f"用户id：{card_di['user_id']}",
                             f"角色：{card_di['character']}",
                             f"乐队：{card_di['o_band']}",
                            f"稀有度：{card_di['rarity']}"])
            
        cards_tu.append(card_tu)

        try:

            repo.add_cards(cards_tu)

            id_dict['slots'] = [(user_id, n) for n in id_dict['slots']]

            repo.delete_slots(id_dict['slots'])

        except Exception as e:

            #rollback the fund to user, raise to let conn rollback the operation
            
            raise RuntimeError('打卡未成功，连接数据库失败，请稍后再试') from e
        
    result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':cards_li,
                              'title':'打卡成功',
                              'intro':f'{cards_intro}'},
                  'txt':cards_txt}
        
=======
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
    
>>>>>>> origin/develop
    return result



<<<<<<< HEAD
=======







>>>>>>> origin/develop
