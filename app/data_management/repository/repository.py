from app.data_management.repository.sql import *

from app.data_management.ports import function_ports

from app.schemas.errors import *

import sqlite3


class Repository(function_ports):

    def __init__(self, conn):
        self.conn = conn




    def create_table(self):



        cursor = self.conn.cursor()

        sqls = table_create_sql()

        #reset tables未能成功查询
        for sql in sqls:
            try:
                cursor.execute(sql)
            except sqlite3.Error as e:

                raise Database_error('创建table失败，数据库连接错误，请稍候再试') from e





    def add_user(self, user_id):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[0]

        try:
            cursor.execute(sql, (user_id, ))

        except sqlite3.IntegrityError as e:

            raise User_already_exists('用户已经存在') from e
        
        except sqlite3.Error as e:

            raise Database_error('创建用户失败，数据库连接错误，请稍候再试') from e




    def search_user(self, user_id):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchone()
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
    
    
    def search_all_user(self):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[2]

        try:
            result = cursor.execute(sql).fetchall()
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result

    def add_fund(self, user_id, fund):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[3]

        try:
            result = cursor.execute(sql, (fund, user_id, fund))
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        if cursor.rowcount == 0:
                raise Not_enough_fund('余额不足')


    def all_user_add_fund(self, fund):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[4]

        try:
            result = cursor.execute(sql, (fund, ))
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e

    


    #card

    def add_cards(self, cards:list):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[0]

        try:
            cursor.executemany(sql, cards)
        
        except sqlite3.IntegrityError:

            raise Card_already_exists('卡牌id已经存在')
        
        except sqlite3.Error as e:
            
            raise Database_error('操作失败，数据库连接错误，请稍候再试') from e
        


    
    def search_card(self, card_id, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[1]

        try:
            result = cursor.execute(sql, (card_id, user_id)).fetchone()

        except sqlite3.Error as e:
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
        
    def search_card_last(self, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[2]

        try:
            result = cursor.execute(sql,(user_id, )).fetchone()
        except sqlite3.Error as e:
            raise Database_error('数据库连接错误，请稍候再试') from e
        
        return result
        
    def search_cards(self, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[3]

        try:
            result = cursor.execute(sql, (user_id, )).fetchall()

        except sqlite3.Error as e:
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
    
    
    def search_cards_by_rarity(self, user_id, rarity):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[4]

        try:
            result = cursor.execute(sql, (user_id, rarity)).fetchall()

        except sqlite3.Error as e:
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
    
    def search_cards_by_band(self, user_id, o_band):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[5]

        try:
            result = cursor.execute(sql, (user_id, o_band)).fetchall()

        except sqlite3.Error as e:
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
    

    def search_cards_by_band_rariry(self, user_id, o_band, rarity):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[6]

        try:
            result = cursor.execute(sql, (user_id, o_band, rarity)).fetchall()

        except sqlite3.Error as e:
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        return result


    
    def set_card_user(self, new_card_id, new_user_id, card_id, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[7]

        try:
            cursor.execute(sql, (new_card_id, new_user_id, card_id, user_id))

        except sqlite3.IntegrityError:

            raise User_not_found('转让用户不存在！请先让该用户至少操作一次来创建帐号')
        

        except sqlite3.Error as e:
            raise Database_error('操作失败，数据库连接错误，请稍候再试')
        if cursor.rowcount == 0:
            raise Card_not_found('用户没有该卡牌')
        
    def delete_cards(self, cards:list):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[8]

        try:
            cursor.executemany(sql, cards)

        except sqlite3.Error as e:
            raise Database_error('操作失败，数据库连接错误，请稍候再试') from e
    
    
    # #band



        
    # def create_band(self, band_id, user_id):
    #     cursor = self.conn.cursor()

    #     sql = band_interact_sql[0]

    #     try:
    #         cursor = cursor.execute(sql, (band_id, user_id))

    #     except 

    #     if cursor.rowcount == 0:


    def add_slots(self, slots:list):
        cursor = self.conn.cursor()

        sql = slot_interact_sql()[0]

        try:
            cursor.executemany(sql, slots)
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        

        


    def search_slots(self, user_id):
        cursor = self.conn.cursor()

        sql = slot_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchall()
            
            return result
        
        except Exception as e:
            raise Database_error('操作失败，数据库连接错误，请稍候再试') from e


    def delete_slots(self, slots:list):
        cursor = self.conn.cursor()

        sql = slot_interact_sql()[2]




        try:
            cursor.executemany(sql, slots)
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        


    def add_event(self, event_id, timestamp):
        cursor = self.conn.cursor()

        sql = event_interact_sql()[0]

        try:
            cursor.execute(sql, (event_id, timestamp))

        except sqlite3.IntegrityError as e:
            raise Request_repeat('重复执行')  
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        
        
        


    def search_event(self, event_id):
        cursor = self.conn.cursor()

        sql = event_interact_sql()[1]

        try:
            result = cursor.execute(sql, (event_id, )).fetchone()
            
            return result
        
        except sqlite3.Error as e:
            raise Database_error(f'操作失败，数据库连接错误，请稍候再试:{e}') from e



    def delete_events(self, timestamp):
        cursor = self.conn.cursor()

        sql = event_interact_sql()[2]

        
        try:
            cursor.execute(sql, (timestamp, ))
            
        except sqlite3.Error as e:  
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e


    def add_sign_in(self, user_id, date, timestamp):
        cursor = self.conn.cursor()

        sql = sign_in_interact_sql()[0]

        try:
            cursor.execute(sql, (user_id, date, timestamp))

        except sqlite3.IntegrityError as e:
            raise Request_repeat('重复执行')  
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        

    def search_sign_in(self, user_id):
        cursor = self.conn.cursor()

        sql = sign_in_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchone()
            
            return result
        
        
        except sqlite3.Error as e:
            raise Database_error(f'操作失败，数据库连接错误，请稍候再试:{e}') from e


    def update_sign_in_date(self, user_id, date, past_date, timestamp):
        
        cursor = self.conn.cursor()

        sql = sign_in_interact_sql()[2]

        try:
            cursor.execute(sql, (date, timestamp, user_id, past_date))
            
        except sqlite3.Error as e:
            raise Database_error(f'操作失败，数据库连接错误，请稍候再试:{e}') from e


        if cursor.rowcount == 0:
            raise Cooldown('正在冷却中，请勿重复操作！')

    def update_sign_in_count(self, user_id, timestamp):
        cursor = self.conn.cursor()

        sql = sign_in_interact_sql()[3]

        try:
            cursor.execute(sql, (timestamp, user_id, timestamp))
            
        except sqlite3.Error as e:
            raise Database_error(f'操作失败，数据库连接错误，请稍候再试:{e}') from e

        if cursor.rowcount == 0:
            raise Cooldown('正在冷却中，请勿重复操作！')






# avatar



    def add_avatar(self, user_id, timestamp):
        cursor = self.conn.cursor()

        sql = avatar_interact_sql()[0]

        try:
            cursor.execute(sql, (user_id, timestamp))

        except sqlite3.IntegrityError as e:
            raise Request_repeat('重复执行')  
            
        except sqlite3.Error as e:
            
            raise Database_error('查询失败，数据库连接错误，请稍候再试') from e
        

    def search_avatar(self, user_id):
        cursor = self.conn.cursor()

        sql = avatar_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchone()
            
            return result
        
        except sqlite3.Error as e:
            raise Database_error(f'操作失败，数据库连接错误，请稍候再试:{e}') from e
        


    def update_avatar(self, user_id, timestamp):
        cursor = self.conn.cursor()

        sql = avatar_interact_sql()[2]

        try:
            cursor.execute(sql, (timestamp, user_id))
            
        except sqlite3.Error as e:
            raise Database_error(f'操作失败，数据库连接错误，请稍候再试:{e}') from e