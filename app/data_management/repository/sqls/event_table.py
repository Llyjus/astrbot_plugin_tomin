


    
EVENT_INSERT_SQL = '''
                INSERT INTO events(event_id, `timestamp`)
                VALUES(?, ?);

'''

EVENT_SEARCH_SQL = '''
                SELECT *
                FROM events
                WHERE event_id = ?;

'''

EVENT_DELETE_SQL = '''
                DELETE
                FROM events
                WHERE `timestamp` <= ?;
'''
