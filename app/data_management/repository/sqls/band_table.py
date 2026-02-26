
# BAND_CREATE_SQL = '''
#             INSERT INTO bands (band_id, user_id)
#             VALUES (?, ?)
# '''

# BANDS_SEARCH_SQL = '''
#             SELECT *
#             FROM bands
#             WHERE user_id = ?;
#                        '''

# BAND_SEARCH_SQL = '''
#             SELECT *
#             FROM bands
#             WHERE user_id = ? AND band_id = ?;
#                        '''

# def band_add_card_sql(loc):
#     BAND_ADD_CARD_SQL = f'''
#             UPDATE bands
#             SET card{loc}_id = ?
#             WHERE user_id = ? AND band_id = ? 
# '''
    