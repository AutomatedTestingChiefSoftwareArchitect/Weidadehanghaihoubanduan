import os
import time
import platform
import unittest
import interfaceTest.getpathInfo
from interfaceTest.config_package import readConfig
from interfaceTest.robot_package import robot_report
from interfaceTest.logs_result import Log
from interfaceTest.report_test.report_tools import HTMLTestRunnerCN
# import xmlrunner
# from HTMLTestRunner import HTMLTestRunner

# 调用日志方法
logger = Log.logger

def report(perform_class, perform_num):
    # 添加unittest测试套件
    suite = unittest.TestSuite()
    # 指定需要执行的类及方法
    suite.addTests(map(perform_class, perform_num))
    logger.info("~~~ 测试报告准备中 ~~~")
    logger.info("case执行开始 ~~~")
    # 打印当前时间
    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    # 获取路径
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result/report-' + date + '.html')
    # 调用get_http获取测试标题及测试人员
    titles = readConfig.ret.get_http("title")
    testers = readConfig.ret.get_http("tester")
    # 判断测试套件是否为空
    if suite is not None:
        # 打开及写入config_path
        fp = open(config_path, 'wb')
        # 测试报告封装调用,用于添加自定义描述
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,
                                                   title=titles,
                                                   # description='Test Description',
                                                   tester=testers)
        # runner = xmlrunner.XMLTestRunner(output=config_path)  # jenkins report

        # 运行测试方法
        runner.run(suite)
        # 关闭测试报告文件
        fp.close()
        # 定义休眠,避免报告还未完全生成完毕,发送出去文件为空
        time.sleep(10)
        logger.info("        ~~~ 测试报告已完成 ~~~")
        try:
            # 判断运行环境
            if platform.system() != "Windows":
                time.sleep(10)
                # 调用DingTalk发送报告方法
                robot_report.new_report('result', rc.ret.get_http("text"), rc.ret.get_http("titles"))
                logger.info("测试报告已发送至钉钉群 ~~~")
            else:
                logger.info("%s 运行环境下，无法调用DingTalk !!!" % platform.system())
        except Exception as e:
            # 捕捉运行报告产生的error
            logger.error("DingTalk: %s " % e)
    else:
        # 没有可执行的case时,返回
        logger.error("没有可执行的Case ~~~")

