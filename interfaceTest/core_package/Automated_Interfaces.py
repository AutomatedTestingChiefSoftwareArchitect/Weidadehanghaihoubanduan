# -*- coding: utf-8 -*-
import os
import sys
import urllib3
import unittest
import requests
import platform
import traceback
o_path = os.getcwd()
sys.path.append(o_path)
from time import sleep
from interfaceTest.robot_package import robot_report
from interfaceTest.judge_inheritance import Inheritanced
from interfaceTest.logs_result import Log
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
from interfaceTest.report_test import report
from interfaceTest.sql_package import My_sql as sql
from interfaceTest.config_package import readConfig as rc
from interfaceTest.core_package import Payment_order

# 实例化log方法
logger = Log.logger

class AutomatedInterfaces(unittest.TestCase):
    # 运行TestCase之前准备工作
    def setUp(self):
        # 创建全局变量list
        self.verificationErrors = []

    # 运行TestCase之后执行的方法
    def tearDown(self):
        try:
            # 收集报错,verificationErrors处理
            self.assertEqual([], self.verificationErrors)
        except AssertionError as s:
            logger.error("error information is : %s" % s)
            logger.error("执行Case错误！测试报告生成中断~~~")
            try:
                # 判断运行环境
                if platform.system() != "Windows":
                    sleep(10)
                    # 调用DingTalk发送错误日志方法
                    robot_report.new_report('logs_result', rc.ret.get_email("text"), rc.ret.get_email("titles"))
                    logger.info("error logs 已发送至钉钉群 ~~~")
                else:
                    logger.info("%s 运行环境下，无法调用DingTalk !!!" % platform.system())
            except Exception as e:
                # 捕捉运行报告产生的error
                logger.error("DingTalk: %s " % e)
            # 强制退出程序
            os._exit(1)

    # 运行TestCase之前数据清理工作 注：主要用于数据库操作
    @classmethod
    def setUpClass(cls):
        # select测试账户
        mysql_list = \
            sql.results.select_mysql(rc.ret.get_mysql("user_info"))
        logger.info("Test user name : %s" % mysql_list[0])
        logger.info("Test user mobile : %s" % mysql_list[1])
        # select测试前待支付订单数量
        cls.before_nums = sql.results.select_num(rc.ret.get_mysql("before_nums"))
        logger.info("{开始测试前} — 待支付订单数据总数: %s" % cls.before_nums)

    # 运行TestCase之后数据查询工作
    @classmethod
    def tearDownClass(cls):
        # select测试完后的待支付订单数量
        cls.after_nums = sql.results.select_num(rc.ret.get_mysql("after_nums"))
        if cls.after_nums == cls.before_nums + 1:
            logger.info("{开始测试后} — 待支付订单数据总数: %s" % cls.after_nums)
        else:
            logger.error("待支付订单数量错误: %s" % (cls.after_nums-cls.before_nums))

    def Landing_even(self):
        # 定义global全局变量,用于Configure_even调用
        global xls_name
        global sheet_name
        global headers_dict
        global responses_json
        # 遍历userCase excel login shell数据
        dates = readExcel.reds.get_xls('userCase.xlsx', 'login')
        # 定义变量method···等等, 接收遍历excel数据
        for method, url, data, case_name, user_agent, content_type, \
            interface_xls_name, interface_sheet_name in dates:
            # 将接收数据定义为全局变量
            self.method = method
            self.url = url
            self.data = data
            self.content_type = content_type
            self.user_agent = user_agent
            self.case_name = case_name
            # 定义变量接收变量  //此处后续需要优化 同时运行多个xls_name and sheet_name
            xls_name = interface_xls_name
            sheet_name = interface_sheet_name
        # 参数化headers , 数据均为excel中的遍历
        headers_dict = {"User-Agent": self.user_agent, "Content-Type": self.content_type}
        # 判断shell login 链接和参数是否为空
        if self.url and self.data is not None:
            try:
                try:
                    # 打印shell login 数据
                    logger.info("-" * 49)
                    logger.info("请求方式:%s" % self.method)
                    logger.info("请求链接:%s" % self.url)
                    logger.info("请求参数:%s" % self.data)
                    logger.info("Content_type: %s" % self.content_type)
                    logger.info("User_Agent: %s" % self.user_agent)
                    # headers连接未关闭后,报出SSH错误
                    urllib3.disable_warnings()
                    # 调用封装的http requests方法
                    responses_json = configHttp.runmain.run_main(self.method, self.url, self.data, headers_dict)
                    # 判断url连接错误
                except (ConnectionError or TimeoutError or RuntimeError or BaseException) as exp:
                    # 错误 就添加至到verificationErrors, 然后verificationErrors处理
                    self.verificationErrors.append(exp)
                    return logger.error("except error : %s" % exp)
                # 判断 接口http状态码是否为200
                self.assertEqual(responses_json.status_code, requests.codes.OK)
                logger.info("login is successful")
                # 调用封装匹配response.json方法
                r = Inheritanced.ret.response_method(responses_json.json(), self.case_name)
                # 如果匹配为空,则添加至verificationErrors处理
                if r is None:
                    self.verificationErrors.append(r)
                    return logger.error("response is %s" % r)
            except (AssertionError or BaseException) as e:
                # 用于捕捉主体中的错误,添加至verificationErrors处理
                self.verificationErrors.append(e)
                return logger.error("login is %s" % responses_json.status_code)
        else:
            # 跳过login登陆模块  注：不能不执行login main方法,因为Configure_even 接口需要 headers
            return logger.info("您未输入登陆和登陆参数，直接运行sheet Interface ~~~")

    def Configure_even(self):
        try:
            headers_dict["UserToken"] = responses_json.json()["userToken"]
            # 根据login excel 配置读取对于的excel 和 shell
            dates = readExcel.reds.get_xls(xls_name, sheet_name)
            # 判断读取数据是否为空
            if dates is None:
                # 数据为空时,抛出错误verificationErrors
                self.verificationErrors.append(dates)
                return logger.error("sheet Interface is %s" % dates)
            # 定义变量,遍历excel
            for method, url, data, case_name in dates:
                try:
                    # 打印数据,用于log的可查性
                    logger.info("-" * 34)
                    logger.info("请求方式:%s" % method)
                    logger.info("请求链接:%s" % url)
                    logger.info("请求参数:%s" % data)
                    urllib3.disable_warnings()
                    # 调用封装的http requests方法
                    self.results = configHttp.runmain.run_main(method, url, data, headers_dict)
                    if url[url.rindex('/') + 1:] != rc.ret.get_order("submitOrder"):
                        self.orderId = Payment_order.PayOrder().SubmitOrder(self.results.json())
                    if self.orderId is not None:
                        self.results = Payment_order.PayOrder().PrePay(headers_dict)
                # 判断url连接错误
                except (ConnectionError or TimeoutError or RuntimeError or BaseException) as exp:
                    # 错误 就添加至到verificationErrors, 然后verificationErrors处理
                    self.verificationErrors.append(exp)
                    return logger.error("except error : %s" % exp)
                # 判断 接口http状态码是否为200
                self.assertEqual(self.results.status_code, requests.codes.OK)
                logger.info("assert url is successful")
                # 调用封装匹配response.json方法
                ret = Inheritanced.ret.response_method(self.results.json(), case_name)
                # 如果匹配为空,则添加至verificationErrors处理
                if ret is None:
                    self.verificationErrors.append(r)
                    return logger.error("response is %s" % ret)
        except (AssertionError or BaseException) as e:
            # 用于捕捉主体中的错误,添加至verificationErrors处理
            self.verificationErrors.append(e)
            return logger.error("%s assert is error" % self.results.status_code)

if __name__ == '__main__':
    # 运行main方法
    report.report(AutomatedInterfaces, ['Landing_even', 'Configure_even'])