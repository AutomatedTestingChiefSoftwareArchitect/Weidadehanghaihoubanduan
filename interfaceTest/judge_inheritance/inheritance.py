from time import sleep
from interfaceTest.logs_result import Log

logger = Log.logger

def additional(response_json, case_name):
    # 如果在FirstClass遍历为找到, 就执行此此程序
    logger.info("    匹配不到对应的response, 请联系管理进行手动添加 ~~~")
    print(case_name + " : " + str(response_json))
    print(), sleep(1)
    return response_json

class FirstClass(object):

    def __init__(self):
        # 全局变量定义
        self.keys_json = None

    def second(self, response_json, case_name):
        if "result" in response_json:
            if response_json["result"] is None:
                logger.error("       json data is error")
                print(case_name + " : " + str(response_json))
                print(), sleep(1)
                return response_json["result"]
            else:
                logger.info("       json data is successful")
                print(case_name + " : " + str(response_json))
                print(), sleep(1)
                return response_json
        else:
            return additional(response_json, case_name)

    def three(self, response_json, case_name):
        if "cashCouponTotalCount" in response_json[self.keys_json]:
            if response_json[self.keys_json]["cashCouponTotalCount"] is None:
                logger.error("       json data is error")
                print(case_name + " : " + str(response_json))
                print(), sleep(1)
                return response_json[self.keys_json]["cashCouponTotalCount"]
            else:
                logger.info("        json data is successful")
                print(case_name + " : " + str(response_json))
                print(), sleep(1)
                return response_json
        else:
            return self.second(response_json, case_name)

    def enter(self, response_json, case_name):
        # 遍历response_json, 获取keys
        for keys in response_json:
            # 赋值全局变量
            self.keys_json = keys
            # 判断r 的值是否是一个字典
            if type(response_json[self.keys_json]) is dict:
                # 判断id 是否在这个字典中
                if "id" in response_json[self.keys_json]:
                    # 判断id的值是否为空
                    if response_json[self.keys_json]["id"] is None:
                        logger.error("       json data is error")
                        print(case_name + " : " + str(response_json))
                        print(), sleep(1)
                        return response_json[self.keys_json]["id"]
                    else:
                        logger.info("        json data is successful")
                        print(case_name + " : " + str(response_json))
                        print(), sleep(1)
                        return response_json
                else:
                    # 如果id不在keys内,调用three,second方法, 类似于继承, 但是py只能继承方法 ！！！
                    return self.three(response_json, case_name)
            else:
                # 此处预留, 后续编写keys value is not dict
                logger.info("        现阶段程序不支持json int and str type ~~~")
                print(case_name + " : " + str(response_json))
                print(), sleep(1)
                return response_json

ret = FirstClass()
