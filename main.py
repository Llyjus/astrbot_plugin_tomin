import re
from pathlib import Path
from typing import AsyncGenerator
from unittest import result
from pydantic import ValidationError

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register, StarTools
from astrbot.api.message_components import At, Plain, Node, Plain, Image
from astrbot.api import logger

import os, sys

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
if PLUGIN_DIR not in sys.path:
    sys.path.insert(0, PLUGIN_DIR)


from app import *




@register("Tomin - 少女乐队游戏", "Llyjus", "一个少女乐队游戏插件，实现抽卡、演出等功能。 ", "0.2.3")
class TominPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.cleaner = Cleaner()
        self.data_path = str(StarTools.get_data_dir() / 'data.db')
        self.picture_path = StarTools.get_data_dir() / 'picture'
        self.avatar_path = StarTools.get_data_dir() / 'avatar'

        self.platform = str(os.getenv("PLATFORM", "qq"))

        max_renderer = int(os.getenv("RENDER_MAX_CONCURRENCY", "2"))
        timeout_s = float(os.getenv("RENDER_TIMEOUT_S", "15"))
        self.renderer = Renderer_html_to_png_bytes(sem=max_renderer, 
                                                   timeout_s=timeout_s)


    async def initialize(self):


        try:
            self.picture_path.mkdir(parents=True, exist_ok=True)
            self.avatar_path.mkdir(parents=True, exist_ok=True)
            db_init(self.data_path)

            await self.renderer.initial()
            logger.info('Tomin插件已初始化。')
            

            

        except Exception as e:
            self.terminate()
            raise RuntimeError('Tomin初始化失败。') from e



    @filter.regex(r'^(帮助|help|hp|bz).*')
    async def help(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """帮助指令"""

        # yield event.plain_result(self.plugin_data_path)
        
        
        text = event.message_obj.message_str
        text = re.sub(r'^(帮助|help|hp|bz)\s*', '', text).strip()


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
            result = await app_inter(
                                    "normal_gacha",
                                    {"user_id": user_id, "fund_spent": fund_spent, "times": times},
                                    renderer=self.renderer,
                                    message_id=message_id,
                                    db_path=self.data_path,
                                    avatar_path=self.avatar_path,
                                    platform=self.platform,
        )
            
            #check error before returning result
            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':

                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']

        except Invalid_input as e:
            result = str(e)

        except ValidationError as e:
            result = error_message(e)

        


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

            result = await app_inter(
            "free_gacha",     
            {"user_id": user_id},
            renderer=self.renderer,
            message_id=message_id,
            db_path=self.data_path,
            avatar_path=self.avatar_path,
            platform=self.platform,
            )


            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']


        except ValidationError as e:
            
            result = error_message(e)

        yield event.plain_result(result)


    @filter.regex(r'^(查卡牌|ckp)\s*(\d+)?\s*$')
    async def search_card(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """查卡指令"""
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            message = event.message_obj.message_str
            user_id = event.get_sender_id()
            user_id = str(user_id)

            text = re.match(r'^(查卡牌|ckp)\s*(\d+)\s*$', message)
            if text:
                if text.group(2):
                    card_id = int(text.group(2))
                    result = await app_inter('search_card_app', 
                                             {'user_id': user_id, 'card_id': card_id}, 
                                             renderer=self.renderer,
                                             message_id=message_id,
                                             db_path=self.data_path,
                                             avatar_path=self.avatar_path,
                                             platform=self.platform,
                    )
                

                        
                else:
                    result = {'return_type':'str',
                              'content': '输入格式错误！请查询helpckp来找到命令。',
                              'error': ''}
            else:
                result = {'return_type':'str',
                          'content': '请输入参数！若要查找全部卡牌请输入ckpj。',
                          'error': ''}
            
            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink()
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']



        except ValidationError as e:
            result = error_message(e)


        yield event.plain_result(result)




    @filter.regex(r'^(查卡牌集|ckpj)\s*([^\d\s]+)?\s*(\d+)?\s*$')
    async def search_cards(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """查卡指令"""
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            message = event.message_obj.message_str
            user_id = event.get_sender_id()
            user_id = str(user_id)

            text = re.sub(r'^(查卡牌集|ckpj)\s*', '', message).strip()
            
            if text == '':
                result = await app_inter(
                    "search_cards_app",
                    {"user_id": user_id},
                    renderer=self.renderer,
                    message_id=message_id,
                    db_path=self.data_path,
                    avatar_path=self.avatar_path,
                    platform=self.platform,
                )

            else:

                text = re.match(r'^([^\d\s]+)?\s*(\d+)?\s*$', text)

                band, rarity = text.group(1), text.group(2)

                if text:

                    if band:
                        
                        if rarity is not None:

                            inputs = Card_input(band=text.group(1), rarity=text.group(2))
                            band, rarity = inputs.band, inputs.rarity

                            result = await app_inter(
                                "search_cards_both_band_rarity",  
                                {"user_id": user_id, "band": band, "rarity": rarity},
                                renderer=self.renderer,
                                message_id=message_id,
                                db_path=self.data_path,
                                avatar_path=self.avatar_path,
                                platform=self.platform,
                            )


                        else:
                            inputs = Card_input(band=text.group(1))
                            band = inputs.band

                            result = await app_inter(
                            "search_cards_band_app",  
                            {"user_id": user_id, "band": band},
                            renderer=self.renderer,
                            message_id=message_id,
                            db_path=self.data_path,
                            avatar_path=self.avatar_path,
                            platform=self.platform,
                        )


                    elif rarity:
                        
                        inputs = Card_input(rarity=text.group(2))
                        rarity = inputs.rarity

                        result = await app_inter(
                            "search_cards_rarity_app", 
                            {"user_id": user_id, "rarity": rarity},
                            renderer=self.renderer,
                            message_id=message_id,
                            db_path=self.data_path,
                            avatar_path=self.avatar_path,
                            platform=self.platform,
                        )

                
                else:
                    result = {'return_type':'str',
                              'content': '输入格式错误！请查询helpckpj来找到命令。',
                              'error': ''}
                    
            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']


        except ValidationError as e:
            result = error_message(e)


        yield event.plain_result(result)




    @filter.command('资金', alias={'zj'})
    async def fund_check(self, event:AstrMessageEvent) ->AsyncGenerator[str, None]:
        '''查资金指令'''
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            message = event.message_obj.message_str

            user_id = event.get_sender_id()
            user_id = str(user_id)

            result = await app_inter(
                "fund_checker", 
                {"user_id": user_id},
                renderer=self.renderer,
                message_id=message_id,
                db_path=self.data_path,
                avatar_path=self.avatar_path,
                platform=self.platform,
            )

            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']
        
        except ValidationError as e:
            result = error_message(e)


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

            p = r'^(?:出售|cs)\s*(\d+)$'
            match = re.match(p, message.strip())
            if match:
                card_id = int(match.group(1))

                _test = Card_input(card_id=card_id)

                result = await app_inter(
                    "sell_card_app",
                    {"user_id": user_id, "card_id": card_id},
                    renderer=self.renderer,
                    message_id=message_id,
                    db_path=self.data_path,
                    avatar_path=self.avatar_path,
                    platform=self.platform,  
                )


            else:
                result = {'return_type':'str',
                          'content': '参数格式错误，请查阅hpcs。',
                          'error': ''}
                
            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']


        except ValidationError as e:
            result = error_message(e)

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

            match = re.match(r'^(稀有度出售|x出售|xcs)\s*(\d+)\s*', message)
            if match.group(2):

            
                rarity = int(match.group(2))
                _test = Card_input(rarity=rarity)


                result = await app_inter(
                    "sell_cards_by_rarity_app",
                    {"user_id": user_id, "rarity": rarity},
                    renderer=self.renderer,
                    message_id=message_id,
                    db_path=self.data_path,
                    avatar_path=self.avatar_path,
                    platform=self.platform,
                )


            else:
                result = {'return_type':'str',
                          'content': '参数格式错误，请查阅hpxcs。',
                          'error': ''}
                
            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']
            


        except ValidationError as e:
            result = error_message(e)


        yield event.plain_result(result)

    @filter.regex(r'^(赠送|zs).*$')
    async def give_card_away(self, event: AstrMessageEvent) ->AsyncGenerator[str, None]:
        """出售指令"""
        try:
            self.cleaner.cleaning_check()

            message_id = event.message_obj.message_id
            message = event.message_obj.message_str
            message_list = event.get_messages()
            giver_id = event.get_sender_id()
            giver_id = str(giver_id)


            
            match = re.match(r'^(赠送|zs)\s*(\d+)[ cC](\d+)\s*$', message)
            if match:
                
                accepter_id = match.group(2)
                card_id = int(match.group(3))

                result = await app_inter(
                    "give_away_cards_app",
                    {"giver_id": giver_id, "accepter_id": accepter_id, "card_id": card_id},
                    renderer=self.renderer,
                    message_id=message_id,
                    db_path=self.data_path,
                    avatar_path=self.avatar_path,
                    platform=self.platform,
                )


                
            elif isinstance(message_list[1], At) and isinstance(message_list[2], Plain):
                accepter_id = str(message_list[1].qq)
                match = re.search(r'^[ Cc]?(\d+)$', message_list[2].text)
                if match:
                    card_id = int(match.group(1))

                result = await app_inter(
                    "give_away_cards_app",
                    {"giver_id": giver_id, "accepter_id": accepter_id, "card_id": card_id},
                    renderer=self.renderer,
                    message_id=message_id,
                    db_path=self.data_path,
                    avatar_path=self.avatar_path,
                    platform=self.platform,
                )


            else:
                result = {'return_type':'str',
                            'content': '参数格式错误，请查阅hpzs。',
                            'error': ''}

            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']


        except ValidationError as e:
            result = error_message(e)

            
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

            result = await app_inter(
                "funds_giving",
                {"amount": text},
                renderer=self.renderer,
                message_id=message_id,
                db_path=self.data_path,
                platform=self.platform,
                avatar_path=self.avatar_path,
            )


            if result['error']:
                logger.error(result['error'])
            if result['return_type'] == 'png':
                try:
                    path = self.picture_path / f"{message_id}.png"
                    path.write_bytes(result['content'])
                    yield event.image_result(str(path))
                finally:
                    path.unlink(missing_ok=True)
                return
            
            else:
                if result['error']:
                    result = '渲染图片失败，以下是文字内容：' + result['content']
                else:
                    result = result['content']



        except Exception as e:
            result = str(e)
            logger.error(f"Unexpected error in sign_in: {e}")

        


        yield event.plain_result(result)

            


    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""


        await self.renderer.close()

        logger.info('Tomin插件已停用。')











    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    # @filter.command("helloworld")
    # async def helloworld(self, event: AstrMessageEvent):
    #     """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
    #     user_name = event.get_sender_name()
    #     message_str = event.message_str # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
    #     logger.info(message_chain)
    #     yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息



