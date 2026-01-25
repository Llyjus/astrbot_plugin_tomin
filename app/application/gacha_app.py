from dataclasses import asdict, astuple
from asyncio import get_running_loop

from app.gacha import Gacha
from app.data_management import Repository, connection


async def normal_gacha(user_id, fund_spent, times, gacha_cls = Gacha, conn = connection()):
    # Use async function for the window of the future 


    # Find the available card_id and insert into database
    with conn:
        repo = Repository(conn)
        user = repo.search_user(user_id)

        if user == None:
            repo.add_user(user_id)
            user = repo.search_user(user_id)
        
        fund = user['fund']
        if fund < fund_spent * times:
            raise ValueError(f'用户资金不足，无法招募！你现在的资金是：{fund}')
        
        repo.add_fund(user_id, - fund_spent * times)

        
        # find card id available
        last_card = repo.search_card_last(user_id)
        if last_card == None:
            card_id = 0
        else:
            card_id = last_card['card_id']

        cards = ''
        cards_tu = []

        

        for _ in range(times):

            cards += '\n'
            
        # Generate card
            card_id += 1

            gacha = gacha_cls()

            bonus = max((fund_spent-10) * 0.1, 0)
            card = gacha.initial(user_id, card_id, bonus)

            # Convert and save
            card_di = asdict(card)
            card_tu = astuple(card)
            for key, value in card_di.items():
                cards += f"{key}：{value}\n"
            cards_tu.append(card_tu)

        # Sub-thread in the future when needed

        try:

            repo.add_cards(cards_tu)

        except Exception as e:

            #rollback the fund to user, raise to let conn rollback the operation
            repo.add_fund(user_id, + fund_spent * times)
            raise RuntimeError('抽卡成功，连接数据库失败，请稍后再试') from e
        
        return cards