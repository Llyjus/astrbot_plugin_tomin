from app.data_management import Repository, connection
from app.services import *
from app.maintenance import event_creater
from app.schemas import *

def search_card_app(user_id, card_id, message_id=None, connect=None):
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result:dict = repo.search_card(card_id=card_id, user_id=user_id)
        
        if result is None:
            raise Card_not_found('没有找到该卡牌！猪...')
        card = ''

        card += f'''\n
                卡牌id：{result['card_id']}
                用户id：{result['user_id']}
                角色：{result['character']}
                乐队：{result['o_band']}
                位置：{result['pos']}
                稀有度：{result['rarity']}
                综合力：{result['power']}
                速度：{result['speed']}
                抗性：{result['resistance']}
                技能1：{result['skill_1']}
                技能2：{result['skill_2']}
                技能3：{result['skill_3']}
'''
        
    return result

def search_cards_app(user_id, message_id=None, connect=None):
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_user(user_id)

        cards = '目前拥有卡牌：\n'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards



def search_cards_rarity_app(user_id, rarity, message_id=None, connect=None):
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_rarity(user_id, rarity)

        cards = f'稀有度为{rarity}的卡牌你目前拥有：'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards




def search_cards_band_app(user_id, band, message_id=None, connect=None):
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_band(user_id, band)

        
        cards = f'{band}的角色卡牌你目前拥有：'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards


def search_cards_both_band_rarity(user_id, band, rarity, message_id=None, connect=None):
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_band_rarity(user_id, band, rarity)

        cards = f'{band}角色卡牌你目前拥有：'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards



def give_away_cards_app(giver_id, card_id, accepter_id, message_id=None, connect=None):
    
    event_creater(message_id=message_id, conn=connect)
    
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        cst_ser.card_send_to_user(giver_id, card_id, accepter_id)

        text = '转让卡牌成功！你的宝宝就这样离你远去...\n'

        #return cards left
        text += search_cards_app(giver_id)

    return text





def sell_card_app(user_id, card_id, message_id=None, connect=None):
    
    event_creater(message_id=message_id, conn=connect)
    
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        fund = cst_ser.sell_card(user_id, card_id)


        result = f'出售成功！获得{fund}资金。你好残忍...\n'
        
        fund_total = Fund_service(repo).fund_search(user_id)

        result += f'现在拥有{fund_total}资金!快去消费吧！\n'

        result += search_cards_app(user_id)

     #return: gain_fund, total fund, total cards
    return result




def sell_cards_by_rarity_app(user_id, rarity, message_id=None, connect=None):
    
    event_creater(message_id=message_id, conn=connect)
    
    if connect is None:
        connect = connection()

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        sold_detail = cst_ser.sell_cards_by_rarity(user_id, rarity)

        result = f"出售成功！一共出售{sold_detail['card_sold']}张卡牌，获得{sold_detail['fund_gain']}资金。你好残忍...\n"

        fund_total = Fund_service(repo).fund_search(user_id)

        result += f'现在拥有{fund_total}资金!快去消费吧！\n'

        result += search_cards_app(user_id=user_id)

     #return: gain_fund, total fund, total cards
    return result

