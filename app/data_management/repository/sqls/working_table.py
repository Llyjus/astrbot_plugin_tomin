

WORKING_INSERT_SQL = '''
        INSERT INTO work_place (card_uid, space, end_time, reward_fund)
        VALUES (?, ?, ?, ?);    
'''

WORKING_SEARCH_BY_USER_SQL = '''
        SELECT *
        FROM work_place AS wp
        LEFT JOIN cards AS c ON wp.card_uid = c.card_uid
        WHERE c.user_id = ?;
'''

WORKING_SEARCH_BY_CARD_SQL = '''
        SELECT *
        FROM work_place as wp
        LEFT JOIN cards AS c ON wp.card_uid = c.card_uid
        WHERE c.user_id = ? AND c.card_id = ?;
'''

WORKING_SPACE_SEARCH_SQL = '''
        SELECT count(*) AS worker, space
        FROM work_place
        GROUP BY space;
'''
        

WORKING_DELETE_SQL = '''
        DELETE
        FROM work_place
        WHERE card_uid = ?;
'''