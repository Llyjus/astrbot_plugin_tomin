


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
    '打工'/'dg'
    '下班'/'xb'
    '工作状态'/'gzzt'/'gzt'
    '卡牌工作状态'/'kpgzzt'/'kgzt'
    本机器人支持不使用空格分隔指令和参数；
    输入‘帮助 [指令名称]’可查看对应指令的使用说明。例如：
        帮助 zm
    
"""



zm_text = """
        '招募' [资金] [次数] 或 'zm' [资金][x或空格][次数] ：
        进行招募，默认最低资金10，次数1。例如：   
        招募 表示默认花费10资金的一次招募，
        zm 20 3/zm20x3 表示每次花费20资金进行3次招募。

        目前角色拟定为6个等级，在无加成的情况下稀有度1-6抽取概率为：40%,30%,25%,5%,0%,0%

        `招募 x`（x为资金数量）最高可一次使用50资金招募，每增加5资金可提升固定比例的稀有度超过2的角色出现,
        五星角色会在25资金以上的招募出现，在40资金时达到最大概率不再增长；6星则是在40资金以上的招募出现。具体为：

        每5资金提升概率为：0%，12.5%，10%，7.5%，5%，5%            |        
        如若花费50资金进行一次招募，稀有度1-6的角色概率分别为：
        0%，0%，35%，40%，15%，10%

        `招募 x n`(n为次数)可在一次指令中进行多次抽取，最多10次。
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
稀有度1: 1资金，
稀有度2: 3资金，
稀有度3: 8资金，
稀有度4: 40资金，
稀有度5: 100资金，
稀有度6: 150资金。
例如“xcs 3”会出售所有稀有度1、2、3的卡牌。
'''


zj_text = '''
使用`资金`或`zj`来查询资金。

'''

zs_text = '''
输入`[zs/赠送][@xxx/qq号][卡牌id]`可以赠送卡牌。
如果是qq号中间需要用` `, `c`或`C`隔断。

'''

dg_text = '''
使用“打工 [卡牌id] [地点] [时长]”或“dg [卡牌id] [地点] [时长]”可以让卡牌开始打工。

地点关键词包括：
SPACE：space；
CiRCLE：circle；
RiNG：ring；
面包房：Yamabuki_Bakery、面包房、mbf、山吹面包房、山吹、ymbk；
宇田川家的拉面馆：wutagawa_laamen、wtgw、wutagawa、拉面、拉面馆、lm、lmg；
六花家的温泉旅馆：rokka_onsenryokan、温泉、温泉旅馆、wq、wqlg、rokka、六花、lock；
弦卷游乐园：Tsurumaki_amusement_park、弦卷、trmk、游乐园、yly、tsurumaki；
吉野家：Yoshinoya、吉野家、ysny、jyj；
STARRY：STARRY、starry。

使用示例：打工 123 面包房 3、dg123mbf3、dg 123 ymbk。

如果不填写时长，则默认工作时长为3小时，工作结束后需要手动结束工作。
工资基础为2资金一小时，最多允许3人同时工作。各成员按工作地点和稀有度获得工资加成。在连续工作超过3小时后，工资减半。稀有度为4、5、6的角色分别能获得1.5倍、2倍和3倍的工资加成。

具体工作地点加成如下：
SPACE中，popipa为1.5倍，其它bangdream乐队均为1.2倍；
CiRCLE中，所有bangdream乐队均为1.2倍；
RiNG中，mygo和ave mujica为1.5倍，其它所有bangdream乐队均为1.2倍；
山吹面包店中，popipa为1.5倍，其他bangdream乐队均为1.2倍；
宇田川家的拉面馆中，afterglow和roselia为1.5倍，其他bangdream乐队均为1.2倍；
六花家的温泉旅馆中，RAS为1.5倍，其他bangdream乐队均为1.2倍；
弦卷游乐园中，hello_happy_world为1.5倍，其他bangdream乐队均为1.2倍；
吉野家中，toge为1.5倍；
STARRY中，kessoku band为1.5倍。

'''

xb_text = '''
使用“下班”或“xb”指令，可以使工作结束的卡牌回归休息状态。
'''

gzzt_text = '''
使用“工作状态”或“gzzt”指令可以查看正在工作的卡牌和工作结束但未下班的卡牌。
'''

kpgzzt_text = '''使用“卡牌工作状态 卡牌id”或“kpgzzt 卡牌id”可以查看特定卡牌的工作状态。
''' 

help_dict = {'dk':dk_text, '打卡':dk_text, 'qd':dk_text, '签到':dk_text,
             'zm':zm_text, '招募':zm_text,
             '帮助':hp_text, 'help':hp_text,
             '查卡牌':ckp_text, 'ckp':ckp_text,
             '查卡牌集':ckpj_text, 'ckpj':ckpj_text,
             '出售':cs_text, 'cs':cs_text,
             '资金':zj_text, 'zj':zj_text,
             'zs':zs_text, '赠送': zs_text,
             '打工':dg_text, 'dg':dg_text,
             '下班':xb_text, 'xb':xb_text,
             '工作状态':gzzt_text, 'gzzt':gzzt_text, 'gzt':gzzt_text,
             '卡牌工作状态':kpgzzt_text, 'kpgzzt':kpgzzt_text, 'kgzt':kpgzzt_text}

help_simple_list = [hp_text, dk_text, 
                    zm_text, ckp_text, 
                    ckpj_text, cs_text, 
                    zj_text, zs_text, 
                    dg_text, xb_text, 
                    gzzt_text, kpgzzt_text]


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
            2:2,
            3:3,
            4:20,
            5:50,
            6:150
        }