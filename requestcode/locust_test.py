from locust import seq_task, TaskSet, HttpLocust
import requests


class Users(TaskSet):

    # def on_start(self):  # 每个虚拟用户执行操作时运行on_start方法，且只运行一次，可用于初始化
    # 可获取cookie，保持持续会话

    def __init__(self, parent):
        super().__init__(parent)
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.cookie = {
            "Cookie": "_ga=GA1.3.792386712.1534772274; "
                      "Hm_lvt_36a333f7223e77fe1827c502c476201c=1547120484,1547450063,1547548088,1548236545;"
                      "_gid=GA1.3.1758201518.1548671021; Hm_lvt_c8a5b25a491d11438e3da524c9928edb=1547549407; "
                      "_xa_cid=51BC66C9416F111665A2; SESSION=05521818-6cb9-4c81-8aeb-09b8981b3636; r=b2afd63c2c2259a8;"
                      "Hm_lpvt_c8a5b25a491d11438e3da524c9928edb=1548682523"}

    @seq_task(1)
    # @task(1)
    def login_first(self):  # code
        url = "/"
        with self.client.get(url, headers=self.header, cookies=self.cookie) as response:
            # catch_response = True ：布尔类型，如果设置为 True, 允许该请求被标记为失败
            if response.status_code == requests.codes.OK:
                response.success("-----------------成功进入--------------------------")
            else:
                response.failure("------------访问详情页出错啦-----------------")

    # @seq_task(2)  # 执行顺序
    # @task(1)  # 执行次数
    """
    def then_read_thread(self):  # code
        urls = "/lottery/1"
        with self.client.get(urls, headers=self.header, cookies=self.cookie) as f1:
            assert f1.status_code == 200
            # assert f1.json()["state"]["code"] == 0
            f1.success("------------------抽奖成功---------------------------")
    """
    # def on_stop(self):  # 每个虚拟用户退出时执行on_stop方法
    # pass


class WebsiteUser(HttpLocust):
    #  def setup(self):  # 每次启动locust时运行setup方法
    #  print('locust setup')

    #  def teardown(self):  # 退出时运行teardown方法
    #  print('locust teardown')

    host = "https://www.baidu.com"
    task_set = Users
    min_wait = 1000  # 执行任务之间的最短等待时间
    max_wait = 1000  # 执行任务之间的最长等待时间
    # task_set=  用于定义此协程(微线程)的执行行为
    # wait_function() 用于计算协程(微线程)执行任务之间的等待时间的函数，以毫秒为单位
    # weight= 选择协程(微线程)的可能性。重量越高，被选中的机会就越大
