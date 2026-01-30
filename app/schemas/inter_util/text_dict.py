


hp_text = """
Tomin指令列表：
    '帮助`/'help'/'hp'/'bz'
    '打卡'/'dk'
    '招募'/'zm'
    '查卡牌'/'ckp'
    '出售'/'cs'

    本机器人支持不使用空格分隔指令和参数；
    输入‘帮助 [指令名称]’可查看对应指令的使用说明。例如：
        帮助 zm
    
"""



zm_text = """
        '招募' [资金] [次数] 或 'zm' [资金][x或空格][次数] ：
        进行招募，默认最低资金10，次数1。例如：   
        招募 表示默认花费10资金的一次招募，
        zm 20 3/zm20x3 表示每次花费20资金进行3次招募。

        目前角色拟定为6个等级，在无加成的情况下稀有度1-6抽取概率为：
        29%，35%，19%，10%，6%，1%

        `招募 x`（x为资金数量）最高可一次使用50资金招募，每增加5资金可提升固定比例的稀有度超过2的角色出现,
        稀有度1-6具体为： 0%，3%，3%，2%，2%，1%
        如若花费50资金进行一次招募，稀有度1-6的角色概率分别为：
        0%，2%，37%，28%，24%，10%

        `招募 x n`(n为次数)可在一次指令中进行多次抽取。
"""

dk_text =  """
    '打卡'或'dk'/'qd'/'签到'来进行每日免费招募。
    冷却时间为4小时，每日最多5次，隔天重置冷却时间。
"""

ckp_text = '''
使用“查卡牌”或者“ckp”命令可以查看你拥有的所有卡牌。

如果想要筛选特定乐队或者特定稀有度的卡牌，
可以使用“查卡牌 乐队名称 稀有度”的格式来查找。
其中乐队名称和稀有度都可以不填写，也可以省略空格。
比如“查卡牌 roselia 4”或者“查卡牌4”都可以。

'''
cs_text = '''
出售卡牌有两种方式：

第一种是出售单张卡牌，
使用“出售 卡牌id”或者“cs 卡牌id”命令。
比如“出售 123”或者“cs 456”。

第二种是批量出售卡牌，
使用“稀有度出售”或者“x出售”或者“xcs 稀有度”命令，
可以出售指定稀有度以及比这个稀有度更低的所有卡牌。
不同稀有度卡牌的出售价格如下：
稀有度1: 3元，
稀有度2: 5元，
稀有度3: 15元，
稀有度4: 40元，
稀有度5: 80元，
稀有度6: 200元。
例如“xcs 3”会出售所有稀有度1、2、3的卡牌。
'''



help_dict = {'dk':dk_text, '打卡':dk_text, 'qd':dk_text, '签到':dk_text,
             'zm':zm_text, '招募':zm_text,
             '帮助':hp_text, 'help':hp_text,
             '查卡牌':ckp_text, 'ckp':ckp_text,
             '出售':cs_text, 'cs':cs_text}



band_dict = {'ppp':'popipa', 'popipa':'popipa',
              'ag':'afterglow', 'afterglow':'afterglow',
              '萝':'roselia', 'r':'roselia', 'roselia':'roselia',
              'pp':'pastel palettes','pastel palettes':'pastel palettes',
              
              'hhw':"hello happy world", '好好玩':"hello happy world",
            "hello happy world":"hello happy world",

            '蝶':"morfonica", 'morfonica':"morfonica",

            'RAS':'RAS', "ras":'RAS','拉丝':'RAS',
            'mygo':'mygo',

            'mjk':'ave mujica','母鸡卡':'ave mujica',
            'avemujica':'ave mujica','mujica':'ave mujica',

            'tgtg': 'toge', 'tg':'toge', '刺刺':'toge',
            'toge':'toge','togetoge':'toge','刺':'toge',


            '结束':'kessoku band', 
            "结束乐队":'kessoku band',
            'kessoku band':'kessoku band',


            
            }


