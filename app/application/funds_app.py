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