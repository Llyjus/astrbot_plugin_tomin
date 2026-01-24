from contextlib import contextmanager

import sqlite3

from app.data_management.config import DB_PATH


@contextmanager
def connection(path=DB_PATH):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    
    except Exception:
        conn.rollback()

        raise

    finally:
        conn.close()





