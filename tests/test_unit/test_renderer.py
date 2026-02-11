from pytest import mark, raises, fixture

from app.infrastuctures import template_generator
from app.schemas import Invalid_input
from app.infrastuctures import Renderer_html_to_png_bytes
# from tests.utils import playwright_browser

# @mark.asyncio
# async def test_renderer(playwright_browser):

#     html = template_generator('cards', 
#                               {'cards':[[1, 'card1', 'desc1'],],
#                                 'title':'卡牌信息',
#                                 'intro':'这是你查询到的卡牌信息：'})


#     img = await playwright_browser.render(html=html)

    # assert isinstance(img, bytes)


    # with raises(Invalid_input) as error1:
    #     html = template_generator('fake_temp', 
    #                             {'cards':[[1, 'card1', 'desc1'],],
    #                             'title':'卡牌信息',
    #                             'intro':'这是你查询到的卡牌信息：'})


        


@mark.asyncio
async def test_renderer():
    renderer = Renderer_html_to_png_bytes()
    await renderer.initial()
    html = template_generator('cards', 
                              {'cards':[[1, 'card1', 'desc1'],],
                                'title':'卡牌信息',
                                'intro':'这是你查询到的卡牌信息：'})


    img = await renderer.render(html=html)


    assert isinstance(img, bytes)

    await renderer.close()

    with raises(Invalid_input) as error1:
        html = template_generator('fake_temp', 
                                {'cards':[[1, 'card1', 'desc1'],],
                                'title':'卡牌信息',
                                'intro':'这是你查询到的卡牌信息：'})

