def table_create_sql():
    return [USERS_TABLE_SQL, CARDS_TABLE_SQL, BANDS_TABLE_SQL]

def user_interact_sql():
    return [USER_INSERT_SQL, USER_CHECK_SQL, FUND_GIVEN_SQL]





USERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,  
    fund INTEGER DEFAULT 0                 
);
"""

CARDS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL, 
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

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE

);
"""

BANDS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS bands (
    band_id INTEGER,
    user_id VARCHAR(50) NOT NULL,
    card1_id INTEGER,
    card2_id INTEGER,
    card3_id INTEGER,
    card4_id INTEGER,
    card5_id INTEGER,

    PRIMARY KEY (band_id, user_id)

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (card1_id) REFERENCES cards(card_id) ON DELETE SET NULL,
    FOREIGN KEY (card2_id) REFERENCES cards(card_id) ON DELETE SET NULL,
    FOREIGN KEY (card3_id) REFERENCES cards(card_id) ON DELETE SET NULL,
    FOREIGN KEY (card4_id) REFERENCES cards(card_id) ON DELETE SET NULL,
    FOREIGN KEY (card5_id) REFERENCES cards(card_id) ON DELETE SET NULL
);
"""


USER_INSERT_SQL = '''
            INSERT INTO users(user_id, fund)
            VALUES(?, 10);
'''

USER_CHECK_SQL = '''
    SELECT * 
    FROM users
    WHERE user_id = ?;
'''

FUND_GIVEN_SQL = '''
    UPDATE users
    SET fund = fund + ?
    WHERE user_id = ? 
        AND fund + ? > 0;
'''