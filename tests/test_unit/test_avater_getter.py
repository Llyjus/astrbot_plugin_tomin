import base64
from pathlib import Path

from pytest import raises

from app.infrastuctures import get_avatar, avatar_dict
from app.schemas import Invalid_input

async def test_avatar_getter(monkeypatch, tmp_path):


    FAKE_PNG_B64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+X2ZQAAAAASUVORK5CYII="
    FAKE_PNG_BYTES = base64.b64decode(FAKE_PNG_B64)

    class Fake_repo():
        def __init__(self, conn):
            pass

    class Fake_avatar_service():
        def __init__(self, repo):
            self.repo = repo

        def check_avatar(self, user_id):
            if user_id == 'test':
                return True
            else:
                return False

        def update_avatar_record(self, user_id, status):
            return True
        
    class Fake_connection():
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            pass
        
    async def fake_qq_avatar_fetcher(user_id):
        return FAKE_PNG_BYTES
            
    
    monkeypatch.setitem(avatar_dict, 'qq', fake_qq_avatar_fetcher)
    
    result1 = await get_avatar(user_id='test',
                              avatar_loc='test_avatar_loc',
                              platform='qq',
                              connect=Fake_connection(),
                              avatar_ser=Fake_avatar_service,
                              repository=Fake_repo)
    
    

    assert result1['error'] is None
    assert result1['avatar_loc'] == 'test_avatar_loc/test.jpg'




    result2 = await get_avatar(user_id='testx',
                              avatar_loc=str(tmp_path / "test_avatar_loc"),
                              platform='qq',
                              connect=Fake_connection(),
                              avatar_ser=Fake_avatar_service,
                              repository=Fake_repo) 
    
    assert result2['error'] == None
    assert 'testx.jpg' in result2['avatar_loc']



    result3 = await get_avatar(user_id='testt',
                         avatar_loc=str(tmp_path / "test_avatar_loc"),
                         platform='fake_platform',
                         connect=Fake_connection(),
                         avatar_ser=Fake_avatar_service,
                         repository=Fake_repo)
        
    assert '平台错误' in result3['error']