import pymysql
from interfaceTest.log_and_logresult_package import Log
import random


class DateBaseHandle(object):

    def __init__(self):

        self.conn = pymysql.connect(
            host='rm-wz91670r7o0zi042j8o.mysql.rds.aliyuncs.com',
            port=3306,
            user='test_shanghai',
            password='shanghai@jinglong',
            db='axd_test',
            charset='utf8'
        )
        self.logger = Log.logger
        self.sid = []
        self.name = []
        self.list_mysql_sid = []
        self.list_mysql_name = []
        self.num = None
        self.key = None

    def select_mysql(self, sql):

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for rows, table in data:
                self.sid.append(rows)
                self.name.append(table)
                self.list_mysql_sid.append(self.sid)
                self.list_mysql_name.append(self.name)
            for topic in self.list_mysql_sid:
                self.num = random.choice(topic)
            for topics in self.list_mysql_name:
                self.key = random.choice(topics)
            return self.num, self.key
        except:
            self.logger.error("select date error")
        finally:
            cursor.close()

    def delete_mysql(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.logger.info("···数据库删除数据错误，回滚中···")
            self.conn.rollback()  # 错误时回滚
            self.logger.info("···数据回滚成功···")
        finally:
            cursor.close()


results = DateBaseHandle()
