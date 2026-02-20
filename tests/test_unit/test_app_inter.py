from pytest_mock import MockerFixture
from pytest import raises
import pytest

from app.interface import app_inter
from app.schemas import Invalid_input
from tests.utils import fake_application_fixture


@pytest.mark.asyncio
async def test_app_inter_func_call(mocker: MockerFixture, fake_application_fixture):

    fake_app_dict, fake_kwargs = fake_application_fixture
    result1 = await app_inter('normal_gacha', 
                    fake_kwargs, 
                    app_dict=fake_app_dict)
    
    assert result1['content'] == '成功'
    

    with raises(Invalid_input) as error1:
        await app_inter('x_func', {})
    assert '函数名称错误' in str(error1.value)

@pytest.mark.asyncio
async def test_app_renderer_fallback(mocker: MockerFixture, fake_application_fixture):
    fake_app_dict, fake_kwargs = fake_application_fixture

    # mock the renderer
    class fake_renderer():
        def __init__(self):
            pass

        async def render(self, html):
            raise TimeoutError("超时")

    result = await app_inter('picture_type', 
                    fake_kwargs, 
                    renderer=fake_renderer(), 
                    app_dict=fake_app_dict)

    assert '成功' in result['content']
    assert result['return_type'] == 'str'