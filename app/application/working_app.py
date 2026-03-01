from time import time

from app.working import working_func
from app.data_management import Repository, connection
from app.services import Working_service
from app.schemas import *


def start_working_app(user_id, 
                      card_id, 
                      place, 
                      hours, 
                      *, 
                      db_path=None, 
                      connect=None, 
                      time_now=None):
    
    
    connect_bit = 0

    if connect is None:
        connect = connection(path=db_path)
        connect_bit = 1

    with connect as conn:

        if connect_bit == 1:
            connect = None

        repo = Repository(conn)
        wkg_ser = Working_service(repo)
        if not wkg_ser.user_working_number_check(user_id):
            raise Working_card_limit('您已经有3张卡牌在工作中了哦，不能再多啦！')
        
        card = repo.search_card(card_id=card_id, 
                                user_id=user_id)
        if not card:
            raise Card_not_found('没有找到该卡牌！猪...')

        band = card['o_band']
        rarity = card['rarity']
        card_uid = card['card_uid']

        result = working_func(band=band, 
                              rarity=rarity, 
                              place=place, 
                              hours=hours, 
                              current_time=time_now)

        end_time = result['end_time']
        reward_fund = result['wage']

        wkg_ser.start_working(user_id=user_id, 
                                  card_id=card_id, 
                                  card_uid=card_uid,
                                  place=place, 
                                  end_time=end_time, 
                                  reward_fund=reward_fund, 
                                  time_now=time_now)
  
    result = user_working_status_app(user_id, db_path=db_path, connect=connect)

    if result['return_type'] == 'html':
        result['content']['title'] = f'派遣工作成功'
        result['content']['intro'] = f'{card["character"]} 已经开始工作了！目前正在工作和休息的卡牌如下：'
    result['txt'] = f"{card['character']} 已经开始工作了！" + result['txt']
    return result
    

def user_working_status_app(user_id, *, 
                            db_path=None, 
                            connect=None, 
                            current_time=None):
    if connect is None:
        connect = connection(path=db_path)

    with connect as conn:

        repo = Repository(conn)

        wkg_ser = Working_service(repo)

        result = wkg_ser.search_working_by_user(user_id)

        cards_li = []
        cards_txt = f'您目前的卡牌工作状态如下：'
        for card in result:
            if current_time is None:
                current_time = int(time())
            time_diff = card['end_time'] - current_time
            work_sign = False
            status = card['status']
            if status == 'working':
                if time_diff <= 0:
                    status_txt = '工作完成，正在等待结算中...'
                else:
                    status_txt = f'工作中'
                work_sign = True
            elif status == 'resting':
                if time_diff > 0:
                    status_txt = f'休息中\n剩余时间：{(time_diff)//3600}小时{((time_diff)%3600)//60}分钟'
                else:
                    continue

            space = place_out_dict.get(card['space'], )
            

            cards_txt += '\n'
            cards_txt += f"""
            角色：{card['character']}
            稀有度：{card['rarity']}
            id：{card['card_id']}
            状态：{status_txt}
            剩余时间：{f'{(time_diff)//3600}小时{((time_diff)%3600)//60}分钟' if time_diff > 0 else '空闲中~'}
            工作地点：{space if work_sign and space else '无'}
            工资：{card['reward_fund'] if (work_sign and card['reward_fund'] != 0) else '无'}"""



            cards_li.append([f"角色：{card['character']}",
             f"稀有度：{card['rarity']}",
             f"id：{card['card_id']}",
             f"状态：{status_txt}",
             f"工作地点：{space if work_sign and space else '无'}",
             f"工资：{card['reward_fund'] if (work_sign and card['reward_fund'] != 0) else '无'}"
])
        if not cards_li:
            raise Card_not_found('目前没有卡牌在工作和休息了哦！')
        else:
            result = {'return_type':'html',
                    'temp_type':'cards',
                    'content':{'cards':cards_li,
                                'title':'卡牌工作状态',
                                'intro':'目前正在工作和休息的卡牌如下：'},
                    'txt':cards_txt,
                    'user_id': user_id}

    return result

def card_working_status_app(user_id, card_id, *, db_path=None, connect=None):
    if connect is None:
        connect = connection(path=db_path)

    with connect as conn:

        repo = Repository(conn)

        wkg_ser = Working_service(repo)

        card = wkg_ser.search_working_by_card(user_id, card_id)
    
        if not card:
            raise Card_not_found('卡牌没工作过呢！猪...')

    current_time = int(time())
    time_diff = card['end_time'] - current_time
    work_sign = False
    status = card['status']
    if status == 'working':
        if time_diff <= 0:
            status_txt = '工作完成，正在等待结算中...'
        else:
            status_txt = f'工作中\n剩余时间：{time_diff//3600}小时{(time_diff%3600)//60}分钟'
        work_sign = True
    elif status == 'resting':
        if time_diff > 0:
            status_txt = f'休息中\n剩余时间：{(time_diff)//3600}小时{((time_diff)%3600)//60}分钟'
        else:
            status_txt = '空闲中，正在等待新工作...'

    space = place_out_dict.get(card['space'], )
            
    card_li = []
    cards_txt = '您目前的卡牌工作状态如下：'
    cards_txt += f"""
            角色：{card['character']}
            稀有度：{card['rarity']}
            id：{card['card_id']}
            状态：{status_txt}
            工作地点：{space if work_sign and space else '无'}
            工资：{card['reward_fund'] if (work_sign and card['reward_fund'] != 0) else '无'}"""



    card_li.append([f"角色：{card['character']}",
             f"稀有度：{card['rarity']}",
             f"id：{card['card_id']}",
             f"状态：{status_txt}",
             f"工作地点：{space if work_sign and space else '无'}",
             f"工资：{card['reward_fund'] if (work_sign and card['reward_fund'] != 0) else '无'}"
])
        
    result = {'return_type':'html',
                  'temp_type':'cards',
                  'content':{'cards':card_li,
                              'title':f'卡牌工作状态',
                              'intro':f'目前该卡牌状态如下：'},
                  'txt':cards_txt,
                  'user_id': user_id}

    return result

def stop_working_app(user_id, card_id, *, db_path=None, connect=None, time_now=None):

    connect_bit = 0
    if connect is None:
        connect = connection(path=db_path)
        connect_bit = 1

    with connect as conn:
        if connect_bit == 1:
            connect = None
        if time_now is None:
            time_now = int(time())-1

        repo = Repository(conn)
        wkg_ser = Working_service(repo)
        card = repo.search_card(card_id=card_id, 
                                user_id=user_id)
        if not card:
            raise Card_not_found('没有找到该卡牌！猪...')

        card_uid = card['card_uid']

        wkg_ser.stop_working(card_uid, current_time=time_now)
    try:    
        result = user_working_status_app(user_id, db_path=db_path, connect=connect)
        result['txt'] = f"{card['character']} 已经停止工作了！" + result['txt']
        if result['return_type'] == 'html':
            result['content']['title'] = f'停止工作成功'
            result['content']['intro'] = f'{card["character"]} 已经停止工作了！目前正在工作和休息的卡牌如下：'
    except Card_not_found:
        raise Card_not_found(f'{card["character"]} 已经停止工作了！目前没有卡牌在工作和休息了哦！')
    return result


def finish_working_app(user_id, *, db_path=None, connect=None, time_now=None):

    connect_bit = 0
    if connect is None:
        connect = connection(path=db_path)
        connect_bit = 1

    with connect as conn:
        if connect_bit == 1:
            connect = None
        if time_now is None:
            time_now = int(time())


        repo = Repository(conn)
        wkg_ser = Working_service(repo)
        finish_result = wkg_ser.finish_working(user_id, current_time=time_now)

    cards = ', '.join(finish_result['cards_finished'])
    fund_gain = finish_result['wages']
    fund_total = repo.search_user(user_id)['fund']
    try:
        result = user_working_status_app(user_id, db_path=db_path, connect=connect, current_time=time_now)
        # Update result( card who finished must be resting so no "no card" branch)
        result['content']['title'] = '工作结束'
        result['content']['intro'] = f'{cards}结束了工作，获得了{fund_gain}资金，目前总资金为{fund_total}。还在工作和休息的卡牌如下：'
        result['txt'] = f'{cards}结束了工作，获得了{fund_gain}资金，目前总资金为{fund_total}。还在工作和休息的卡牌如下：'
    except Card_not_found:
        raise Card_not_found(f'{cards}结束了工作，获得了{fund_gain}资金，目前总资金为{fund_total}。目前没有卡牌在工作和休息了哦！')
    return result