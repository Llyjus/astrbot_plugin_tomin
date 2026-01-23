from dataclasses import asdict


from app.gacha.service.gacha import Gacha
from app.data_management.services.repository import Repository
from app.data_management.services.connection import connection


def normal_gacha(user_id, fund_spent=10, gacha_cls = Gacha, conn = connection()):

    # Find the available card_id and insert into database
    with conn:
        repo = Repository(conn)
        user = repo.search_user(user_id)

        if user == None:
            repo.add_user(user_id)
            user = repo.search_user(user_id)
        
        fund = user['fund']
        if fund < fund_spent:
            raise ValueError(f'用户资金不足，无法招募！你现在的资金是：{fund}')
        
        repo.add_fund(user_id, -fund_spent)


        last_card = repo.search_card_last(user_id)
        if last_card == None:
            card_id = 1
        else:
            card_id = last_card['card_id'] + 1

        # Generate card

        gacha = gacha_cls()

        bonus = max((fund_spent-10) * 0.1, 0)
        card = gacha.initial(user_id, card_id, bonus)

        card = asdict(card)
        repo.add_card(**card)
    
        return card