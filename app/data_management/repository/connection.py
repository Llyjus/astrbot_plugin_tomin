from contextlib import contextmanager

from pathlib import Path
import sqlite3

from app.data_management.config import DB_PATH


@contextmanager
def connection(path=None):
    if path is None:
        path = DB_PATH
        
    db_path = Path(path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(path, timeout=10)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    
    except Exception:
        conn.rollback()

        raise

    finally:
        conn.close()





