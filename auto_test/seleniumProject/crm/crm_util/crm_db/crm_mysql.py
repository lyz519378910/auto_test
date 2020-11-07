
import pymysql
import pymongo

class DbOperation:

    # so = SqlOperation('localhost', 'crm')
    def __init__(self,host_p = None,database_n = None,user_n = 'root',password_s = '123456',port_n = 3306):
        # 创建连接(管道)
        try:
            self.conn = pymysql.Connection(host=host_p, user=user_n, password=password_s,
                                      database=database_n, port=port_n, charset='utf8')
        except Exception as e:
            print(e,'connect failed!')

    # so.delete_data("delete from customer_info where customer_id = 50")
    def delete_data(self,sql_s):
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
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
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()              #提交数据
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
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            self.conn.commit()                  #提交数据
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
    def select_data(self,sql_s):
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            # 通过游标的fetchall方法，获取数据                 查找独有
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

    #一般用在添加时，用刚添加的元素对比数据库中值，有则添加成功
    # so.search_data("select * from customer_info where customer_id = 50 ",list_site,param)
    def operation_data(self,sql_s,list_site,param):
        try:
            # 创建游标(字典方式展示)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL
            self.cur.execute(sql_s)
            # 通过游标的fetchall方法，获取数据                 查找独有
            res = self.cur.fetchall()
            # 打印数据
            list(res)
            print(res[list_site][param])
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()
        return res

# if __name__ == '__main__':
#     do = DbOperation('localhost','crm')
#     # so.select_data("select * from customer_info where customer_id = 66 ")
#     do.delete_data("delete from customer_info where customer_id = 50")
#     # so.insert_data("insert into customer_info(customer_id) values(50)")
# #     so.update_data("update customer_info set customer_id = 66 where customer_id=50")
#

