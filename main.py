from typing import AsyncGenerator
from pydantic import ValidationError
from asyncio import get_running_loop

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger



from app import *

@register("Tomin - 少女乐队游戏", "Llyjus", "一个少女乐队游戏插件，实现抽卡、演出等功能。 ", "0.1.0")
class Tomin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.cleaner = Cleaner()

    async def initialize(self):
        """sub thread"""
        try:

            db_init()

            loop = get_running_loop()
            await loop.run_in_executor(None, numpy_system_dependencies_check)


        except Exception as e:
            self.terminate()
            raise RuntimeError('Tomin初始化失败。') from e



  

    @filter.command("招募", alias={'zm'})
    async def draw_card(self, event: AstrMessageEvent, fund_spent=10, times=1) ->AsyncGenerator[str, None]:
        """招募指令"""
        try:

            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            user_id = event.get_sender_id()

            user_id = str(user_id)
            result = ''

            # validate
            check = Gacha_input(user_id=user_id, fund_spent=fund_spent, times=times)



            # gacha
            cards = normal_gacha(user_id, fund_spent, times, message_id)



            result = "成功抽取卡牌:\n"


            result += cards


        except ValidationError as e:
            
            result = error_message(e)

        except App_error as e:
            result += str(e)
        except Infra_error as e:
            result += str(e)
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
