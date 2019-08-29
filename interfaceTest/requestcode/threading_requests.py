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
