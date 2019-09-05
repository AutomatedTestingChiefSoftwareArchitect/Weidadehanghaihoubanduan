import requests
from interfaceTest.log_and_logresult_package import Log

# 实例化log方法
logger = Log.logger

class RunMain(object):
    # 封装http requests post 方法
    def send_post(self, url, data, headers):
        # 运行post接口,后返回
        result = requests.post(url=url, data=data, headers=headers, verify=False)
        return result

    # 封装http requests get 方法
    def send_get(self, url, data, headers):
        # 运行get接口,后返回
        result = requests.get(url=url, params=data, headers=headers, verify=False)
        return result

    # 根据method来判断需要运行get 还是 post 方法
    def run_main(self, method, url=None, data=None, headers=None):
        # 定义空变量
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
        elif method == 'get':
            result = self.send_get(url, data, headers)
        else:
            logger.info("method值错误！！！")
        return result

runmain = RunMain()
