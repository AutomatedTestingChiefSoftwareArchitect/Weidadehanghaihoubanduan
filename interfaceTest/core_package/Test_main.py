import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from interfaceTest.log_and_logresult_package import Log
import interfaceTest.getpathInfo
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp
# from interfaceTest.sql_package import My_sql
# import sys

logger = Log.logger


class Interface(unittest.TestCase):
    """
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
    """
    @classmethod
    def setUp(cls):
        print("-------------date init----------------")

    @classmethod
    def tearDown(cls):
        print("-------------date clean----------------")

    """
    @unittest.skipUnless(sys.platform.startswith("哈哈哈"), "not stat")
    def test_interface(self):
        pass  # this is to here ret.add_num codes
    unittest.skip(reason)
    unittest.skipIf(condition,reason)      即在满足condition条件下跳过该用例
    unittest.skipUnless(condition,reason)  reason用于描述跳过的原因
    """
    def test_1_login(self):

        configHttp.runmain.login_http()

    def test_2_college(self):

        url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
        parameter = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]
        methods = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][3]
        results = configHttp.runmain.run_main(methods, url, parameter,
                                              configHttp.runmain.headers, configHttp.runmain.cookies)
        try:
            self.assertEqual(results.status_code, 200)
            logger.info("college interface is successful")
        except:
            logger.error("college interface is %s" % results.status_code)


if __name__ == '__main__':

    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    suite = unittest.TestSuite()
    suite.addTest(Interface("test_1_login"))
    suite.addTest(Interface("test_2_college"))
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result\\report-'+date+'.html')
    if suite is not None:
        fp = open(config_path, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='Test Report',
                                description='Test Description')
        runner.run(suite)
        fp.close()
    else:
        logger.error("Have no case to test")