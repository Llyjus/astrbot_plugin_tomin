from typing import AsyncGenerator
from pydantic import ValidationError
from asyncio import get_running_loop

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger



from app import *

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class Tomin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """子线程"""
        try:
            loop = get_running_loop()
            await loop.run_in_executor(None, numpy_system_dependencies_check)
            await loop.run_in_executor(None, db_init)

        except Exception as e:
            self.terminate()
            raise RuntimeError('Tomin初始化失败。') from e

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    # @filter.command("helloworld")
    # async def helloworld(self, event: AstrMessageEvent):
    #     """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
    #     user_name = event.get_sender_name()
    #     message_str = event.message_str # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
    #     logger.info(message_chain)
    #     yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息



    @filter.command("招募", alias={'zm'})
    async def draw_card(self, event: AstrMessageEvent, fund_spent=10) ->AsyncGenerator[str, None]:
        """招募指令"""
        try:
            user_id = event.get_sender_id()

            user_id = str(user_id)
            result = ''

            #validate
            check = Gacha_input(user_id=user_id, fund_spent=fund_spent)


            # Gacha
            card = normal_gacha(user_id)

            result = "成功抽取卡牌:\n"
            for key, item in card.items():
                result += str(key) + ': ' + str(item) + '\n'
            
        except ValidationError as e:
            
            result = error_message(e)

        except Exception as e:
            result += str(e)

        yield event.plain_result(result)



    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        logger.info('girls_band_game插件已停用。')