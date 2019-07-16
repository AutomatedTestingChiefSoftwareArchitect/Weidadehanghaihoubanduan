import os
import time
import unittest
import xmlrunner
from interfaceTest.log_and_logresult_package import Log
import interfaceTest.getpathInfo
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
# from interfaceTest.sql_package import My_sql
# from HTMLTestRunner import HTMLTestRunner

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
        self.verificationErrors = []

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def login(self):
        try:
            configHttp.runmain.login_http()
            self.assertIsNone(configHttp.runmain.ret)
            logger.info("login response is successful")
        except AssertionError as e:
            logger.error("login response is %s" % configHttp.runmain.ret)
            self.verificationErrors.append(e)

    def college(self):

        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]
        methods = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][3]
        results = configHttp.runmain.run_main(methods, url, parameter,
                                              configHttp.runmain.headers, configHttp.runmain.cookies)
        try:
            self.assertEqual(results.status_code, 200)
            logger.info("college interface is successful")
        except AssertionError as e:
            self.verificationErrors.append(e)
            logger.error("college interface is %s" % results.status_code)

        if results.json()["result"] is not None:
            self.verificationErrors.append(results.json()["result"])
            logger.error("results.json()['result'] is %s" % results.json()["result"])
        else:
            logger.info("results.json()['result'] is successful")


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(map(Interface, ["login", "college"]))
    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result\\report-'+date+'.xml')
    if suite is not None:
        """
         # 本地报告
        fp = open(config_path, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='Test Report',
                                description='Test Description')
        """
        runner = xmlrunner.XMLTestRunner(output=config_path)  # jenkins report
        runner.run(suite)
        # fp.close()
    else:
        logger.error("Have no case to test")
