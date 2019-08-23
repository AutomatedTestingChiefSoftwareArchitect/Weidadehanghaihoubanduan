import os
import unittest
import time
import HTMLTestRunnerCN
import interfaceTest.getpathInfo
from interfaceTest.log_and_logresult_package import Log

# import xmlrunner
# from HTMLTestRunner import HTMLTestRunner

logger = Log.logger


def report(perform_class, perform_num):
    suite = unittest.TestSuite()
    suite.addTests(map(perform_class, perform_num))
    logger.info("测试报告准备中~~~")
    logger.info("case执行开始 ~~~")
    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result\\report-' + date + '.html')
    if suite is not None:
        fp = open(config_path, 'wb')
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,
                                                   title=u'自动化测试报告',
                                                   # description='Test Description',
                                                   tester=u"邓颜灿")
        # runner = xmlrunner.XMLTestRunner(output=config_path)  # jenkins report
        runner.run(suite)
        fp.close()
        logger.info("测试报告已完成~~~")
    else:
        logger.error("没有可执行的Case~~~")
