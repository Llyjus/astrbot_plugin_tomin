from app.data_management import Repository, connection
from app.services import *
from app.maintenance import event_creater
from app.schemas import *

<<<<<<< HEAD
def search_card_app(user_id, card_id, *, db_path=None, connect=None):
    if connect is None:
        connect = connection(path=db_path)
=======
def search_card_app(user_id, card_id, message_id=None, connect=None):
    if connect is None:
        connect = connection()
>>>>>>> origin/develop

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result:dict = repo.search_card(card_id=card_id, user_id=user_id)
        
        if result is None:
            raise Card_not_found('没有找到该卡牌！猪...')
<<<<<<< HEAD


    cards_li = [[   f"卡牌id：{result['card_id']}",
                f"用户id：{result['user_id']}",
                f"角色：{result['character']}",
                f"乐队：{result['o_band']}",
                f"位置：{result['pos']}",
                f"稀有度：{result['rarity']}",
                f"综合力：{result['power']}",
                f"速度：{result['speed']}",
                f"抗性：{result['resistance']}"]]
    card_txt = f'''这是你查询到的卡牌信息：
卡牌id：{result['card_id']}
用户id：{result['user_id']}
角色：{result['character']}
乐队：{result['o_band']}
位置：{result['pos']}
稀有度：{result['rarity']}
综合力：{result['power']}
速度：{result['speed']}
抗性：{result['resistance']}'''
    
    result = {'return_type':'html',
              'temp_type':'cards',
              'content':{'cards':cards_li,
                         'title':'卡牌信息',
                         'intro':'这是你查询到的卡牌信息：'},
              'txt':card_txt
                         }

        
    return result

def search_cards_app(user_id, *, db_path=None, connect=None):
    if connect is None:
        connect = connection(path=db_path)
=======
        card = ''

        card += f'''卡牌id：{result['card_id']}
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
        
    return card

def search_cards_app(user_id, message_id=None, connect=None):
    if connect is None:
        connect = connection()
>>>>>>> origin/develop

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

<<<<<<< HEAD
        cards = cst_ser.cards_search_by_user(user_id)

        cards_li = []

        cards_txt = '目前拥有卡牌：\n'
        for card in cards:
            cards_txt += '\n'
            cards_txt += f"角色：{card['character']}\n稀有度：{card['rarity']}\n卡牌id：{card['card_id']}\n"
            cards_li.append([
                             f"角色：{card['character']}",
                             f"稀有度：{card['rarity']}",
                             f"卡牌id：{card['card_id']}"
                             ])
    result = {'return_type':'html',
              'temp_type':'cards',
              'content':{'cards':cards_li,
                         'title':'卡牌信息',
                         'intro':'目前拥有卡牌：'},
              'txt':cards_txt}

    return result



def search_cards_rarity_app(user_id, rarity, *, db_path=None, connect=None):
    if connect is None:
        connect = connection(path=db_path)
=======
        result = cst_ser.cards_search_by_user(user_id)

        cards = '目前拥有卡牌：\n'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards



def search_cards_rarity_app(user_id, rarity, message_id=None, connect=None):
    if connect is None:
        connect = connection()
>>>>>>> origin/develop

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_rarity(user_id, rarity)

<<<<<<< HEAD

        cards_li = []
        cards_txt = f'稀有度为{rarity}的卡牌你目前拥有：'
        for card in result:
            cards_txt += '\n'
            cards_txt += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"
            cards_li.append([f"角色：{card['character']}",
                             f"稀有度：{card['rarity']}",
                             f"id：{card['card_id']}"
                             ])
        
        result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':cards_li,
                              'title':f'稀有度{rarity}卡牌查询结果',
                              'intro':f'稀有度为{rarity}的卡牌你目前拥有：'},
                  'txt':cards_txt}

    return result
=======
        cards = f'稀有度为{rarity}的卡牌你目前拥有：'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards
>>>>>>> origin/develop




<<<<<<< HEAD
def search_cards_band_app(user_id, band, *, db_path=None, connect=None):
    if connect is None:
        connect = connection(path=db_path)
=======
def search_cards_band_app(user_id, band, message_id=None, connect=None):
    if connect is None:
        connect = connection()
>>>>>>> origin/develop

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_band(user_id, band)

<<<<<<< HEAD
        cards_li = []
        cards_txt = f'{band}的角色卡牌你目前拥有：'
        for card in result:
            cards_txt += '\n'
            cards_txt += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"
            cards_li.append([f"角色：{card['character']}",
                             f"稀有度：{card['rarity']}",
                             f"id：{card['card_id']}"
                             ])
            
        result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':cards_li,
                              'title':f'{band}卡牌查询结果',
                              'intro':f'{band}的角色卡牌你目前拥有：'},
                  'txt':cards_txt}

    return result


def search_cards_both_band_rarity(user_id, band, rarity, *, db_path=None, connect=None):
    if connect is None:
        connect = connection(path=db_path)
=======
        
        cards = f'{band}的角色卡牌你目前拥有：'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards


def search_cards_both_band_rarity(user_id, band, rarity, message_id=None, connect=None):
    if connect is None:
        connect = connection()
>>>>>>> origin/develop

    with connect as conn:

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        result = cst_ser.cards_search_by_band_rarity(user_id, band, rarity)

<<<<<<< HEAD
        cards_txt = f'{band}角色卡牌你目前拥有：'
        cards_li = []
        for card in result:
            cards_txt += '\n'
            cards_txt += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"
            cards_li.append([f"角色：{card['character']}",
                             f"稀有度：{card['rarity']}",
                             f"id：{card['card_id']}"
                             ])

    result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':cards_li,
                              'title':f'{band} {rarity}卡牌查询结果',
                              'intro':f'{band}角色卡牌你目前拥有：'},
                  'txt':cards_txt}

    return result



def give_away_cards_app(giver_id, card_id, accepter_id, *, db_path=None, connect=None):
    
    context_bit = 0
    
    if connect is None:
        connect = connection(path=db_path)
        context_bit = 1
        
    with connect as conn:

        if context_bit == 1:
            connect = None

        repo = Repository(conn)
        cst_ser = Card_storage_service(repo)
        slot_list = cst_ser.card_send_to_user(giver_id, card_id, accepter_id)

        #add slot
        card_ser = Card_service(repo)
        card_ser.set_slots(user_id=giver_id, slot_list=[card_id])
        #delete slot
        card_ser.delete_slots(user_id=accepter_id, slot_list=slot_list)


        text = '转让卡牌成功！你的宝宝就这样离你远去...\n'

            #return cards left
    try:
        result = search_cards_app(giver_id, db_path=db_path, connect=connect)
        result['content']['intro'] = '转让卡牌成功！你的宝宝就这样离你远去...剩余卡牌：'
        result['content']['title'] = '转让卡牌成功'
        text += result['txt']
    except Card_not_found:
        result = {'return_type':'str',
                    'content': text + '你没有其它卡牌啦！'}

    return result
=======
        cards = f'{band}角色卡牌你目前拥有：'
        for card in result:
            cards += '\n'
            cards += f"角色：{card['character']}\n稀有度：{card['rarity']}\nid：{card['card_id']}\n"

    return cards



def give_away_cards_app(giver_id, card_id, accepter_id, message_id=None, connect=None):
    
    event_creater(message_id=message_id, conn=connect)
    
    if connect is None:
        
        with connection() as conn:

            repo = Repository(conn)
            cst_ser = Card_storage_service(repo)
            slot_list = cst_ser.card_send_to_user(giver_id, card_id, accepter_id)

            #add slot
            card_ser = Card_service(repo)
            card_ser.set_slots(user_id=giver_id, slot_list=[card_id])
            #delete slot
            card_ser.delete_slots(user_id=accepter_id, slot_list=slot_list)
    else:
        with connect as conn:

            repo = Repository(conn)
            cst_ser = Card_storage_service(repo)
            slot_list = cst_ser.card_send_to_user(giver_id, card_id, accepter_id)
            
            #add slot
            card_ser = Card_service(repo)
            card_ser.set_slots(user_id=giver_id, slot_list=[card_id])
            #delete slot
            card_ser.delete_slots(user_id=accepter_id, slot_list=slot_list)

    text = '转让卡牌成功！你的宝宝就这样离你远去...\n'

        #return cards left
    try:
        text += search_cards_app(giver_id, connect=connect)

    except Card_not_found:
        text += '你没有其它卡牌啦！'




    return text
>>>>>>> origin/develop





<<<<<<< HEAD
def sell_card_app(user_id, card_id, *, db_path=None, connect=None):
    
    context_bit = 0
    
    if connect is None:
        connect = connection(path=db_path)
        context_bit = 1
        
    with connect as conn:

        if context_bit == 1:
            connect = None

        repo = Repository(conn)

        cst_ser = Card_storage_service(repo)

        fund = cst_ser.sell_card(user_id, card_id)

            
        fund_total = Fund_service(repo).fund_search(user_id)


        #add slot
        card_ser = Card_service(repo)
        card_ser.set_slots(user_id=user_id, slot_list=[card_id])



        text = f'出售成功！获得{fund}资金。你好残忍...\n现在拥有{fund_total}资金!快去消费吧！\n'
        
        # search after submiting
    try:
        result = search_cards_app(user_id=user_id, db_path=db_path, connect=connect)
        result['content']['intro'] = f'出售成功！获得{fund}资金。你好残忍...\n现在拥有{fund_total}资金!快去消费吧！'
        result['content']['title'] = '出售成功'
        text += result['txt']
        result['txt'] = text
        
    except Card_not_found:
        result = {'return_type':'str',
                    'content': text + '你没有其它卡牌啦！'}

=======
def sell_card_app(user_id, card_id, message_id=None, connect=None):
    
    event_creater(message_id=message_id, conn=connect)
    
    if connect is None:
        with connection() as conn:

            repo = Repository(conn)

            cst_ser = Card_storage_service(repo)

            fund = cst_ser.sell_card(user_id, card_id)

            
            fund_total = Fund_service(repo).fund_search(user_id)


            #add slot
            card_ser = Card_service(repo)
            card_ser.set_slots(user_id=user_id, slot_list=[card_id])

    else:
        with connect as conn:

            repo = Repository(conn)
            cst_ser = Card_storage_service(repo)
            fund = cst_ser.sell_card(user_id, card_id)

            
            fund_total = Fund_service(repo).fund_search(user_id)


            #add slot
            card_ser = Card_service(repo)
            card_ser.set_slots(user_id=user_id, slot_list=[card_id])

    result = f'出售成功！获得{fund}资金。你好残忍...\n现在拥有{fund_total}资金!快去消费吧！\n'
    
    # search after submiting
    try:
        result += search_cards_app(user_id=user_id, connect=connect)

    except Card_not_found:
        result += '你没有其它卡牌啦！'


     #return: gain_fund, total fund, total cards
>>>>>>> origin/develop
    return result




<<<<<<< HEAD
def sell_cards_by_rarity_app(user_id, rarity, *, db_path=None, connect=None):
    
    context_bit = 0
    
    if connect is None:
        connect = connection(path=db_path)
        context_bit = 1
        
    with connect as conn:

        if context_bit == 1:
            connect = None

        repo = Repository(conn)
        cst_ser = Card_storage_service(repo)
        sold_detail = cst_ser.sell_cards_by_rarity(user_id, rarity)

        #add slots
        card_ser = Card_service(repo)
        card_ser.set_slots(user_id=user_id, slot_list=sold_detail['cards_id_list'])
            
        fund_total = Fund_service(repo).fund_search(user_id)



        text = f"出售成功！一共出售{sold_detail['cards_sold']}张卡牌，获得{sold_detail['fund_gain']}资金。你好残忍...\n现在拥有{fund_total}资金!快去消费吧！\n"
    
    try:
        result = search_cards_app(user_id=user_id, db_path=db_path, connect=connect)
        result['content']['intro'] = f"出售成功！\n一共出售{sold_detail['cards_sold']}张卡牌，获得{sold_detail['fund_gain']}资金。你好残忍...\n剩余卡牌："
        result['content']['title'] = '出售成功'
        text += result['txt']
        result['txt'] = text

    except Card_not_found:
        result = {'return_type':'str',
                    'content': text + '你没有其它卡牌啦！'}

=======
def sell_cards_by_rarity_app(user_id, rarity, message_id=None, connect=None):
    
    event_creater(message_id=message_id, conn=connect)
    
    if connect is None:
        with connection() as conn:

            repo = Repository(conn)
            cst_ser = Card_storage_service(repo)
            sold_detail = cst_ser.sell_cards_by_rarity(user_id, rarity)

            #add slots
            card_ser = Card_service(repo)
            card_ser.set_slots(user_id=user_id, slot_list=sold_detail['cards_id_list'])
            
            fund_total = Fund_service(repo).fund_search(user_id)
    
    else:
        with connect as conn:

            repo = Repository(conn)
            cst_ser = Card_storage_service(repo)
            sold_detail = cst_ser.sell_cards_by_rarity(user_id, rarity)

            #add slots
            card_ser = Card_service(repo)
            card_ser.set_slots(user_id=user_id, slot_list=sold_detail['cards_id_list'])
            
            fund_total = Fund_service(repo).fund_search(user_id)


    result = f"出售成功！一共出售{sold_detail['cards_sold']}张卡牌，获得{sold_detail['fund_gain']}资金。你好残忍...\n现在拥有{fund_total}资金!快去消费吧！\n"
    try:
        result += search_cards_app(user_id=user_id, connect=connect)

    except Card_not_found:
        result += '你没有其它卡牌啦！'
        
     #return: gain_fund, total fund, total cards
>>>>>>> origin/develop
    return result
