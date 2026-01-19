from contextlib import contextmanager

import sqlite3



@contextmanager
def connection(path):
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





