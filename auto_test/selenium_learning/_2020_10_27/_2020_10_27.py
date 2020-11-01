
import pymysql

class SqlOperation:

    def __init__(self,host_p = None,database_n = None,user_n = 'root',password_s = '123456',port_n = 3306):
        # 创建连接(管道)
        self.conn = pymysql.Connection(host=host_p, user=user_n, password=password_s,
                                  database=database_n, port=port_n, charset='utf8')
        # 创建游标(字典方式展示)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # so.delete_data("delete from customer_info where customer_id = 50")
    def delete_data(self,sql_s):
        try:
            # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('delete success!')
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    # so.insert_data("insert into customer_info(customer_id) values(50)")
    def insert_data(self,sql_s):
        try:
            # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('insert success!')
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    # so.update_data("update customer_info set user_id = 5 where user_id = 7 ")
    def update_data(self,sql_s):
        try:
        # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('update success!')
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    # so.search_data("select * from customer_info where customer_id = 50 ")
    def search_data(self,sql_s):
        try:
            # 执行SQL
            self.cur.execute(sql_s)
            # 通过游标的fetchall方法，获取数据
            res = self.cur.fetchall()
            # 打印数据
            print(res)
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()
        return res

if __name__ == '__main__':
    so = SqlOperation('localhost','crm')
    so.search_data("select * from customer_info where customer_id = 50 ")



