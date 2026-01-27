import pytest 
from pytest import raises

from main import Tomin

@pytest.mark.asyncio
async def test_draw_card_success(mocker):

    # Mock 2 fake object
    fake_context = mocker.Mock()

    fake_event = mocker.Mock()
    fake_event.get_message_text.return_value = ["zm20x2", 
                                                "招募100 1", 
                                                "招募40", 
                                                "zm20 100"]
    fake_event.get_sender_id.return_value = "test"
    fake_event.plain_result.side_effect = lambda x: x


    
    test = Tomin(fake_context)

    # Patch the file Tomin imported
    mock_gacha = mocker.patch(
        "main.normal_gacha",
        return_value="character: ksm")

    

    for i in fake_event.get_message_text.return_value:
        fake_event.get_message_text.return_value = i
        card = test.draw_card(fake_event)



        result = [msg async for msg in card]


        args, kwargs = mock_gacha.call_args


        calls = mock_gacha.call_args_list

        assert calls[0].args[1] == 20 and calls[0].args[2] == 2

            
        assert 'character: ksm' in result[0]


        fake_event.get_message_text.return_value = 'szmd'

        card = test.draw_card(fake_event)

        result = [msg async for msg in card]

        assert '命令格式错误' in result[0]