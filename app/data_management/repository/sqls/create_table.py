USERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,  
    fund INTEGER NOT NULL CHECK (fund >= 0)                
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

EVENT_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS events(
    event_id TEXT PRIMARY KEY,
    `timestamp` INT 

);

'''


SIGN_IN_SQL = '''
CREATE TABLE IF NOT EXISTS sign_in(
    user_id VARCHAR(50) PRIMARY KEY,
    date INT,
    count INT,
    `timestamp` INT

);

'''

AVATAR_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS avatar(
    user_id VARCHAR(50) PRIMARY KEY,
    update_time int
);
'''


WORKING_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS work_place(
    card_uid INTEGER,
    space TEXT,
    end_time INT,
    reward_fund INT,

    PRIMARY KEY (card_uid),
    FOREIGN KEY (card_uid) REFERENCES cards(card_uid) ON DELETE CASCADE
);
'''




