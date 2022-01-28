# -*- coding: utf-8 -*-
import pymysql
from dbutils.pooled_db import PooledDB
from tools.log import log


class MyDb(object):
    def __init__(self, host, port, user, password, database):
        # 初始化并搞了一个链接池 适用于高并发、网站 建立链接、游标
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=5,  # 连接池最大连接数，0和none表示不受限制
            mincached=1,  # 初始化时，至少创建的空闲连接，0表示不创建
            maxcached=3,  # 连接池最大空闲连接数，0和none表示不受限制
            blocking=True,  # 没有可用连接时，是否排队，true排队，false不排队直接报错
            ping=0,
            host=host, port=port, user=user, password=password,
            database=database
        )

        # self.conn = self.pool.connection()
        # self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # self.host = host
        # self.port = port
        # self.user = user
        # self.password = password
        # self.dbname = dbname

        # self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
        #                             database=self.dbname)
        # self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select(self, sql):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            log.error(e)
        self.result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return self.result

    def insert(self, sql):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            log.error(e)
        self.cursor.close()
        self.conn.close()

    def update(self, sql):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            log.error(e)
        self.cursor.close()
        self.conn.close()

    def delete(self, sql):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            log.error(e)
        self.cursor.close()
        self.conn.close()

    def select_real(self, sql):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            log.error(e)
        self.result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return self.result


# db1 正式库用于查询
db1 = MyDb(host="221.237.182.170", port=3326, user='epuser', password='epuser@123-TFblue',
           database='ep')
# db2 测试库用于插入，记录操作日志
db2 = MyDb(host="106.75.138.97", port=3306, user='epuser', password='epuser@123-New',
           database='ep')
# db3 测试库 testgroup 用于
db3 = MyDb(host="106.75.138.97", port=3306, user='epuser', password='epuser@123-New',
           database='testgroup')

if __name__ == '__main__':
    sql = "select * from user limit 0,1"
    db = MyDb(host="221.237.182.170", port=3326, user='epuser', password='epuser@123-TFblue',
              database='ep')
    a = db.select(sql)
    print(a)
