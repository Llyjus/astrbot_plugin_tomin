from app.services import Fund_service
from app.data_management import connection, Repository
from app.maintenance import event_creater

def funds_giving(amount:int, message_id = None, connect=None):

    event_creater(message_id, connect)

    if connect == None:
        connect = connection()

    with connect as conn:
        repo = Repository(conn)
        repo.all_user_add_fund(amount)

    return f'成功！所有玩家收到奖励：{amount}资金!'

def fund_checker(user_id, message_id, connect=None):
    if connect == None:
        connect = connection()

    with connect as conn:
        repo = Repository(conn)
        fund_ser = Fund_service(repo=repo)
        fund = fund_ser.fund_search(user_id)

    return f'你目前拥有{fund}资金！'

