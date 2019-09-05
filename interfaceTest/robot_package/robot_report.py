import os
import json
import urllib3
import requests
from time import sleep
from interfaceTest import getpathInfo
from interfaceTest.log_and_logresult_package import Log
from interfaceTest.config_package import readConfig as rc

# 调用日志及取测试报告路径
logger = Log.logger
path = getpathInfo.get_Path()
xlsPath = os.path.join(path, 'result')

def test_report():
    # 获取result下所有的文件
    lists = os.listdir(xlsPath)
    # 判断文件是否为空
    if lists is not None:
        # sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
        # 最后对lists元素，按文件修改时间大小从小到大排序。
        lists.sort(key=lambda fn: os.path.getmtime(xlsPath + "/" + fn))
        # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
        file_new = os.path.join(xlsPath, lists[-1])
        # 截取文件名
        cs = os.path.basename(file_new)
        return cs
    else:
        # 为空时返回str, 不会报错！！！
        logger.error("result report is : %s" % lists)
        return str(lists)

def new_report():
    sleep(10)
    # 调用get_http获取 DingTalk url
    hook_token = r"%s" % rc.ret.get_http("hook_token")
    # DingTalk 消息头
    headers = {'content-type': 'application/json'}
    # 调用get_http获取 DingTalk 参数
    date = {
        "msgtype": "link",
        "link": {
            "text": "This is test report",
            "title": u"测试报告",
            "picUrl": "",
            "messageUrl": r"%s" %(rc.ret.get_http("environment_path")) + test_report()
        }
    }
    # 同Configure_even_code文件内一致
    urllib3.disable_warnings()
    # 发送http连接
    r = requests.post(hook_token, headers=headers, data=json.dumps(date))
    # 定义连接后返回的编码格式
    r.encoding = 'utf-8'