import logging

from app.application.cards_app import *
from app.application.funds_app import *
from app.application.gacha_app import *
from app.infrastuctures import template_generator, render_html_to_png_bytes, Renderer_html_to_png_bytes


app_dict = {
    'normal_gacha': normal_gacha,
    'free_gacha': free_gacha,
    'funds_giving': funds_giving,
    'fund_checker': fund_checker,
    'search_card_app': search_card_app,
    'search_cards_app': search_cards_app,
    'search_cards_rarity_app': search_cards_rarity_app,
    'search_cards_band_app': search_cards_band_app,
    'search_cards_both_band_rarity': search_cards_both_band_rarity,
    'give_away_cards_app': give_away_cards_app,
    'sell_card_app': sell_card_app,
    'sell_cards_by_rarity_app': sell_cards_by_rarity_app,

}


async def app_inter(function_name, args:dict, renderer:Renderer_html_to_png_bytes=None, message_id=None, connect=None):

    event_creater(message_id=message_id, conn=connect)


    func = app_dict.get(function_name, )
    if func is None:
        raise Invalid_input(f'函数名称错误：{function_name}')
    

    try:
        result = func(**args)

        #result: {'return_type':'str/html', 
        #           'temp_type': none/str,
        #           'content': str/dict,
        #           'txt': none/str}
        if result:

            if result['return_type'] == 'str':
                pass
            
            elif result['return_type'] == 'html':



                try:
                    #convert to image
                    html = template_generator(result['temp_type'], result['content'])

                    img = await renderer.render(html=html)

                    result = {'return_type': 'png', 
                            'content': img}
                except TimeoutError:
                    result = {'return_type': 'str', 
                            'content': '生成图片超时,以下是文本内容：\n' + result.get('txt', '')}





        else:
            return
        
    except App_error as e:
        result = {'return_type': 'str', 
                            'content': str(e)}
        

    except Infra_error as e:
        result = {'return_type': 'str', 
                            'content': str(e)}
        
        logger = logging.getLogger(__name__)
        logger.error(f"Infra_error: {e}")


    except TimeoutError as e:
        result = {'return_type': 'str', 
                            'content': '生成图片超时，请重试'}
        

    except Exception as e:
        result = {'return_type': 'str', 
                            'content': f'未知错误，请联系管理员处理{e}'}
        
        logger = logging.getLogger(__name__)
        logger.error(f"Unknown error: {e}")

    return result

