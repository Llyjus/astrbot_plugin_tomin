


SIGN_IN_INSERT_SQL = '''
        INSERT INTO sign_in (user_id, date, count, `timestamp`)
        VALUES (?, ?, 1, ?);

'''

SIGN_IN_SEARCH_SQL = '''
        SELECT *
        FROM sign_in
        WHERE user_id = ?;  
'''

SIGN_IN_DATE_UPDATE_SQL = '''
        UPDATE sign_in
        SET date = ?, count = 1, `timestamp` = ?
        WHERE user_id = ? AND date = ?;
'''

SIGN_IN_COUNT_UPDATE_SQL = '''
        UPDATE sign_in
        SET count = count + 1
            , `timestamp` = ?
        WHERE user_id = ? 
            AND count < 5
            AND ? - `timestamp` >= 3600*4;
''' 

