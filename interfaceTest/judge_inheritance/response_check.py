from interfaceTest.judge_inheritance import Inheritanced as ret

class ResponseCheck(object):

    def Check_info(self, response_json, case_name):

        logger.info("        %s check is successful" % response_json[ret.methods])
        print(case_name + " : " + str(response_json))
        print(), sleep(1)
        return response_json

    def Check_error(self,response_json, case_name):

        logger.error("      response check error: %s" % response_json[ret.methods])
        print(case_name + " : " + str(response_json))
        print(), sleep(1)
        return response_json[ret.methods]

rc = ResponseCheck()