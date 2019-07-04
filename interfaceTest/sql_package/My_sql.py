import pymysql
import interfaceTest.config_package.readConfig
from interfaceTest.log_and_logresult_package import Log


class Mysqldate:

    def __init__(self):
        self.host = interfaceTest.config_package.readConfig.ret.get_mysql('host')
        self.port = interfaceTest.config_package.readConfig.ret.get_mysql('port')
        self.db = interfaceTest.config_package.readConfig.ret.get_mysql('db')
        self.user = interfaceTest.config_package.readConfig.ret.get_mysql('user')
        self.password = interfaceTest.config_package.readConfig.ret.get_mysql('password')
        self.charset = 'utf-8'
        self.log = Log.logger

    def open_mysql(self):

        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db,
                                    user=self.user, password=self.password, charset=self.charset)
        self.cursor = self.conn.cursor()

    def select_mysql(self, key, value):
        self.open_mysql()
        date = "SELECT %s FROM %s;" % (key, value)
        reslut = self.cursor.execute(date)
        if reslut is None:
            self.log.error("login error")

    def delete_mysql(self, value, key,ids):
        self.open_mysql()
        dates = "DELETE FROM %s WHERE %s=%s;" % (value,key, ids)
        resluts = self.cursor.execute(dates)
        if resluts is None:
            self.log.error("login error")

    def close_mysql(self, method, value, key, ids):
        if method == "select":
            self.select_mysql(key, value)
        elif method == "delete":
            self.delete_mysql(value, key, ids)
        else:
            self.log.error("method error")
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    rets = Mysqldate()