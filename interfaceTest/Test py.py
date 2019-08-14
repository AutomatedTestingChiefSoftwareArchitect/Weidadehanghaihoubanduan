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


method = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[1][0]
url = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[1][1]
data = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[1][2]
# content_type = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[0][3]
# user_agent = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[0][4]
# user_token = readExcel.reds.get_xls('userCase.xlsx', 'Interface')[0][5]

headers = {
            "User-Agent": "application/json",
            "Content-Type": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, "
                            "like Gecko) Mobile/14G60 MicroMessenger/7.0.2(0x17000222) NetType/WIFI Language/zh_CN",
            "userToken": "e751ed59-6485-4387-8dbf-425f0c635505"
        }
print(url)
print(data)
# print(content_type)
# print(user_agent)
# print(user_token)

# results = configHttp.runmain.run_main(method, url=url, data=data, headers=headers)
results = requests.post(url, None, data, headers=headers)
print(results.json())
