"""
import requests

url = "https://api.aixiangdao.com/getCityTopics"
urls = "https://www.baidu.com/"

data = {"cityId":29}
dates = {}
"""
import requests
from interfaceTest.http_package import configHttp
from interfaceTest.readexcel_package import readExcel
from interfaceTest.judge_inheritance import inheritance

method = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][0]
url = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][1]
data = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][2]
name = readExcel.reds.get_xls('userCase.xlsx', 'login')[0][6]
# content_type = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[0][3]
# user_agent = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[0][4]
# user_token = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[0][5]

headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 ("
                          "KHTML, like Gecko) Mobile/14G60 MicroMessenger/7.0.2(0x17000222) NetType/WIFI "
                          "Language/zh_CN",
            "Content-Type": "application/json",
            "userToken": "51321b4f-c0bb-4474-8981-fbed65a01fb6"
        }
print(method)
print(url)
print(data)
print(name)
# print(content_type)
# print(user_agent)
# print(user_token)

results = configHttp.runmain.run_main(method, url, data, headers)
# results = requests.get(url, params=data, headers=headers)
# print(results.json())
# ret = inheritance.ret.enter(results.json(), name)
# print(results)
result = {'data': {"2": 2}}
r = inheritance.ret.enter(result, name)