from app.data_management.repository.sql import *

from app.data_management.ports import function_ports

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
            except Exception as e:

                raise RuntimeError('创建table失败，数据库连接错误，请稍候再试') from e





    def add_user(self, user_id):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[0]

        try:
            cursor.execute(sql, (user_id, ))

        except sqlite3.IntegrityError as e:

            raise ValueError('用户已经存在') from e
        
        except Exception as e:

            raise RuntimeError('创建用户失败，数据库连接错误，请稍候再试') from e





    def search_user(self, user_id):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchone()
        except Exception as e:
            
            raise RuntimeError('查询失败，数据库连接错误，请稍候再试') from e
        
        return result

    def add_fund(self, user_id, fund):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[2]

        try:
            result = cursor.execute(sql, (fund, user_id, fund))
            
        except Exception as e:
            
            raise RuntimeError('查询失败，数据库连接错误，请稍候再试') from e
        
        if cursor.rowcount == 0:
                raise ValueError('余额不足')

        
    


    #card

    def add_cards(self, cards:list):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[0]

        try:
            cursor.executemany(sql, cards)
        
        except sqlite3.IntegrityError:

            raise ValueError('卡牌id已经存在')
        
        except Exception as e:
            
            raise RuntimeError('操作失败，数据库连接错误，请稍候再试') from e
        


    
    def search_card(self, card_id, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[1]

        try:
            result = cursor.execute(sql, (card_id, user_id)).fetchone()

        except Exception as e:
            raise RuntimeError('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
        
    def search_card_last(self, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[2]

        try:
            result = cursor.execute(sql,(user_id, )).fetchone()
        except Exception as e:
            raise RuntimeError('数据库连接错误，请稍候再试') from e
        
        return result
        
    def search_cards(self, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[3]

        try:
            result = cursor.execute(sql, (user_id, )).fetchall()

        except Exception as e:
            raise RuntimeError('查询失败，数据库连接错误，请稍候再试') from e
        
        return result
    
    def set_card_user(self, new_card_id, new_user_id, card_id, user_id):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[4]

        try:
            cursor.execute(sql, (new_card_id, new_user_id, card_id, user_id))

        except sqlite3.IntegrityError:

            raise ValueError('转让用户不存在！请先让该用户至少操作一次来创建帐号')
        

        except Exception as e:
            raise RuntimeError('操作失败，数据库连接错误，请稍候再试')
        
        if cursor.rowcount == 0:
            raise ValueError('用户没有该卡牌')
        
    def delete_cards(self, cards:list):
        cursor = self.conn.cursor()

        sql = card_interact_sql()[5]

        try:
            cursor.executemany(sql, cards)

        except Exception as e:
            raise RuntimeError('操作失败，数据库连接错误，请稍候再试') from e
    
    
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
            
        except Exception as e:
            
            raise RuntimeError('查询失败，数据库连接错误，请稍候再试') from e
        

        


    def search_slots(self, user_id):
        cursor = self.conn.cursor()

        sql = slot_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchall()
            
            return result
        
        except Exception as e:
            raise RuntimeError('操作失败，数据库连接错误，请稍候再试') from e


    def delete_slots(self, slots:list):
        cursor = self.conn.cursor()

        sql = slot_interact_sql()[2]




        try:
            cursor.executemany(sql, slots)
            
        except Exception as e:
            
            raise RuntimeError('查询失败，数据库连接错误，请稍候再试') from e
        
        
