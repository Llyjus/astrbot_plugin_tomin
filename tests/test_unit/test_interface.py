import pytest

from main import Tomin

@pytest.mark.asyncio
async def test_draw_card_success(mocker):

    # Mock 2 fake object
    fake_context = mocker.Mock()

    fake_event = mocker.Mock()
    fake_event.get_sender_id.return_value = "test"
    fake_event.plain_result.side_effect = lambda x: x


    
    test = Tomin(fake_context)

    # Patch the file Tomin imported
    mocker.patch(
        "main.normal_gacha",
        return_value={"character": "ksm", 'user_id': 'test'}
    )

    card = test.draw_card(fake_event, fund_spent=10)
    result = [msg async for msg in card]
            
    assert 'character: ksm' in result[0]

