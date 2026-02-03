from pathlib import Path
import sqlite3
import os


from app.data_management.config import DB_PATH
from app.data_management.repository.repository import Repository



def db_init(path=DB_PATH):

    db_path = Path(os.path.dirname(path)) / 'data.db'

    conn = sqlite3.connect(db_path)


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