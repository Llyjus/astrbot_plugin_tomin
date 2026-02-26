
USER_INSERT_SQL = '''
            INSERT INTO users(user_id, fund)
            VALUES(?, 10);
            '''

USER_CHECK_SQL = '''
    SELECT * 
    FROM users
    WHERE user_id = ?;
            '''

USERS_CHECK_ALL_SQL = '''
    SELECT *
    FROM users;
'''

FUND_GIVEN_SQL = '''
    UPDATE users
    SET fund = fund + ?
    WHERE user_id = ? 
        AND fund + ? >= 0;
            '''

FUND_GIVEN_ALL_USER_SQL = '''
    UPDATE users
    SET fund = fund + ?;
'''