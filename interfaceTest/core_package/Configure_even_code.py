import os
import unittest
import requests
from time import sleep
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
from interfaceTest.report_test import report
# from interfaceTest.sql_package import My_sql

logger = Log.logger


class Interface(unittest.TestCase):

    def setUp(self):

        self.cookies = None
        self.results = None
        self.verificationErrors = []
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

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

        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[1][2]

        if url and parameter is not None:
            try:
                try:
                    results = requests.get(url, parameter, headers=self.headers, timeout=2)
                    self.results = results
                except requests.exceptions.ConnectionError as a:
                    self.verificationErrors.append(a)
                    return logger.error("login url error : %s" % self.results)
                except TimeoutError as b:
                    self.verificationErrors.append(b)
                    return logger.error("login timeout error~~~")

                self.assertEqual(self.results.status_code, requests.codes.OK)
                logger.info("-----login is successful")

                if "result" in self.results.json():

                    if self.results.json()["result"] is None:
                        self.verificationErrors.append(self.results.json())
                        return logger.error("-----login results is error")
                    else:
                        logger.info("-----login results is successful")
                        self.cookies = self.results.cookies
                        logger.info("login cookie is : %s" % self.cookies)
                        return self.cookies, print(self.results.json()), sleep(1)

                elif "response" in self.results.json():

                    if self.results.json()["response"] is None:
                        self.verificationErrors.append(self.results.json())
                        return logger.error("-----login results is error")
                    else:
                        logger.info("-----login results is successful")
                        self.cookies = self.results.cookies
                        logger.info("login cookie is : %s" % self.cookies)
                        return self.cookies, print(self.results.json()), sleep(1)
                else:

                    logger.info("-----login results is successful")
                    self.cookies = self.results.cookies
                    logger.info("login cookie is : %s" % self.cookies)
                    return self.cookies, print(self.results.json()), sleep(1)

            except AssertionError as e:

                self.verificationErrors.append(e)
                return logger.error("-----login is %s" % self.results.status_code)
        else:

            return logger.info("您未输入登陆和登陆参数，直接运行sheet Interface ~~~")

    def Configure_even_code(self):

        try:
            dates = readExcel.reds.get_xls('userCase.xlsx', 'Interface')
            if dates is None:
                self.verificationErrors.append(dates)
                return logger.error("date is %s" % dates)

            for method, url, data in dates:

                try:
                    logger.info("请求方式:%s" % method)
                    logger.info("请求链接:%s" % url)
                    logger.info("请求参数:%s" % data)
                    results = configHttp.runmain.run_main(method, url, data, headers=self.headers, cookies=self.cookies)
                    self.results = results
                except requests.exceptions.ConnectionError as a:
                    self.verificationErrors.append(a)
                    return logger.error("url error : %s" % self.results)
                except TimeoutError as b:
                    self.verificationErrors.append(b)
                    return logger.error("timeout error~~~")

                self.assertEqual(self.results.status_code, requests.codes.OK)
                logger.info("-----%s is successful" % url)

                if "result" in self.results.json():

                    if self.results.json()["result"] is None:
                        self.verificationErrors.append(self.results.json())
                        return logger.error("-----%s.json is error" % url)
                    else:
                        logger.info("-----%s.json is successful" % url)
                        print(self.results.json()), sleep(1)

                elif "response" in self.results.json():

                    if self.results.json()["response"] is None:
                        self.verificationErrors.append(self.results.json())
                        return logger.error("-----%s.json is error" % url)
                    else:
                        logger.info("-----%s.json is successful" % url)
                        print(self.results.json()), sleep(1)
                else:

                    logger.info("-----%s.json is successful" % url)
                    print(self.results.json()), sleep(1)

        except AssertionError as e:

            self.verificationErrors.append(e)
            return logger.error("-----%s assert is error" % self.results.status_code)


if __name__ == '__main__':

    report.report(Interface, ["login", 'Configure_even_code'])
