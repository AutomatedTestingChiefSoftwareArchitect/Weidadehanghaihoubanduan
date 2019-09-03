import random
import pymysql
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.config_package import readConfig as rc

class DateBaseHandle(object):

    def __init__(self):
        self.conn = \
            pymysql.connect(host=rc.ret.get_mysql("host"),
            port=int(rc.ret.get_mysql("port")),
            user=rc.ret.get_mysql("user"),
            password=rc.ret.get_mysql("password"),
            db=rc.ret.get_mysql("db"),
            charset=rc.ret.get_mysql("charset"),
            connect_timeout=int(rc.ret.get_mysql("connect_timeout")))
        self.logger = Log.logger
        self.sid = []
        self.list = []
        self.name = []
        self.num = None
        self.key = None
        self.list_mysql_sid = []
        self.list_mysql_name = []

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
            self.list.append(self.num)
            self.list.append(self.key)
            return self.list
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
            self.conn.rollback()
            self.logger.info("···数据回滚成功···")
        finally:
            cursor.close()
# "select name,mobile FROM axd_user WHERE id=1541682410768827427"
results = DateBaseHandle()