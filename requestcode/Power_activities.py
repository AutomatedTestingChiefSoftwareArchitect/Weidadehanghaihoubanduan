import urllib3
import requests
import threading
from time import time
from interfaceTest.readexcel_package import readExcel

nums = 0
THREAD_NUM = 1
ONE_WORKER_NUM = 1


def test():

    global nums
    dates = readExcel.reds.get_xls('Power_activities.xlsx', 'activities')

    for user_mobile, user_token in dates:

        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, "
                                 "like Gecko) Mobile/14G60 MicroMessenger/7.0.2(0x17000222) "
                                 "NetType/WIFI Language/zh_CN",
                   "Content-Type": "application/json",
                   "userToken": user_token}
        url = "https://api.aixiangdao.com/user/getUserInfo"
        data = {}

        urllib3.disable_warnings()
        r = requests.post(url=url, data=data, headers=headers)
        if r.status_code == requests.codes.OK:
            print("%s : 助力成功~~~" % user_mobile)
        else:
            print("%s : 助力失败~~~" % user_mobile)
        nums += 1


def working():

    global ONE_WORKER_NUM
    for i in range(0, ONE_WORKER_NUM):
        test()


def tests():

    global nums
    global THREAD_NUM
    threads = []
    start_time = time()  # 开始时间

    for i in range(THREAD_NUM):
        ret = threading.Thread(target=working(), name="T" + str(i))
        ret.setDaemon(True)
        threads.append(ret)

    for ret in threads:
        ret.start()
        ret.join()

    end_time = time()  # 结束时间
    num = nums  # 请求总数
    run_time = end_time - start_time  # 总消耗时间
    one_requests_time = float(run_time) / num  # 每个请求平均消耗时间
    print("请求总数:" + str(num))
    print("开始时间：" + str(start_time))
    print("结束时间：" + str(end_time))
    print("总消耗时间：" + str(run_time) + "秒")
    print("每个请求平均消耗时间：" + str(one_requests_time) + "秒")


if __name__ == "__main__":
    tests()
