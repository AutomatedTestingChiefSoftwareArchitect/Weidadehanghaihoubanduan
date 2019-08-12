import requests
from interfaceTest.log_and_logresult_package import Log

logger = Log.logger


class RunMain(object):

    def send_post(self, url, data, headers, cookies):

        result = requests.post(url, data, headers=headers, cookies=cookies, timeout=2)
        return result

    def send_get(self, url, data, headers, cookies):

        result = requests.get(url, data, headers=headers, cookies=cookies, timeout=2)
        return result

    def run_main(self, method, url, data, headers=None, cookies=None):

        result = None
        if method == 'post':
            result = self.send_post(url, data, headers, cookies)
        elif method == 'get':
            result = self.send_get(url, data, headers, cookies)
        else:
            logger.info("method值错误！！！")
        return result


runmain = RunMain()
