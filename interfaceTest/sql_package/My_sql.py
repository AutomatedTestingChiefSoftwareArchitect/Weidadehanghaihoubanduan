import random
import pymysql
from interfaceTest.logs_result import Log
from interfaceTest.config_package import readConfig as rc

class DateBaseHandle(object):

    def __init__(self):
        # 连接mysql, 及调用get_mysql方法获取参数变量
        self.conn = \
            pymysql.connect(host=rc.ret.get_mysql("host"),
            port=int(rc.ret.get_mysql("port")),
            user=rc.ret.get_mysql("user"),
            password=rc.ret.get_mysql("password"),
            db=rc.ret.get_mysql("db"),
            charset=rc.ret.get_mysql("charset"),
            connect_timeout=int(rc.ret.get_mysql("connect_timeout")))
        # 定义全局变量
        self.logger = Log.logger
        self.sid = []
        self.list = []
        self.name = []
        self.num = None
        self.key = None
        self.list_mysql_sid = []
        self.list_mysql_name = []

    def select_mysql(self, sql):
        # 返回游标对象
        cursor = self.conn.cursor()
        try:
            # 根据sql对数据库执行对应操作
            cursor.execute(sql)
            # fetchall：返回全部数据
            data = cursor.fetchall()
            # 根据random.choice 返回一个list的值,
            # 其中返回的值是mysql语句中的列
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
            # 捕捉date错误
            self.logger.error("select date error")
        finally:
            # finally：无论程序报错或者不报错,一定会执行的方法,
            # 关闭数据库连接
            cursor.close()

    def delete_mysql(self, sql):
        # 同上！！！
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            # 指数：除了select不需要commit,其他均需要！！！
            self.conn.commit()
        except:
            self.logger.info("···数据库删除数据错误，回滚中···")
            # 删除数据库中,如有报告直接回滚
            self.conn.rollback()
            self.logger.info("···数据回滚成功···")
        finally:
            # 同上！！！
            cursor.close()
# "select name,mobile FROM axd_user WHERE id=1541682410768827427"
results = DateBaseHandle()