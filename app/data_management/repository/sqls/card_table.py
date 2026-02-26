


CARD_INSERT_SQL = """
            INSERT INTO cards (card_id, user_id, `character`, o_band, pos, rarity, power, speed, resistance, skill_1, skill_2, skill_3)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """

CARD_SEARCH_SQL = """
            SELECT *
            FROM cards
            WHERE card_id = ? AND user_id = ?;
            """

CARD_SEARCH_LAST_SQL = """
            SELECT *
            FROM cards
            WHERE user_id = ?
            ORDER BY card_id DESC
            LIMIT 1;
            """

CARDS_SEARCH_SQL = """
            SELECT *
            FROM cards
            WHERE user_id = ?;
        """

CARDS_SEARCH_BY_RARITY_SQL = """
            SELECT *
            FROM cards
            WHERE user_id = ? AND rarity = ?;
        """

CARDS_SEARCH_BY_BAND_SQL = """
            SELECT *
            FROM cards
            WHERE user_id = ? AND o_band = ?;
        """

CARDS_SEARCH_BY_BAND_RARITY_SQL = '''
            SELECT *
            FROM cards
            WHERE user_id = ? AND o_band = ? AND rarity = ?;

'''

CARD_SET_USER_SQL = """
            UPDATE cards
            SET card_id = ?, user_id = ?
            WHERE card_id = ? AND user_id = ?;
        """

CARDS_DELETE_SQL = '''
            DELETE 
            FROM cards
            WHERE card_id = ? AND user_id = ?;

'''