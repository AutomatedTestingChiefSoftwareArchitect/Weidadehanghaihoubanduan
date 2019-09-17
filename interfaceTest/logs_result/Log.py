import os
import logging
import interfaceTest.getpathInfo
from logging.handlers import TimedRotatingFileHandler

# 获取测试路径
path = interfaceTest.getpathInfo.get_Path()
# 存放log文件的路径
log_path = os.path.join(path, 'logs_result')

class Logger(object):

    def __init__(self, logger_name='logs…'):

        # 返回一个logger对象，如果没有指定名字将返回root logger
        self.logger = logging.getLogger(logger_name)
        # 指定最低的日志级别,，低于NOTSET的级别将被忽略
        logging.root.setLevel(logging.NOTSET)
        # 定义文件名
        self.log_file_name = 'logs'
        # 保留备份文件个数
        self.backup_count = 15
        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式 %(filename)s方法具体作用或查看log文件对应输出 可百度！！！
        self.formatter = logging.Formatter('%(filename)s - %(funcName)s - %(asctime)s - %(levelname)s '
                                           '- %(lineno)d - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            # 日志信息会输出到指定的stream中，如果stream为空则默认输出到sys.stderr
            # logging.StreamHandler(stream=None)
            # file_handler = logging.StreamHandler()

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='W0',
                                                    interval=0, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            # 同下 ！！！ file_handler is not console_handler
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
            """
            # 定义最终log信息的顺序, 结构和内容
            console_handler.setFormatter(self.formatter)
            # 定义日志输出级别
            console_handler.setLevel(self.console_output_level)
            # 将相应的console_handler 添加至logger对象中
            self.logger.addHandler(console_handler)
            """
        return self.logger

logger = Logger().get_logger()
