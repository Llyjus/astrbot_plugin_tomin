import os
from pathlib import Path
import sqlite3
import sys

from pytest import fixture

abs_location = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from app.data_management import Repository



@fixture
def e2e_database(tmp_path):

    db_path = tmp_path / 'data.db'
    conn = sqlite3.connect(db_path)
    repo = Repository(conn)
    repo.create_table()
    conn.close()

    return str(db_path)

    