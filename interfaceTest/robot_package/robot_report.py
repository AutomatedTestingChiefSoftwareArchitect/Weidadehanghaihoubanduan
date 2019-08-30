import os
import json
import urllib3
import requests
import platform
from time import sleep
from interfaceTest import getpathInfo
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.config_package import readConfig as rc

logger = Log.logger
path = getpathInfo.get_Path()

def environment_path():

    try:
        if platform.system() == "Windows":
            xlsPath = os.path.join(path, 'result')
        else:
            xlsPath = rc.ret.get_http("environment_path")
        return xlsPath
    except Exception as a:
        raise logger.info("DingTalk: %s " % a)

def test_report():

    xlsPaths = environment_path()
    lists = os.listdir(xlsPaths)
    if lists is not None:
        lists.sort(key=lambda fn: os.path.getmtime(xlsPaths + "/" + fn))
        file_new = os.path.join(xlsPaths, lists[-1])
        cs = os.path.basename(file_new)
        return cs
    else:
        logger.error("result report is : %s" % lists)
        return str(lists)


def new_report():

    sleep(10)
    hook_token = "https://oapi.dingtalk.com/robot/send?access_token" \
                 "=fd6ed0a8d8b8fe335dea97ac3b850c73c26363251948463c45b182bf9ca99eb1 "
    headers = {'content-type': 'application/json'}

    date = {

        "msgtype": "link",
        "link": {
            "text": "This is test report",
            "title": u"测试报告",
            "picUrl": "",
            "messageUrl": environment_path() + test_report()
        }
    }

    urllib3.disable_warnings()
    r = requests.post(hook_token, headers=headers, data=json.dumps(date))
    r.encoding = 'utf-8'
