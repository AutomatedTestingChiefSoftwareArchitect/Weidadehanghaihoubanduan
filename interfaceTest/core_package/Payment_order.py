from interfaceTest.config_package import readConfig
from interfaceTest.http_package import configHttp
from interfaceTest.core_package import Automated_Interfaces

class PayOrder(object):

    def __init__(self):
        # 定义全局变量
        self.ProductOrder_orderId = None

    def SubmitOrder(self, resubmit):
        # 获取submitProductOrder response
        self.ProductOrder_orderId = resubmit["data"]["orderId"]
        return self.ProductOrder_orderId

    def PrePay(self, headers_dict):
        # 待支付接口
        url = readConfig.ret.get_order("PrePay_url")
        data = {"payWayId":1,"orderId":self.ProductOrder_orderId,"clientType":"miniApp"}
        PrePayJson = configHttp.runmain.run_main('post', url, data, headers_dict)
        return PrePayJson