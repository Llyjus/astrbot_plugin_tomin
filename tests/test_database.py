import sqlite3


# Test if we can create tables correctly
def test_table_creation(memory_db_connection):

    cursor = memory_db_connection.cursor()
    tables = cursor.execute("""
    SELECT name, type
    FROM sqlite_master
    WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
""").fetchall()



    table_names = [table['name'] for table in tables]
    expected_tables = ['users', 'cards', 'bands']

    for i in expected_tables:
        assert i in table_names, f'Wrong! Table {i} is not in the database. Tables are: {table_names}'




# Test if every column exists in tables
def test_table_columns(memory_db_connection):

    conn = memory_db_connection
    cursor = conn.cursor()
    
    table_names = ['users', 'cards', 'bands']
    result = []
    for i in range(3):


        result = cursor.execute(f"PRAGMA table_info({table_names[i]})").fetchall()
    
        columns = [col['name'] for col in result]


    correct_columns = [
    ['id', 'fund'],
    ['id', 'owner', 'character', 'o_band', 'pos', 'rarity', 'power', 'speed', 'resistance', 'skill_1', 'skill_2', 'skill_3'],
    ['id', 'user_id', 'card1_id', 'card2_id', 'card3_id', 'card4_id', 'card5_id']
]
    for c in correct_columns[i]:
            assert c in columns, f'''Column {c} doesn\' t exist in table!
                        All names in {table_names[i]} are: {correct_columns[i]}'''
            


    
   