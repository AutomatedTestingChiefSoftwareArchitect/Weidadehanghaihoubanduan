import urllib3
from interfaceTest.config_package import readConfig
from interfaceTest.http_package import configHttp
from interfaceTest.core_package import Automated_Interfaces


def SubmitOrder(resubmit):
    # 获取submitProductOrder response
    ProductOrder_orderId = resubmit["data"]["orderId"]
    return ProductOrder_orderId


class PayOrder(object):

    def PrePay(self, Order_Id, headers_dict):
        # 待支付接口
        url = readConfig.ret.get_order("PrePay_url")
        data = {"payWayId":1,"orderId":Order_Id,"clientType":"miniApp"}
        print(self.ProductOrder_orderId)
        urllib3.disable_warnings()
        PrePayJson = configHttp.runmain.run_main('post', url, data, headers_dict)
        return PrePayJson
