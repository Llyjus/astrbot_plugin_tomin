import re
from typing import AsyncGenerator
from unittest import result
from pydantic import ValidationError
from asyncio import get_running_loop

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register, StarTools
from astrbot.api import logger

import os, sys

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
if PLUGIN_DIR not in sys.path:
    sys.path.insert(0, PLUGIN_DIR)


from app import *



@register("Tomin - 少女乐队游戏", "Llyjus", "一个少女乐队游戏插件，实现抽卡、演出等功能。 ", "0.1.0")
class TominPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.cleaner = Cleaner()
        self.data_path = str(StarTools.get_data_dir() / 'data.db')

        # self.plugin_data_path = get_astrbot_data_path() / "plugin_data" / self.name


    async def initialize(self):


        try:

            db_init(self.data_path)


        except Exception as e:
            self.terminate()
            raise RuntimeError('Tomin初始化失败。') from e



    @filter.regex(r'^(帮助|help|hp|bz).*')
    async def help(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """帮助指令"""

        # yield event.plain_result(self.plugin_data_path)
        
        
        text = event.message_obj.message_str
        text = re.sub(r'^(help|帮助)\s*', '', text).strip()


        if text in help_dict:
            help = help_dict[text]

        else:
            help = help_dict['help']
        yield event.plain_result(help)






    @filter.regex(r'(招募|zm)\s*(\d+)?(?:\s*[xX ]\s*(\d+))?$')
    async def draw_card(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """招募指令"""

        message_text = event.message_obj.message_str

        if message_text.strip() == '招募' or message_text.strip() == 'zm':
            fund_spent = 10
            times = 1

        else:
            st = r'^(招募|zm)\s*(\d+)?(?:\s*[xX ]\s*(\d+))?$'
            message_text = re.match(st, message_text)
            if message_text:

                if message_text.group(2):
                    fund_spent = int(message_text.group(2))
                else: 
                    fund_spent = 10

                if message_text.group(3):
                    times = int(message_text.group(3))
                else: 
                    times = 1
                    

            else:
                yield event.plain_result('''命令格式错误。示例：
                                         zm 20 3/zm20x3 表示每次花费20资金进行3次招募。''')
                return

        try:

            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            user_id = event.get_sender_id()

            user_id = str(user_id)
            result = ''

            # validate
            _check = Gacha_input(user_id=user_id, fund_spent=fund_spent, times=times)



            # gacha
            cards = normal_gacha(user_id, fund_spent, times, message_id )



            result = "成功抽取卡牌:\n"


            result += cards


        except ValidationError as e:
            
            result = error_message(e)

        except App_error as e:
            result = str(e)
        except Infra_error as e:
            result = str(e)
            logger.error(f"Infra_error: {e}")

        yield event.plain_result(result)






    @filter.command("打卡", alias={'dk', '签到', 'qd'})
    async def sign_in(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """打卡指令"""
        try:

            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            user_id = event.get_sender_id()

            user_id = str(user_id)
            result = ''

            # validate
            _check = Gacha_input(user_id=user_id, fund_spent=10, times=1)



            # gacha
            cards = free_gacha(user_id, message_id=message_id)



            result = cards


        except ValidationError as e:
            
            result = error_message(e)

        except App_error as e:
            result += str(e)
        except Infra_error as e:
            result += str(e)
            logger.error(f"Infra_error: {e}")

        yield event.plain_result(result)





    @filter.regex(r'^(查卡牌|ckp)\s*([^\d\s]+)?\s*(\d+)?\s*$')
    async def search_card(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """查卡指令"""
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            message = event.message_obj.message_str
            user_id = event.get_sender_id()
            user_id = str(user_id)

            text = re.sub(r'^(查卡牌|ckp)\s*', '', message).strip()
            
            if text == '':
                result = search_cards_app(user_id=user_id)

            else:

                text = re.match(r'^([^\d\s]+)?\s*(\d+)?\s*$', text)

                band, rarity = text.group(1), text.group(2)

                if text:

                    if band:
                        
                        if rarity is not None:

                            inputs = Card_input(band=text.group(1), rarity=text.group(2))
                            band, rarity = inputs.band, inputs.rarity

                            result = search_cards_both_band_rarity(user_id, band, rarity)
                        
                        else:
                            inputs = Card_input(band=text.group(1))
                            band = inputs.band
                            result = search_cards_band_app(user_id, band)
                    
                    elif rarity:
                        
                        inputs = Card_input(rarity=text.group(2))
                        rarity = inputs.rarity
                        result = search_cards_rarity_app(user_id, rarity)
                
                else:
                    result = '参数错误！请查阅help获取帮助。'

        except ValidationError as e:
            result = error_message(e)
        except App_error as e:
            result = str(e)
        except Infra_error as e:
            result = str(e)
            logger.error(f"Infra_error: {e}")


        yield event.plain_result(result)





    @filter.regex(r'^(出售|cs).*')
    async def sell_card(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """出售指令"""
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id

            message = event.message_obj.message_str

            user_id = event.get_sender_id()

            user_id = str(user_id)

            card_id = re.sub(r'^(出售|cs)\s*', '', message).strip()

            _test = Card_input(card_id=card_id)

            result = sell_card_app(user_id, card_id=card_id, message_id=message_id)
        
        except ValidationError as e:
            result = error_message(e)
        except App_error as e:
            result = str(e)
        except Infra_error as e:
            result = str(e)
            logger.error(f"Infra_error: {e}")


        yield event.plain_result(result)
            
            
    @filter.regex(r'^(稀有度出售|xcs|x出售).*')
    async def sell_cards_rarity(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """出售指令"""
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            message = event.message_obj.message_str
            user_id = event.get_sender_id()

            user_id = str(user_id)

            rarity = re.sub(r'^(稀有度出售|x出售|xcs)\s*', '', message).strip()

            _test = Card_input(rarity=rarity)

            result = sell_cards_by_rarity_app(user_id, rarity=rarity, message_id=message_id)
        
        except ValidationError as e:
            result = error_message(e)
        except App_error as e:
            result = str(e)
        except Infra_error as e:
            result = str(e)
            logger.error(f"Infra_error: {e}")


        yield event.plain_result(result)
            





    @filter.permission_type(filter.PermissionType.ADMIN)
    @filter.regex(r'^(全服奖励|qfjl).*')
    async def gift(self, event: AstrMessageEvent):

        """全服奖励指令"""
        message_id = event.message_obj.message_id

        text = event.message_obj.message_str
        text = re.sub(r'^(全服奖励|qfjl)\s*', '', text).strip()
        
        
        
        try:
            text = int(text)

            _check = Funds_reward_input(fund_amount=text)

            result = funds_giving(text, message_id=message_id)

        except App_error as e:
            result = str(e)
        except Infra_error as e:
            result = str(e)
            logger.error(f"Infra_error: {e}")

        yield event.plain_result(result)
        



    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""

        logger.info('girls_band_game插件已停用。')











    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    # @filter.command("helloworld")
    # async def helloworld(self, event: AstrMessageEvent):
    #     """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
    #     user_name = event.get_sender_name()
    #     message_str = event.message_str # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
    #     logger.info(message_chain)
    #     yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息
