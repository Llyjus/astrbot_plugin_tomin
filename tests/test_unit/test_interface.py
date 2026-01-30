import pytest 
from pytest import raises
from pydantic import ValidationError

from main import TominPlugin

@pytest.mark.asyncio
async def test_draw_card_success(mocker):

    # Mock 2 fake object
    fake_context = mocker.Mock()

    fake_event = mocker.Mock()

    fake_event.get_sender_id.return_value = "test"
    fake_event.plain_result.side_effect = lambda x: x

    fake_input= ["zm20x2", 
                                                "招募100 1", 
                                                "招募40", 
                                                "zm20 100"]




    test = TominPlugin(fake_context)

    # Patch the file Tomin imported
    mock_gacha = mocker.patch(
        "main.normal_gacha",
        return_value="character: ksm")

    

    for i in fake_input:
        fake_event.message_obj.message_str = i
        card = test.draw_card(fake_event)




        result = [msg async for msg in card]


        args, kwargs = mock_gacha.call_args

        calls = mock_gacha.call_args_list

    assert calls[0].args[1] == 20 and calls[0].args[2] == 2

            
    assert 'character: ksm' in result[0]


    fake_event.message_obj.message_str = 'szmd'

    card = test.draw_card(fake_event)

    result = [msg async for msg in card]

    assert '命令格式错误' in result[0]

    fake_event.message_obj.message_str = 'zm101x100'
    card = test.draw_card(fake_event)
    result = [msg async for msg in card]


    fake_event.message_obj.message_str = 'zm110 2'
    card = test.draw_card(fake_event)
    result = [msg async for msg in card]

    assert '招募资金不能大于50或小于10！' in result[0]




@pytest.mark.asyncio
async def test_sell_card(mocker):

    # test interface function sell card
    fake_context = mocker.Mock()

    fake_event = mocker.Mock()

    fake_event.message_obj.message_id = 1
    fake_event.message_obj.message_str = 'cs1'
    fake_event.get_sender_id.return_value = 'test'
    fake_event.plain_result.side_effect = lambda x: x


    fake_cls = TominPlugin(fake_context)


    mock_sell = mocker.patch(
        'main.sell_card_app', return_value='成功')
    


    r = fake_cls.sell_card(fake_event)


    result = [msg async for msg in r]

    assert result[0] == '成功'
    
    args, kwargs = mock_sell.call_args

    calls = mock_sell.call_args_list

    assert calls[0].args[0] == 'test'
