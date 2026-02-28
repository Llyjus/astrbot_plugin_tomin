from app.application.cards_app import *
from app.application.funds_app import *
from app.application.gacha_app import *
from app.application.working_app import *
from app.infrastuctures import template_generator, Renderer_html_to_png_bytes
from app.infrastuctures import get_avatar

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
    'card_working_status_app': card_working_status_app,
    'start_working_app': start_working_app,
    'card_working_status_app': card_working_status_app,
    'user_working_status_app': user_working_status_app,
    'stop_working_app': stop_working_app,
    'finish_working_app': finish_working_app,

}

#used for avatar url generation


async def app_inter(function_name, 
                    kwargs:dict, 
                    platform:str ,
                    avatar_path:str = None,
                    request_return_type:str = 'html',
                    *,
                    renderer:Renderer_html_to_png_bytes=None, 
                    message_id=None, 
                    connect=None, 
                    db_path=None,
                    app_dict=app_dict):
    
    func = app_dict.get(function_name, )
    if func is None:
        raise Invalid_input(f'函数名称错误：{function_name}')
    
    result = {'return_type': 'str',
              'content': '',
              'error': ''}
    
    try:
        event_creater(message_id=message_id, 
                  conn=connect, 
                  db_path = db_path)
    
        result = func(**kwargs, db_path=db_path, connect=connect)

        #result: {'return_type':'str/html', 
        #           'temp_type': none/str,
        #           'content': str/dict,
        #           'txt': none/str}
        if result:

            if result['return_type'] == 'str':
                result['error'] = ''
            
            elif result['return_type'] == 'html':
                if request_return_type == 'html':


                    try:

                        #add user avatar url from interface layer
                        if avatar_path:
                            avatar_result = await get_avatar(user_id=result['user_id'], 
                                                            avatar_loc=avatar_path,
                                                            platform=platform)

                            result['content']['avatar_path'] = avatar_result['avatar_loc']


                        #convert to image
                        html = template_generator(result['temp_type'], result['content'])

                        img = await renderer.render(html=html)

                        result = {'return_type': 'png', 
                                'content': img,
                                'error': avatar_result['error'] if avatar_path else ''}
                    except TimeoutError as e:
                        result = {'return_type': 'str', 
                                'content': '渲染图片失败，以下是文字内容：' + result.get('txt', ''),
                                'error': str(e),
                                'error_sign': None}

                elif request_return_type == 'str':
                    result = {'return_type': 'str', 
                                'content': result.get('txt', ''),
                                'error': '',
                                'error_sign': None}
        else:
            result = {'return_type': 'str', 
                                'content': "没有返回结果",
                                'error': "没有返回结果",
                                'error_sign': 1}
                        



        
    except App_error as e:
        result = {'return_type': 'str', 
                            'content': str(e),
                            'error': "",
                            'error_sign': 1}
        

    except Infra_error as e:
        result = {'return_type': 'str', 
                            'content': str(e),
                            'error': str(e),
                            'error_sign': 1}
        

    except Exception as e:
        result = {'return_type': 'str', 
                            'content': f'未知错误，请联系管理员处理{str(e)}',
                            'error': str(e),
                            'error_sign': 1}

    return result


