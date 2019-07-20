import os
import unittest
import requests
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
from interfaceTest.testCase import login_report
# import xmlrunner
# from interfaceTest.sql_package import My_sql

logger = Log.logger


class Interface(unittest.TestCase):

    def setUp(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        self.cookie = None
        self.verificationErrors = []

    def tearDown(self):
        error_list = []
        try:
            self.assertEqual([], self.verificationErrors)
        except AssertionError as s:
            error_list.append(s)
            if error_list is not None:
                logger.error("error information is : %s" % error_list)
                os._exit(1)

    def login(self):
        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]
        results = requests.post(url, parameter, self.headers)
        try:
            self.assertEqual(results.status_code, 500)
            logger.info("-----login is successful-----")
            if results.json()["data"] is not None:
                self.verificationErrors.append(results.json()["data"])
                logger.error("-----login results is error-----")
            else:
                logger.info("-----login results is successful-----")
                self.cookie = results.cookies
                logger.info("login cookie is : %s" % self.cookie)
                return self.cookie, print(results.json())

        except AssertionError as e:
            logger.error("-----login is %s-----" % results.status_code)
            self.verificationErrors.append(e)

    def college(self):
        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][2]
        methods = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][3]
        results = configHttp.runmain.run_main(methods, url, parameter, self.headers, self.cookie)
        try:
            self.assertEqual(results.status_code, 200)
            logger.info("-----college is successful-----")
            if results.json()["result"] is not None:
                self.verificationErrors.append(results.json()["result"])
                logger.error("-----college results is error-----")
            else:
                logger.info("-----college results is successful-----")
                return print(results.json())

        except AssertionError as e:
            logger.error("-----college is error-----")
            self.verificationErrors.append(e)


if __name__ == '__main__':

    login_report.report()
