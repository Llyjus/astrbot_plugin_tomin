
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