import os
import time
import unittest
from interfaceTest.log_and_logresult_package import Log
import interfaceTest.getpathInfo
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
from HTMLTestRunner import HTMLTestRunner
import requests
# import xmlrunner
# from interfaceTest.sql_package import My_sql

logger = Log.logger


class Interface(unittest.TestCase):
    """
    //TODO this is unittest methods
    self.assertEqual(a, b)       check that a == b
    self.assertNotEqual(a, b)    check that a != b
    self.assertTrue(x)           check that bool(x) is true
    self.assertFalse(x)          check that bool(x) is False
    self.assertIs(a, b)          check that a is b
    self.assertIsNot(a, b)       check that a is not b
    self.assertIsNone(x)         check that x is none
    self.assertIsNotNone(x)      check that x is not none
    self.assertIn(a, b)          check that a in b
    self.assertNotIn(a,b)        check that a not in b
    self.assertIsInstance(a, b)  check that isinstance(a, b)
    self.assertNotIsInstance(a, b)  check that not isinstance(a, b)
    unittest.skip(reason)
    unittest.skipIf(condition,reason)      即在满足condition条件下跳过该用例
    unittest.skipUnless(condition,reason)  reason用于描述跳过的原因\

    """
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
                return self.cookie

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
            if results.json()["result"] is None:
                self.verificationErrors.append(results.json()["result"])
                logger.error("-----college results is error-----")
            else:
                return logger.info("-----college results is successful-----")

        except AssertionError as e:
            logger.error("-----college is error-----")
            self.verificationErrors.append(e)


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(map(Interface, ["login", "college"]))
    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result\\report-'+date+'.html')
    if suite is not None:
        fp = open(config_path, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='Test Report',
                                description='Test Description')

        # runner = xmlrunner.XMLTestRunner(output=config_path)  # jenkins report
        runner.run(suite)
        fp.close()
    else:
        logger.error("Have no case to test")
