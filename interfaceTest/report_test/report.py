import os
import time
import platform
import unittest
import interfaceTest.getpathInfo
from interfaceTest.config_package import readConfig
from interfaceTest.robot_package import robot_report
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.report_test.report_tools import HTMLTestRunnerCN

# import xmlrunner
# from HTMLTestRunner import HTMLTestRunner

logger = Log.logger


def report(perform_class, perform_num):

    suite = unittest.TestSuite()
    suite.addTests(map(perform_class, perform_num))
    logger.info("~~~ 测试报告准备中 ~~~")
    logger.info("case执行开始 ~~~")
    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result/report-' + date + '.html')
    titles = readConfig.ret.get_http("title")
    testers = readConfig.ret.get_http("tester")

    if suite is not None:
        fp = open(config_path, 'wb')
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,
                                                   title=titles,
                                                   # description='Test Description',
                                                   tester=testers)
        # runner = xmlrunner.XMLTestRunner(output=config_path)  # jenkins report
        runner.run(suite)
        fp.close()
        time.sleep(10)
        logger.info("        ~~~ 测试报告已完成 ~~~")
        try:
            if platform.system() != "Windows":
                time.sleep(10)
                robot_report.new_report()
                logger.info("测试报告已发送至钉钉群 ~~~")
            else:
                logger.info("%s 运行环境下，无法调用DingTalk !!!" % platform.system())
        except Exception as e:
            logger.error("DingTalk: %s " % e)
    else:
        logger.error("没有可执行的Case ~~~")

