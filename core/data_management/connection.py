from functools import wraps
from os import path, makedirs
import sqlite3


def db_connection(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
            if not path.exists('../../plugin_data/girls_band_game'):
                makedirs('../../plugin_data/girls_band_game')
            connection = sqlite3.connect('../../plugin_data/girls_band_game/data.db')
            connection.row_factory = sqlite3.Row
            
            try:

                result = func(connection, *args, **kwargs)
                connection.commit()
                return result
                
            except Exception as e:
                connection.rollback()
                raise e('操作失败。')
                
            finally:
                connection.close()

    return wrapper

    