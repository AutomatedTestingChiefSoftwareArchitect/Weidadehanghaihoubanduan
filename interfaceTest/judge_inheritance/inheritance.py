from interfaceTest.log_and_logresult_package import Log
from time import sleep

logger = Log.logger


class FirstClass(object):

    def first(self, r, case_name):

        logger.info("        匹配不到对应的response, 请联系管理进行手动添加~~~"), print(case_name + " : " + str(r)), sleep(1)
        return r

    def second(self, r, case_name):

        if "result" in r["data"]:

            if r["data"]["result"] is None:
                logger.error("       json data is error"), print(case_name + " : " + str(r)), sleep(1)
                return r["data"]["result"]
            else:
                logger.info("       json data is successful"), print(case_name + " : " + str(r)), sleep(1)
                return r

        else:
            return self.first(r, case_name)

    def three(self, r, case_name):

        if "cashCouponTotalCount" in r["data"]:

            if r["data"]["cashCouponTotalCount"] is None:
                logger.error("       json data is error"), print(case_name + " : " + str(r)), sleep(1)
                return r["data"]["cashCouponTotalCount"]
            else:
                logger.info("        json data is successful"), print(case_name + " : " + str(r)), sleep(1)
                return r
        else:
            return self.second(r, case_name)

    def enter(self, r, case_name):

        if "id" in r["data"]:

            if r["data"]["id"] is None:
                logger.error("       json data is error"), print(case_name + " : " + str(r)), sleep(1)
                return r["data"]["id"]
            else:
                logger.info("       json data is successful"), print(case_name + " : " + str(r)), sleep(1)
                return r
        else:
            return self.three(r, case_name)


ret = FirstClass()
