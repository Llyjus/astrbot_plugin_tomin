from pathlib import Path

from app.data_management import db_init



def test_db_init(mocker):
    path = Path.cwd()

    path = db_init(path)


    path = path


    assert path.exists()
    
    


    path.unlink()
    