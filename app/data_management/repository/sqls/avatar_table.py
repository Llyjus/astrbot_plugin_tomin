
AVATAR_INSERT_SQL = '''
        INSERT INTO avatar (user_id, update_time)
        VALUES (?, ?);
'''

AVATAR_SEARCH_SQL = '''
        SELECT *
        FROM avatar
        WHERE user_id = ?;
'''

AVATAR_UPDATE_SQL = '''
        UPDATE avatar
        SET update_time = ?
        WHERE user_id = ?;
'''



