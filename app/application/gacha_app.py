from dataclasses import asdict, astuple
from asyncio import get_running_loop

from app.gacha import Gacha
from app.data_management import Repository, connection
from app.services import Card_service, Fund_service


def normal_gacha(user_id, fund_spent, times, gacha_cls = Gacha, conn = None):
    # Use async function for the window of the future 

    if conn is None:
        conn = connection()

    # Find the available card_id and insert into database
    with conn:
        repo = Repository(conn)

        fund_ser = Fund_service(repo)

        fund_ser.user_exists(user_id)

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

            for key, value in card_di.items():
                cards += f"{key}：{value}\n"
            cards_tu.append(card_tu)

        try:

            repo.add_cards(cards_tu)

            id_dict['slots'] = [(user_id, n) for n in id_dict['slots']]

            repo.delete_slots(id_dict['slots'])

        except Exception as e:

            #rollback the fund to user, raise to let conn rollback the operation
            
            raise RuntimeError('抽卡成功，连接数据库失败，请稍后再试') from e
        
    return cards