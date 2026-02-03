from dataclasses import asdict, astuple
from time import time

from app.gacha import Gacha
from app.data_management import Repository, connection
from app.services import *
from app.maintenance import event_creater



def normal_gacha(user_id, fund_spent, times, *, gacha_cls = Gacha, connect = None):
    # Use async function for the window of the future 


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

        cards_txt = f'您花费{fund_spent * times}资金成功抽取到了{times}张卡牌：'
        cards_tu = []
        cards_li = []

        for i in id_dict['cards_id']:

            cards_txt += '\n'
            

        # Generate card
            card = gacha_cls().initial(user_id, i, fund_spent)

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
            
            raise RuntimeError('抽卡成功，连接数据库失败，请稍后再试') from e
        
    result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':cards_li,
                              'title':'抽卡结果',
                              'intro':f'您花费{fund_spent * times}资金成功抽取到了{times}张卡牌：'},
                  'txt':cards_txt}
    return result



def free_gacha(user_id, *, gacha_cls = Gacha, connect = None):

    context_bit = 0

    if connect is None:
        connect = connection()
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
        
    return result



