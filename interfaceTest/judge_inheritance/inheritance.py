from interfaceTest.log_and_logresult_package import Log
from time import sleep

logger = Log.logger


class FirstClass(object):

    def first(self, r):

        logger.info("此条消息为select未匹配, 后返回~"), print(r), sleep(1)
        return r

    def second(self, r):

        if "id" in r["data"]:

            if r["data"]["id"] is None:
                logger.error("json data is error"), print(r), sleep(1)
                return r["data"]["id"]
            else:
                logger.info("json data is successful"), print(r), sleep(1)
                return r

        else:
            return self.first(r)

    def three(self, r):

        if "response" in r["data"]:

            if r["data"]["response"] is None:
                logger.error("json data is error"), print(r), sleep(1)
                return r["data"]["response"]
            else:
                logger.info("json data is successful"), print(r), sleep(1)
                return r
        else:
            return self.second(r)

    def enter(self, r):

        if "result" in r["data"]:

            if r["data"]["result"] is None:
                logger.error("json data is error"), print(r), sleep(1)
                return r["data"]["result"]
            else:
                logger.info("json data is successful"), print(r), sleep(1)
                return r
        else:
            return self.three(r)


ret = FirstClass()
