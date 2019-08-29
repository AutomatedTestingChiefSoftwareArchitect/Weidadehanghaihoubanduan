import os
import unittest
import requests
from time import sleep
from log_and_logresult_package import Log
from readexcel_package import readExcel
from http_package import configHttp
from report_test import report
# from interfaceTest.sql_package import My_sql

logger = Log.logger


class Interface(unittest.TestCase):

    def setUp(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        self.cookie = None
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

        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]

        try:
            try:
                results = requests.post(url, parameter, self.headers, timeout=2)
                self.results = results
            except requests.exceptions.ConnectionError as a:
                self.verificationErrors.append(a)
                return logger.error("login url error : %s" % self.results)
            except TimeoutError as b:
                self.verificationErrors.append(b)
                return logger.error("login timeout error~~~")
            self.assertEqual(self.results.status_code, 500)
            logger.info("-----login is successful")
            if self.results.json()["data"] is not None:
                self.verificationErrors.append(self.results.json()["data"])
                return logger.error("-----login results is error")
            else:
                logger.info("-----login results is successful")
                self.cookie = self.results.cookies
                logger.info("login cookie is : %s" % self.cookie)
                return self.cookie, print(self.results.json())
        except AssertionError as e:
            self.verificationErrors.append(e)
            return logger.error("-----login is %s" % self.results.status_code)

    def college(self):

        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][2]
        methods = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][3]

        try:
            try:
                results = configHttp.runmain.run_main(methods, url, parameter, self.headers, self.cookie)
                self.results = results
            except requests.exceptions.ConnectionError as a:
                self.verificationErrors.append(a)
                return logger.error("login url error : %s" % self.results)
            except TimeoutError as b:
                self.verificationErrors.append(b)
                return logger.error("login timeout error~~~")
            self.assertEqual(self.results.status_code, 200)
            logger.info("-----college is successful")
            if self.results.json()["result"] is not None:
                self.verificationErrors.append(self.results.json()["result"])
                return logger.error("-----college results is error")
            else:
                logger.info("-----college results is successful")
                return print(self.results.json())
        except AssertionError as e:
            self.verificationErrors.append(e)
            return logger.error("-----college is error")


if __name__ == '__main__':

    report.report(Interface, ['login', 'college'])
