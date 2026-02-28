from app.data_management.repository.sqls.user_table import *
from app.data_management.repository.sqls.card_table import *
from app.data_management.repository.sqls.band_table import *
from app.data_management.repository.sqls.slot_table import *
from app.data_management.repository.sqls.event_table import *
from app.data_management.repository.sqls.sign_in_table import *
from app.data_management.repository.sqls.avatar_table import *
from app.data_management.repository.sqls.create_table import *
from app.data_management.repository.sqls.working_table import * 



def table_create_sql():
    return [USERS_TABLE_SQL, 
            CARDS_TABLE_SQL, 
            BANDS_TABLE_SQL, 
            SLOTS_TABLE_SQL, 
            EVENT_TABLE_SQL, 
            SIGN_IN_SQL, 
            AVATAR_TABLE_SQL, 
            WORKING_TABLE_SQL]

def user_interact_sql():
    return [USER_INSERT_SQL, USER_CHECK_SQL, USERS_CHECK_ALL_SQL, FUND_GIVEN_SQL, FUND_GIVEN_ALL_USER_SQL]

def card_interact_sql():
    return [CARD_INSERT_SQL, CARD_SEARCH_SQL, 
            CARD_SEARCH_LAST_SQL, CARDS_SEARCH_SQL, 
            CARDS_SEARCH_BY_RARITY_SQL, CARDS_SEARCH_BY_BAND_SQL, 
            CARDS_SEARCH_BY_BAND_RARITY_SQL, 
            CARD_SET_USER_SQL, CARDS_DELETE_SQL]

# def band_interact_sql():
#     sql1 = [BAND_CREATE_SQL, BAND_SEARCH_SQL, BANDS_SEARCH_SQL]
#     sql2 = [band_add_card_sql(x) for x in range(1, 6)]
#     return sql1 + sql2

def slot_interact_sql():
    return [SLOT_INSERT_SQL, SLOTS_SELECT_SQL, SLOT_DELETE_SQL]

def event_interact_sql():
    return [EVENT_INSERT_SQL, EVENT_SEARCH_SQL, EVENT_DELETE_SQL]

def sign_in_interact_sql():
    return [SIGN_IN_INSERT_SQL, SIGN_IN_SEARCH_SQL, SIGN_IN_DATE_UPDATE_SQL, SIGN_IN_COUNT_UPDATE_SQL]

def avatar_interact_sql():
    return [AVATAR_INSERT_SQL, AVATAR_SEARCH_SQL, AVATAR_UPDATE_SQL]

def working_interact_sql():
    return [WORKING_INSERT_SQL, 
            WORKING_SEARCH_BY_USER_SQL, 
            WORKING_SEARCH_BY_CARD_SQL, 
            WORKING_SPACE_SEARCH_SQL, 
            WORKING_DELETE_SQL,
            WORKING_UPDATE_SQL]





