import os
import configparser
import interfaceTest.getpathInfo

# 读取当前路径
path = interfaceTest.getpathInfo.get_Path()
# join拼接改变当前路径
config_path = os.path.join(path, 'config_package/config.ini')
# 利用configparser模块读写配置文件的方法
config = configparser.ConfigParser()
# 以utf-8形式读取join拼接路径
config.read(config_path, encoding='utf-8')

class ReadConfig(object):

    def get_http(self, name):
        # 读取REPORT下变量name字段  注：name is str
        value = config.get('REPORT', name)
        return value

    def get_email(self, name):
        # 读取EMAIL下变量name字段  注：name is str
        value = config.get('LOGS', name)
        return value

    def get_mysql(self, name):
        # 读取DATABASE下变量name字段  注：name is str
        value = config.get('DATABASE', name)
        return value
# 实例化对象
ret = ReadConfig()