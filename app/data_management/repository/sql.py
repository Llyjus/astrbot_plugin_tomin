def table_create_sql():
    return [USERS_TABLE_SQL, CARDS_TABLE_SQL, BANDS_TABLE_SQL, SLOTS_TABLE_SQL]

def user_interact_sql():
    return [USER_INSERT_SQL, USER_CHECK_SQL, FUND_GIVEN_SQL]

def card_interact_sql():
    return [CARD_INSERT_SQL, CARD_SEARCH_SQL, CARD_SEARCH_LAST_SQL, CARDS_SEARCH_SQL, CARD_SET_USER_SQL, CARD_DELETE_SQL]

def band_interact_sql():
    sql1 = [BAND_CREATE_SQL, BAND_SEARCH_SQL, BANDS_SEARCH_SQL]
    sql2 = [band_add_card_sql(x) for x in range(1, 6)]
    return sql1 + sql2

def slot_interact_sql():
    return [SLOT_INSERT_SQL, SLOTS_SELECT_SQL, SLOT_DELETE_SQL]




USERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,  
    fund INTEGER DEFAULT 0                 
);
            """

CARDS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS cards (
    card_uid INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL, 
    character VARCHAR(100) NOT NULL,
    o_band VARCHAR(100) NOT NULL,
    pos VARCHAR(50) NOT NULL,
    rarity INTEGER NOT NULL,
    power INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    resistance INTEGER NOT NULL,
    skill_1 TEXT,
    skill_2 TEXT,
    skill_3 TEXT,



    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    UNIQUE(user_id, card_id)
);
            """



BANDS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS bands (
    band_id INTEGER NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    card1_uid INTEGER,
    card2_uid INTEGER,
    card3_uid INTEGER,
    card4_uid INTEGER,
    card5_uid INTEGER,

    PRIMARY KEY (band_id, user_id),

    FOREIGN KEY (card1_uid) REFERENCES cards(card_uid) ON DELETE SET NULL,
    FOREIGN KEY (card2_uid) REFERENCES cards(card_uid) ON DELETE SET NULL,
    FOREIGN KEY (card3_uid) REFERENCES cards(card_uid) ON DELETE SET NULL,
    FOREIGN KEY (card4_uid) REFERENCES cards(card_uid) ON DELETE SET NULL,
    FOREIGN KEY (card5_uid) REFERENCES cards(card_uid) ON DELETE SET NULL
);
            """


SLOTS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS slots(
    user_id VARCHAR(50) NOT NULL,
    slot INTEGER NOT NULL,

    PRIMARY KEY (user_id, slot)
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
        AND fund + ? >= 0;
            '''

CARD_INSERT_SQL = """
            INSERT INTO cards (card_id, user_id, `character`, o_band, pos, rarity, power, speed, resistance, skill_1, skill_2, skill_3)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """

CARD_SEARCH_SQL = """
            SELECT *
            FROM cards
            WHERE card_id = ? AND user_id = ?;
            """

CARD_SEARCH_LAST_SQL = """
            SELECT *
            FROM cards
            WHERE user_id = ?
            ORDER BY card_id DESC
            LIMIT 1;
            """

CARDS_SEARCH_SQL = """
            SELECT *
            FROM cards
            WHERE user_id = ?;
        """

CARD_SET_USER_SQL = """
            UPDATE cards
            SET card_id = ?, user_id = ?
            WHERE card_id = ? AND user_id = ?;
        """

CARD_DELETE_SQL = '''
            DELETE 
            FROM cards
            WHERE user_id = ? AND card_id = ?

'''

BAND_CREATE_SQL = '''
            INSERT INTO bands ('band_id, user_id')
            VALUES (?, ?)
'''

BANDS_SEARCH_SQL = '''
            SELECT *
            FROM bands
            WHERE user_id = ?;
                       '''

BAND_SEARCH_SQL = '''
            SELECT *
            FROM bands
            WHERE user_id = ? AND band_id = ?;
                       '''

def band_add_card_sql(loc):
    BAND_ADD_CARD_SQL = f'''
            UPDATE bands
            SET card{loc}_id = ?
            WHERE user_id = ? AND band_id = ? 
'''
    
SLOT_INSERT_SQL = '''


        INSERT INTO slots (user_id, slot)
        VALUES (?, ?);

'''
    
SLOTS_SELECT_SQL = '''
                SELECT *
                FROM slots
                WHERE user_id = ?
                ORDER BY slot ASC;
'''

SLOT_DELETE_SQL = '''
                DELETE
                FROM slots
                WHERE user_id = ? AND slot = ?;
'''
    
