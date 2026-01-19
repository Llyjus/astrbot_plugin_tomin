from app.data_management.services.sql import table_create_sql, user_interact_sql

from app.data_management.ports import function_ports


class Repository:

    def __init__(self, conn):
        self.conn = conn




    def create_table(self):

        cursor = self.conn.cursor()

        sqls = table_create_sql()

        #reset tables
        for sql in sqls:
            try:
                cursor.execute(sql)
            except Exception as e:

                self.conn.rollback()
                raise RuntimeError('创建table失败，数据库连接错误，请稍候再试') from e





    def add_user(self, user_id):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[0]

        try:
            cursor.execute(sql, (user_id, ))
        
        except Exception as e:
            raise RuntimeError('创建用户失败，数据库连接错误，请稍候再试')
        

    def search_user(self, user_id):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[1]

        try:
            result = cursor.execute(sql, (user_id, )).fetchone()
        except Exception as e:
            
            raise RuntimeError('未能成功查询，数据库连接错误，请稍候再试') from e
        
        else:
            
            return result

    def add_fund(self, user_id, fund):

        cursor = self.conn.cursor()

        sql = user_interact_sql()[2]

        try:
            result = cursor.execute(sql, (fund, user_id, fund))
            
        except Exception as e:
            
            raise RuntimeError('未能成功查询，数据库连接错误，请稍候再试') from e
        
        if cursor.rowcount == 0:
                raise ValueError('余额不足或用户不存在')
        else:
            
            return result