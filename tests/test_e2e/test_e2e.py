from pathlib import Path
import base64

from pytest_mock import MockerFixture
from pytest import mark


from main import TominPlugin
from tests.utils import db_checker
from app.data_management import Repository, connection


@mark.asyncio
async def test_of_e2e(mocker: MockerFixture, e2e_database):

    fake_context = mocker.Mock()

    class Fake_renderer():
        def __init__(self):
            pass

        async def render(self, html):
            FAKE_PNG_B64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+X2ZQAAAAASUVORK5CYII="
            FAKE_PNG_BYTES = base64.b64decode(FAKE_PNG_B64)
            return FAKE_PNG_BYTES

    db_path = e2e_database
    tomin = TominPlugin(fake_context)
    tomin.data_path = db_path
    tomin.picture_path = Path(tomin.data_path).parent
    tomin.renderer = Fake_renderer()






    # part1: ensure the picture exists when sending
    def picture_exists(path):
        assert Path(path).exists()
        return True

    # fake message event
    fake_dk_event1 = mocker.Mock()
    fake_dk_event1.get_sender_id.return_value = "user1"
    fake_dk_event1.message_obj.message_id = '1'
    fake_dk_event1.image_result = mocker.Mock(side_effect=picture_exists)
    fake_dk_event1.plain_result.side_effect = lambda x: x

    # test sign in 
    # and return picture successfully
    user1_dk = tomin.sign_in(fake_dk_event1)
    user1_dk_result = [msg async for msg in user1_dk][0]
    assert user1_dk_result == True




    # part2: i) Testing the sentence returned  
    #          when timeout happens in renderer 
    #        ii) Testing the normal gacha function

    class Timeout_renderer():
        def __init__(self):
            pass

        async def render(self, html):
            raise TimeoutError("超时")
        
    tomin.renderer = Timeout_renderer()


    fake_zm_event2 = mocker.Mock()
    fake_zm_event2.get_sender_id.return_value = "222"
    fake_zm_event2.message_obj.message_id = '2'
    fake_zm_event2.message_obj.message_str = "zm10 1"
    fake_zm_event2.plain_result.side_effect = lambda x: x

    user2_zm = tomin.draw_card(fake_zm_event2)
    user2_zm_result = [msg async for msg in user2_zm][0]
    assert "生成图片超时" in user2_zm_result
    assert "您花费10资金成功抽取到了1张卡牌" in user2_zm_result

    user2_zm = tomin.draw_card(fake_zm_event2)
    user2_zm_result = [msg async for msg in user2_zm][0]
    assert "重复执行" in user2_zm_result


    # part3: i)Testing the give away function 
    #        ii)Testing the slot
    fake_zm_event3 = mocker.Mock()
    fake_zm_event3.get_sender_id.return_value = "user1"
    fake_zm_event3.message_obj.message_id = '3'
    fake_zm_event3.message_obj.message_str = "zm10 1"
    fake_zm_event3.image_result = mocker.Mock(side_effect=picture_exists)
    fake_zm_event3.plain_result.side_effect = lambda x: x

    user1_zm = tomin.draw_card(fake_zm_event3)
    user1_zm_result = [msg async for msg in user1_zm][0]



    fake_zs_event4 = mocker.Mock()
    fake_zs_event4.get_sender_id.return_value = "user1"
    fake_zs_event4.message_obj.message_id = '4'
    fake_zs_event4.message_obj.message_str = "zs222 1"
    fake_zs_event4.plain_result.side_effect = lambda x: x
    user1_zs = tomin.give_card_away(fake_zs_event4)
    user1_zs_result = [msg async for msg in user1_zs][0]
    assert "目前拥有卡牌：" in user1_zs_result


    # part4: Test the slots
    with connection(tomin.data_path) as conn:
        repo = Repository(conn=conn)
        last_checker = db_checker(repo=repo)

    assert last_checker == True


    