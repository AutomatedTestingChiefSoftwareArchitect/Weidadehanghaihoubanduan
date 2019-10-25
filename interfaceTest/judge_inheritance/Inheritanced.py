from time import sleep
from interfaceTest.logs_result import Log
from interfaceTest.readexcel_package import readExcel
from interfaceTest.judge_inheritance import response_check

logger = Log.logger

def method_int(response_json, case_name):

    if response_json[ret.methods] is None or response_json[ret.methods] == 0:

        return response_check.rc.Check_error(response_json, case_name)
    else:
        return response_check.rc.Check_info(response_json, case_name)

def method_str(response_json, case_name):

    if response_json[ret.methods] is 'None' or response_json[ret.methods] is 'none'\
            or response_json[ret.methods] is 'Null' or response_json[ret.methods] is 'null':

        return response_check.rc.Check_error(response_json, case_name)
    else:
        return response_check.rc.Check_info(response_json, case_name)

def method_list(response_json, case_name):

    return method_int(response_json, case_name)

def method_dict(response_json, case_name):

    list_keys = []
    list_item = []
    list_dates = readExcel.reds.get_xls('userCase.xlsx', 'Response')
    for list_key in list_dates:
        list_keys = list_key
    dict_info = response_json[ret.methods]
    if len(dict_info) != 0:
        dict_keys = list(dict_info.keys())
        list_nums = [x for x in list_keys if x in dict_keys]
        logger.info("check keys nums ： %s" % list_nums)
        if len(list_nums) == 0:
            logger.info("    匹配不到对应的response keys  请联系管理进行手动添加 ~~~")
            print(case_name + " : " + str(response_json))
            print(), sleep(1)
            return response_json
        for item in list_nums:
            if response_json[ret.methods][item] is None:
                logger.error("       %s is null" % item)
                print(case_name + " : " + str(response_json))
                print(), sleep(1)
                list_item.append(item)
                return response_json[ret.methods][item]
            else:
                logger.info("        %s check is successful" % item)
                list_item.append(item)
        if list_item is not None:
            print(case_name + " : " + str(response_json))
            print(), sleep(1)
            return response_json
    else:
       logger.info("response keys is %s" % dict_info)
       return response_json

class FirstClass(object):

    def __init__(self):

        self.methods = "data"

    def response_method(self, response_json, case_name):
        
        result = None
        if type(response_json[self.methods]) is int:
            result = method_int(response_json, case_name)
        elif type(response_json[self.methods]) is str:
            result = method_str(response_json, case_name)
        elif type(response_json[self.methods]) is list:
            result = method_list(response_json, case_name)
        elif type(response_json[self.methods]) is dict:
            result = method_dict(response_json, case_name)
        else:
            logger.error("      type response is %s" % response_json[self.methods])
        return result

ret = FirstClass()