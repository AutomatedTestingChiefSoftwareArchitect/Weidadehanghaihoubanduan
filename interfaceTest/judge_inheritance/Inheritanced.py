from time import sleep
from interfaceTest.logs_result import Log
from interfaceTest.readexcel_package import readExcel
from interfaceTest.judge_inheritance import response_check
from interfaceTest.config_package import readConfig

logger = Log.logger

def method_int(response_json):

    if response_json in (None, 0):
        logger.info("check %s is" % response_json)
        return response_json
    else:
        logger.error("check %s is" % response_json)
        return response_json

def method_str(response_json):

    if response_json in ('None', 'none', 'Null', 'null'):
        logger.info("check %s is" % response_json)
        return response_json
    else:
        logger.error("check %s is" % response_json)
        return response_json

def method_list(response_json):

    return method_int(response_json)

def method_dict(response_json):
    list_keys = []
    list_item = []
    list_dates = readExcel.reds.get_xls('userCase.xlsx', 'Response')
    for list_key in list_dates:
        list_keys = list_key
    dict_keys = response_json.key()
    list_nums = [x for x in list_keys if x in dict_keys]
    logger.info("check keys nums ： %s" % list_nums)
    if len(list_nums) == 0:
        logger.info("    匹配不到对应的response keys  请联系管理进行手动添加 ~~~")
        # print(case_name + " : " + str(response_json))
        # print(), sleep(1)
        return list_nums
    else:
        for item in list_nums:
            if not response_json[item]:
                logger.error("       %s is null" % item)
                # print(case_name + " : " + str(response_json[item]))
                # print(), sleep(1)
                list_item.append(item)
                return response_json[item]
            else:
                logger.info("        %s check is successful" % item)
                list_item.append(item)
    if list_item:
        # print(case_name + " : " + str(response_json))
        # print(), sleep(1)
        return response_json

class FirstClass(object):

    def __init__(self):
        self.result_list = []

    def response_method(self, response_json, case_name):
        if response_json:
            methods_keys = list(response_json.keys())
            for items in methods_keys:
                # if type(response_json[items]) is int:
                if isinstance(response_json[items], int):
                    self.result_list.append(method_int(response_json[items]))
                if isinstance(response_json[items], str):
                    self.result_list.append(method_str(response_json[items]))
                if isinstance(response_json[items], list):
                    self.result_list.append(method_list(response_json[items]))
                if isinstance(response_json[items], dict):
                    self.result_list.append(method_dict(response_json[items]))
        else:
            logger.error("      type response is %s" % response_json)
            self.result_list.append(response_json)
        if None or 0 in self.result_list:
            return response_check.rc.Check_error()
        else:
            return response_check.rc.Check_info(response_json, case_name)

ret = FirstClass()