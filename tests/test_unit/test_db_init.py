from pathlib import Path

from app.data_management import db_init



def test_db_init():
    path = Path.cwd() / 'data.db'

    db_init(path)

    assert path.exists()
    



    path.unlink()
    