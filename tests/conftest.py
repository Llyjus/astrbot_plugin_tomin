# tests/conftest.py
import pytest
import sqlite3
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.data_management import table_create_sql

@pytest.fixture
def memory_db_connection():


    # establish an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row

    # initialize the database
    table_create_sql()

    cursor = conn.cursor()
    create_sql = table_create_sql()
    for sql in create_sql:
        cursor.execute(sql)

    yield conn
    
    conn.close()