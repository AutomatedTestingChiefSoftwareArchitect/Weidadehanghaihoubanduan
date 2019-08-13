from interfaceTest.log_and_logresult_package import Log
from time import sleep

logger = Log.logger


class FirstClass(object):

    def first(self, r):

        return logger.info("assert json is not "), r

    def second(self, r):

        if "data" in r:
            if r["data"] is None:
                return logger.error("json data is error")
            else:
                logger.info("json data is successful")
                return print(r), sleep(1)
        else:
            self.first(r)

    def three(self, r):

        if "response" in r:
            if r["response"] is None:
                return logger.error("json response is error")
            else:
                logger.info("json response is successful")
                return print(r), sleep(1)
        else:
            self.second(r)

    def enter(self, r):

        if "result" in r:
            if r["result"] is None:
                return logger.error("json results is error")
            else:
                logger.info("json results is successful")
                return print(r), sleep(1)
        else:
            self.three(r)


ret = FirstClass()