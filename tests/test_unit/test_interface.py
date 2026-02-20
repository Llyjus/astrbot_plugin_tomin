import pytest
from pydantic import ValidationError
from main import TominPlugin


@pytest.mark.asyncio
async def test_draw_card_success(mocker):
    # only test param parsing and app_inter calling

    fake_context = mocker.Mock()
    fake_event = mocker.Mock()
    fake_event.get_sender_id.return_value = "test"
    fake_event.message_obj.message_id = None
    fake_event.plain_result.side_effect = lambda x: x

    test = TominPlugin(fake_context)

    # mock app_inter
    mock_app_inter = mocker.AsyncMock(
        return_value={"return_type": "str", 
                      "content": "character: ksm",
                      "error": ""}
    )
    mocker.patch("main.app_inter", mock_app_inter)

    fake_input = ["zm20x10", "招募10 1", "招募50", "zm30 1"]

    for msg in fake_input:

        fake_event.message_obj.message_str = msg
        gen = test.draw_card(fake_event)
        result = [x async for x in gen]

        assert isinstance(result[0], str)

    # 4th call should be zm30 1 -> fund_spent=30 times=1
    assert mock_app_inter.await_count == 4
    call = mock_app_inter.await_args_list[3]
    # call.args: (function_name, args_dict)
    assert call.args[0] == "normal_gacha"
    assert call.args[1]["user_id"] == "test"
    assert call.args[1]["fund_spent"] == 30
    assert call.args[1]["times"] == 1

    # param format error: not call app_inter
    before = mock_app_inter.await_count
    fake_event.message_obj.message_str = "szmd"
    gen = test.draw_card(fake_event)
    result = [x async for x in gen]
    assert "命令格式错误" in result[0]
    assert mock_app_inter.await_count == before

    # fund_spent exceed limit
    fake_event.message_obj.message_str = "zm110 2"
    gen = test.draw_card(fake_event)
    result = [x async for x in gen]
    assert "招募资金不能大于50或小于10！" in result[0]


@pytest.mark.asyncio
async def test_sell_card(mocker):
    fake_context = mocker.Mock()
    fake_event = mocker.Mock()

    fake_event.message_obj.message_id = None
    fake_event.message_obj.message_str = "cs1"
    fake_event.get_sender_id.return_value = "test"
    fake_event.plain_result.side_effect = lambda x: x

    plugin = TominPlugin(fake_context)

    # test sell_card interface
    plugin.cleaner.cleaning_check = mocker.Mock()

    mock_app_inter = mocker.AsyncMock(
        return_value={"return_type": "str", 
                      "content": "成功",
                      "error": ""}
    )
    mocker.patch("main.app_inter", mock_app_inter)

    gen = plugin.sell_card(fake_event)
    result = [x async for x in gen]
    assert result[0] == "成功"

    # verify app_inter called with correct params
    mock_app_inter.assert_awaited_once()
    call = mock_app_inter.await_args
    assert call.args[0] == "sell_card_app"
    assert call.args[1]["user_id"] == "test"
    assert call.args[1]["card_id"] == 1

    # param format error: not call app_inter
    mock_app_inter.reset_mock()
    fake_event.message_obj.message_str = "cs 1a"
    gen = plugin.sell_card(fake_event)
    result = [x async for x in gen]
    assert "参数格式错误" in result[0]
    mock_app_inter.assert_not_awaited()
