import pytest
import sqlite3
import sys
import os

abs_location = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from app.data_management.services.repository import Repository




@pytest.fixture
def memory_db_connection():


    # establish an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row

    # initialize the database
    operater = Repository(conn)

    operater.create_table()

    yield operater
    
    conn.close()




