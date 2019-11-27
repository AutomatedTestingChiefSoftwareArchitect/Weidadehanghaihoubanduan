from time import sleep
from interfaceTest.logs_result import Log
from interfaceTest.judge_inheritance import Inheritanced

logger = Log.logger

class ResponseCheck(object):

    def Check_info(self, response_json, case_name):

        logger.info("        %s check is successful" % response_json)
        print(case_name + " : " + str(response_json))
        print(), sleep(1)
        return response_json

    def Check_error(self):

        # logger.error("      response check error: %s" % response_json)
        # print(case_name + " : " + str(response_json))
        # print(), sleep(1)
        return None

rc = ResponseCheck()