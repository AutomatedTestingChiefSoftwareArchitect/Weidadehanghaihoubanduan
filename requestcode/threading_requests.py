import requests
import threading
import datetime


class Requests(object):

    def __init__(self, page, url):
        self.page = page
        self.url = url
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.cookie = {
            "Cookie": "_ga=GA1.3.792386712.1534772274; "
                      "Hm_lvt_36a333f7223e77fe1827c502c476201c=1547120484,1547450063,1547548088,1548236545;"
                      "_gid=GA1.3.1758201518.1548671021; Hm_lvt_c8a5b25a491d11438e3da524c9928edb=1547549407; "
                      "_xa_cid=51BC66C9416F111665A2; SESSION=05521818-6cb9-4c81-8aeb-09b8981b3636; r=b2afd63c2c2259a8;"
                      "Hm_lpvt_c8a5b25a491d11438e3da524c9928edb=1548682523"
        }

    def page_get(self):
        print("---开始访问抽奖详情页---")
        page = requests.get(self.page, headers=self.header, cookies=self.cookie, timeout=1)
        page.raise_for_status()
        # page.encoding = 'utf-8'
        if page.status_code == requests.codes.OK:
            if page.json()['message'] != "成功":
                print("message error : %s" % page.json()['message'])
            print()
            print("详情页面访问成功: %s" % page.json()['message'])
        else:
            raise Exception("http error info: %s" % page.status_code)

    def interface_get(self):
        r = requests.get(self.url, headers=self.header, cookies=self.cookie, timeout=1)
        r.raise_for_status()  # 检查是否链接成功
        # r.encoding = 'utf-8'
        print("\n"
              "startTime: %s \n"
              "Success: %s OK\n"
              "Total_time: %ss\n"
              "results: %s" % (datetime.datetime.now(),  # 返回服务器当前时间
                               r.status_code,  # 返回http状态码
                               r.elapsed.total_seconds(),  # 返回请求总时间
                               r.text))  # 返回执行结果
        print()
        print("---详情页访问结束---")


if __name__ == '__main__':

    ret = Requests("https://www.baidu.com",
                   "https://www.baidu.com")
    i = 0
    while i < 1:
        i += 1
        threading.Thread(target=ret.page_get, args=()).start()
        threading.Thread(target=ret.interface_get, args=()).start()


"""

# 增加并发数和总数
import threading
from time import time
import requests
 
THREAD_NUM = 100  # 多少线程，多少请求
ONE_WORKER_NUM = 10   # 虚拟用户数
 
 
# test()此处的程序，可以替换
def test():
    r = requests.get()
    print("测试程序")
 
 
# 多线程，虚拟用户数
def working():
    global ONE_WORKER_NUM
    for i in range(0, ONE_WORKER_NUM):
        test()
 
 
def t():
    global THREAD_NUM
    Threads = []
    start_time = time()  # 开始时间
 
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working(), name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
 
    end_time = time()  # 结束时间
    num = THREAD_NUM * ONE_WORKER_NUM   # 请求总数
    run_time = end_time - start_time    # 总消耗时间
    one_requests_time = float(run_time) / num  # 每个请求平均消耗时间
    print("请求总数:" + str(num))
    print("开始时间：" + str(start_time))
    print("结束时间：" + str(end_time))
    print("总消耗时间：" + str(run_time) + "秒")
    print("每个请求平均消耗时间：" + str(one_requests_time) + "秒")
 
 
if __name__ == "__main__":
    t()

"""