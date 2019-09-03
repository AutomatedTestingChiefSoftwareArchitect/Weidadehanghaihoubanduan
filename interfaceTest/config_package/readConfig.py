import os
import configparser
import interfaceTest.getpathInfo

path = interfaceTest.getpathInfo.get_Path()
config_path = os.path.join(path, 'config_package/config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

class ReadConfig(object):

    def get_http(self, name):
        value = config.get('REPORT', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value

ret = ReadConfig()