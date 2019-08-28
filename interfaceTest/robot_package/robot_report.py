import os
import json
import urllib3
import requests
from interfaceTest import getpathInfo

path = getpathInfo.get_Path()
xlsPath = os.path.join(path, "result")


def test_report():

    lists = os.listdir(xlsPath)
    lists.sort(key=lambda fn: os.path.getmtime(xlsPath + "\\" + fn))
    file_new = os.path.join(xlsPath, lists[-2])
    # as = os.system(r'%s' % file_new)  # 打开网页
    cs = os.path.basename(file_new)
    return cs


def new_report():

    hook_token = "https://oapi.dingtalk.com/robot/send?access_token=" \
                 "08b8a15e755cc50cceb4ec2b5dc5110e8a73d78b36e01f50bfa9bf74a298c28d"
    headers = {'content-type': 'application/json'}
    date = {

        "msgtype": "link",
        "link": {
            "text": "This is test report",
            "title": u"测试报告",
            "picUrl": "",
            "messageUrl": r"http://localhost:63342/PyrequestCode/interfaceTest/result/" + test_report()
        }
    }
    urllib3.disable_warnings()
    r = requests.post(hook_token, headers=headers, data=json.dumps(date))
    r.encoding = 'utf-8'
