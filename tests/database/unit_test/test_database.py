import sys
import os
from pytest import raises

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app.data_management.services.repository import Repository



def test_users_table(memory_db_connection):
    
    repo = memory_db_connection

    repo.add_user('test')
    result = repo.search_user('test')

    assert result['user_id'] == 'test' and result['fund'] == 10

    repo.add_fund('test', 20)

    repo.conn.commit()
    result = repo.search_user('test')

    assert result['fund'] == 30

    with raises(ValueError) as result:
        repo.add_fund('test', -100)

    assert '余额不足或用户不存在' in str(result.value)


    

    
    


    



    
   