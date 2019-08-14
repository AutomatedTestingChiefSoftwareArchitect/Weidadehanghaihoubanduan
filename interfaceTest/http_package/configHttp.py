import requests
from interfaceTest.log_and_logresult_package import Log

logger = Log.logger


class RunMain(object):

    def send_post(self, url, data, headers):

        result = requests.post(url=url, data=data, headers=headers, verify=False)
        return result

    def send_get(self, url, data, headers):

        result = requests.get(url=url, data=data, headers=headers, verify=False)
        return result

    def run_main(self, method, url=None, data=None, headers=None):

        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
        elif method == 'get':
            result = self.send_get(url, data, headers)
        else:
            logger.info("method值错误！！！")
        return result


runmain = RunMain()
