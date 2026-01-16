from functools import wraps

from core.data_management.connection import db_connection

USERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,  
    fund INTEGER DEFAULT 0                 
);
"""

CARDS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner INTEGER NOT NULL, 
    character VARCHAR(100) NOT NULL,
    o_band VARCHAR(100),
    pos VARCHAR(50),
    rarity INTEGER,
    power INTEGER,
    speed INTEGER,
    resistance INTEGER,
    skill_1 TEXT,
    skill_2 TEXT,
    skill_3 TEXT,

    FOREIGN KEY (owner) REFERENCES users(id) ON DELETE CASCADE

);
"""

BANDS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    card1_id INTEGER,
    card2_id INTEGER,
    card3_id INTEGER,
    card4_id INTEGER,
    card5_id INTEGER,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (card1_id) REFERENCES cards(id) ON DELETE SET NULL,
    FOREIGN KEY (card2_id) REFERENCES cards(id) ON DELETE SET NULL,
    FOREIGN KEY (card3_id) REFERENCES cards(id) ON DELETE SET NULL,
    FOREIGN KEY (card4_id) REFERENCES cards(id) ON DELETE SET NULL,
    FOREIGN KEY (card5_id) REFERENCES cards(id) ON DELETE SET NULL
);
"""

def table_create_sql():
    return [USERS_TABLE_SQL, CARDS_TABLE_SQL, BANDS_TABLE_SQL]



@db_connection
def initialization(connection):

        cursor = connection.cursor()

        sqls = table_create_sql()
        #reset tables
        for sql in sqls:
            cursor.execute(sql)
