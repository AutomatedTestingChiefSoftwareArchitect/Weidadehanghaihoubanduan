import requests
from interfaceTest.log_and_logresult_package import Log

logger = Log.logger


class RunMain(object):

    def send_post(self, url, data, headers, cookies):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url, data, headers=headers, cookies=cookies, timeout=2)
        # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def send_get(self, url, data, headers, cookies):
        result = requests.get(url, data, headers=headers, cookies=cookies, timeout=2)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def run_main(self, method, url, data, headers=None, cookies=None):
        # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers, cookies)
        elif method == 'get':
            result = self.send_get(url, data, headers, cookies)
        else:
            logger.info("method值错误！！！")
        return result


runmain = RunMain()
