# -*- coding: utf-8 -*-
import os
import sys
import urllib3
import unittest
import requests
o_path = os.getcwd()
sys.path.append(o_path)
from time import sleep
from interfaceTest.judge_inheritance import inheritance
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
from interfaceTest.report_test import report

# from interfaceTest.sql_package import My_sql

logger = Log.logger


# This is main code
class Interface(unittest.TestCase):

    def setUp(self):

        self.results = None
        self.verificationErrors = []

    def tearDown(self):

        error_list = []
        try:
            self.assertEqual([], self.verificationErrors)
        except AssertionError as s:
            error_list.append(s)
            if error_list is not None:
                logger.error("error information is : %s" % error_list)
                logger.error("执行Case错误！测试报告生成中断~~~")
                os._exit(1)

    @classmethod
    def setUpClass(cls):

        logger.info("mysql data init ~~~")
        sleep(1)

    @classmethod
    def tearDownClass(cls):

        logger.info("mysql data clean ~~~")
        sleep(1)

    def login(self):

        date = readExcel.reds.get_xls('userCase.xlsx', 'login')

        global headers
        global xls_name
        global sheet_name

        for method, url, data, content_type, user_agent, user_token, case_name, \
            interface_xls_name, interface_sheet_name in date:
            self.method = method
            self.url = url
            self.data = data
            self.content_type = content_type
            self.user_agent = user_agent
            self.user_token = user_token
            self.case_name = case_name
            xls_name = interface_xls_name
            sheet_name = interface_sheet_name

        headers = {"User-Agent": self.user_agent, "Content-Type": self.content_type,
                   "userToken": self.user_token}

        if self.url and self.data is not None:

            try:

                try:
                    logger.info("-" * 49)
                    logger.info("请求方式:%s" % self.method)
                    logger.info("请求链接:%s" % self.url)
                    logger.info("请求参数:%s" % self.data)
                    logger.info("Content_type: %s" % self.content_type)
                    logger.info("User_Agent: %s" % self.user_agent)
                    logger.info("User_Token: %s" % self.user_token)
                    urllib3.disable_warnings()
                    results = configHttp.runmain.run_main(self.method, self.url, self.data, headers)
                    self.results = results

                except requests.exceptions.ConnectionError as a:

                    self.verificationErrors.append(a)
                    return logger.error("login url error : %s" % self.results)

                except TimeoutError as b:

                    self.verificationErrors.append(b)
                    return logger.error("login timeout error")

                self.assertEqual(self.results.status_code, requests.codes.OK)
                logger.info("login is successful")

                r = inheritance.ret.enter(self.results.json(), self.case_name)

                if r is None:
                    return self.verificationErrors.append(r)

                return None

            except AssertionError as e:

                self.verificationErrors.append(e)
                return logger.error("login is %s" % self.results.status_code)
        else:

            return logger.info("您未输入登陆和登陆参数，直接运行sheet Interface ~~~")

    def Configure_even_code(self):

        try:

            name = xls_name
            header = headers
            sheet = sheet_name
            dates = readExcel.reds.get_xls(name, sheet)

            if dates is None:
                self.verificationErrors.append(dates)
                return logger.error("sheet Interface is %s" % dates)

            for method, url, data, case_name in dates:

                try:
                    logger.info("-" * 34)
                    logger.info("请求方式:%s" % method)
                    logger.info("请求链接:%s" % url)
                    logger.info("请求参数:%s" % data)
                    urllib3.disable_warnings()
                    results = configHttp.runmain.run_main(method, url, data, header)
                    self.results = results

                except requests.exceptions.ConnectionError as a:

                    self.verificationErrors.append(a)
                    return logger.error("url error : %s" % self.results)

                except TimeoutError as b:

                    self.verificationErrors.append(b)
                    return logger.error("timeout error")

                self.assertEqual(self.results.status_code, requests.codes.OK)
                logger.info("assert url is successful")

                r = inheritance.ret.enter(self.results.json(), case_name)

                if r is None:
                    return self.verificationErrors.append(r)

        except AssertionError as e:

            self.verificationErrors.append(e)
            return logger.error("%s assert is error" % self.results.status_code)


if __name__ == '__main__':
    report.report(Interface, ['login', 'Configure_even_code'])
