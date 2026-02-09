


hp_text = """
Tomin指令列表：
    '帮助`/'help'/'hp'/'bz'
    '打卡'/'dk'
    '招募'/'zm'
    '查卡牌'/'ckp'
    '查卡牌集'/'ckpj'
    '出售'/'cs'
    '资金'/'zj'
    '赠送'/'zs'
    本机器人支持不使用空格分隔指令和参数；
    输入‘帮助 [指令名称]’可查看对应指令的使用说明。例如：
        帮助 zm
    
"""



zm_text = """
        '招募' [资金] [次数] 或 'zm' [资金][x或空格][次数] ：
        进行招募，默认最低资金10，次数1。例如：   
        招募 表示默认花费10资金的一次招募，
        zm 20 3/zm20x3 表示每次花费20资金进行3次招募。

<<<<<<< HEAD
        目前角色拟定为6个等级，在无加成的情况下稀有度1-6抽取概率为：40%,30%,25%,5%,0%,0%

        `招募 x`（x为资金数量）最高可一次使用50资金招募，每增加5资金可提升固定比例的稀有度超过2的角色出现,
        五星角色会在25资金以上的招募出现，在40资金时达到最大概率不再增长；6星则是在40资金以上的招募出现。具体为：

        每5资金提升概率为：0%，12.5%，10%，7.5%，5%，5%            |        
        如若花费50资金进行一次招募，稀有度1-6的角色概率分别为：
        0%，0%，35%，40%，15%，10%

        `招募 x n`(n为次数)可在一次指令中进行多次抽取，最多10次。
=======
        目前角色拟定为6个等级，在无加成的情况下稀有度1-6抽取概率为：
        29%，35%，19%，10%，6%，1%

        `招募 x`（x为资金数量）最高可一次使用50资金招募，每增加5资金可提升固定比例的稀有度超过2的角色出现,
        稀有度1-6具体为： 0%，3%，3%，2%，2%，1%
        如若花费50资金进行一次招募，稀有度1-6的角色概率分别为：
        0%，5%，34%，26%，22%，9%

        `招募 x n`(n为次数)可在一次指令中进行多次抽取。
>>>>>>> origin/develop
"""

dk_text =  """
    '打卡'或'dk'/'qd'/'签到'来进行每日免费招募。
    冷却时间为4小时，每日最多5次，隔天重置冷却时间。
"""

ckp_text = '''
使用“查卡牌[id]”或者“ckp[id]”命令可以查看你特定id的卡牌。
如果想要筛选特定类型卡牌集或查询全部卡牌，
输入helpckpj查询指令。
'''


ckpj_text = '''
使用“查卡牌集”或者“ckpj”命令可以查看你拥有的所有卡牌。

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
<<<<<<< HEAD
稀有度1: 1资金，
稀有度2: 3资金，
稀有度3: 8资金，
稀有度4: 40资金，
稀有度5: 100资金，
稀有度6: 150资金。
=======
稀有度1: 1元，
稀有度2: 3元，
稀有度3: 10元，
稀有度4: 30元，
稀有度5: 50元，
稀有度6: 100元。
>>>>>>> origin/develop
例如“xcs 3”会出售所有稀有度1、2、3的卡牌。
'''


zj_text = '''
使用`资金`或`zj`来查询资金。

'''

zs_text = '''
输入`[zs/赠送][@xxx/qq号][卡牌id]`可以赠送卡牌。
如果是qq号中间需要用` `, `c`或`C`隔断。

'''

help_dict = {'dk':dk_text, '打卡':dk_text, 'qd':dk_text, '签到':dk_text,
             'zm':zm_text, '招募':zm_text,
             '帮助':hp_text, 'help':hp_text,
             '查卡牌':ckp_text, 'ckp':ckp_text,
             '查卡牌集':ckpj_text, 'ckpj':ckpj_text,
             '出售':cs_text, 'cs':cs_text,
             '资金':zj_text, 'zj':zj_text,
             'zs':zs_text, '赠送': zs_text}



band_dict = {'ppp':'popipa', 'popipa':'popipa',
              'ag':'afterglow', 'afterglow':'afterglow',
              '萝':'roselia', 'r':'roselia', 'roselia':'roselia',
              'pp':'pastel palettes','pastel_palettes':'pastel palettes',
              
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


fund_map = {
            1:1,
<<<<<<< HEAD
            2:2,
            3:3,
            4:20,
            5:50,
            6:150
=======
            2:3,
            3:10,
            4:30,
            5:50,
            6:100
>>>>>>> origin/develop
        }