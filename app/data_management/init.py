from pathlib import Path
import sqlite3
import os


from app.data_management.config import DB_PATH
from app.data_management.repository.repository import Repository

###
from astrbot.api import logger
##


def db_init(path=DB_PATH):

    db_path = Path(os.path.dirname(path)) / 'data.db'

    


    if not db_path.exists():



        db_path.parent.mkdir(parents=True, exist_ok=True)


        try:
            conn = sqlite3.connect(db_path)

            try:

                repo = Repository(conn)
                repo.create_table()
                conn.commit()
            finally:
                conn.close()
            
    
                
        except Exception as e:
            raise RuntimeError('数据库初始化失败') from e
        
    return db_path


def reset_slots(path=DB_PATH):

    db_path = Path(os.path.dirname(path)) / 'data.db'

    try:
        conn = sqlite3.connect(db_path)

        logger.error('已执行')            
        c = conn.cursor()
        c.execute('''
DROP TABLE IF EXISTS slots;
''')      
        c.execute('''
CREATE TABLE IF NOT EXISTS slots(
    user_id VARCHAR(50) NOT NULL,
    slot INTEGER NOT NULL,

    PRIMARY KEY (user_id, slot)
);
        
''')
        
        r = c.execute('''SELECT * FROM slots;''').fetchall()
        l = [i['slot'] for i in r]
        logger.error('{l}')

        conn.commit()
        conn.close()
    except Exception as e:
            conn.rollback()
            raise RuntimeError('数据库初始化失败') from e
