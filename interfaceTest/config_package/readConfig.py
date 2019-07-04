import os
import configparser
import interfaceTest.getpathInfo

path = interfaceTest.getpathInfo.get_Path()  # 调用实例化
config_path = os.path.join(path,
                           './config_package/config.ini')  # 这句话是在path路径下再加一级
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):  # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    ret = ReadConfig()

