import unittest
import os
import sys
from HTMLTestRunner import HTMLTestRunner
import time
from interfaceTest.log_and_logresult_package import Log
import interfaceTest.getpathInfo
from interfaceTest.readexcel_package import readExcel
from interfaceTest.http_package import configHttp


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
    @classmethod  # preform a
    def setUp(cls):
        print("-------------date init----------------")

    @classmethod  # preform a
    def tearDown(cls):
        print("-------------date clean----------------")

    def test_interface(self):
        log.error("pass")
        pass  # this is to here ret.add_num codes
    """
    unittest.skip(reason)
    unittest.skipIf(condition,reason)      即在满足condition条件下跳过该用例
    unittest.skipUnless(condition,reason)  reason用于描述跳过的原因
    """
    @unittest.skipUnless(sys.platform.startswith("xxx"), "xxx")
    def test_date(self):

        url = readExcel.reads.get_xls(('userCase.xlsx', 'login')[0][1])
        dates = readExcel.reads.get_xls(('userCase.xlsx', 'login')[1][2])
        methods = readExcel.reads.get_xls(('userCase.xlsx', 'login')[2][2])
        r = configHttp.result.run_main(methods, url, dates)
        print(r)
        log.info("pass")
        pass  # this is to here ret.is_prime codes


if __name__ == '__main__':
    path = interfaceTest.getpathInfo.get_Path()  # 调用实例化
    config_path = os.path.join(path,
                               './result/report.html')
    log = Log.logger
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Interface))
    date = time.strftime('%Y%m%d%H%M%S')
    if suite is not None:  # 判断test_suite是否为空
        fp = open(config_path, 'wb')
        # 调用HTMLTestRunner
        runner = HTMLTestRunner(fp, title='Test Report', description='Test Description')
        runner.run(suite)
        unittest.main()
    else:
        print("Have no case to test.")
