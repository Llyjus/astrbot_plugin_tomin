
import pytest


@pytest.fixture
def fake_application_fixture():

    def fake_normal_gacha(user_id, fund_spent, times, db_path, connect):
        return {'return_type': 'str',
                'content': '成功'}
    
    def picture_type(user_id, fund_spent, times, db_path, connect):
        return {'return_type':'html',
              'temp_type':'cards',
              'content':{'cards': [{"text":[f"角色：test",
                                            f"稀有度：test",
                                            f"id：test"
                                    ],
                                "picture_key":('test', 'test')}],
                         'title':'卡牌信息',
                         'intro':'这是你查询到的卡牌信息：'},
              'txt':'成功'}
    
    fake_app_dict = {
        'normal_gacha': fake_normal_gacha,
        'picture_type': picture_type,

    }



    fake_kwargs = {
        'user_id': 'test',
        'fund_spent': 10,
        'times': 1
    }
    return fake_app_dict, fake_kwargs