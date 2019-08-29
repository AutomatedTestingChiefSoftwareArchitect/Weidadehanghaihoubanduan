import requests
import datetime
import random


class Interface(object):

    def __init__(self):
        self.phone = None
        self.password = None
        self.cookies = None
        self.types = None
        self.ids = None
        self.list_login = []
        self.list_college = []
        self.topic_list = []
        self.topic = None
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def login_parameter(self):  # 登陆参数
        self.list_login = [15721484678, 1572148]
        for i in range(1):
            self.topic = random.choice(self.list_login)
            print(self.topic)
            return self.topic

    def college_parameter(self):  # college参数
        with open("types_ids") as f1:
            for key in f1.read().splitlines():
                self.list_college.append(key)

    def college_measurement(self):  # 测评题目参数
        with open("measurement") as f2:
            self.topic_list.append(f2.read().splitlines())
            for topic in self.topic_list:
                # 这里不return 调用时，无输出，且print无效
                # random 必须是list[list]
                return random.choice(topic)

    def login_get(self, phone, password):  # 登陆接口 获取cookie
        self.phone = phone
        self.password = password
        login_url = "https://www.review.xiaozao.org/api/user/phoneLogin?"
        querystring = {
            "regionCodeIndex": 37,
            "phone": self.phone,
            "password": self.password,
            "remember": "true"
        }
        r = requests.get(login_url, headers=self.header, params=querystring, timeout=2)
        if r.status_code == requests.codes.OK:
            self.cookies = r.cookies
            return print("successful login_get")
        else:
            raise Exception("https error: %s" % r.status_code)

    def page_get(self):  # 首页6大学院
        page_url = "https://www.review.xiaozao.org/api/roadmap-evaluation/status/2"
        ret = requests.get(page_url, headers=self.header, cookies=self.cookies, timeout=2)
        if ret.status_code == requests.codes.OK:
            return print("successful page_get")
        else:
            raise Exception("https error: %s" % ret.status_code)

    def measurement_get(self, types, ids, college):  # 获取测评题目
        self.types = types
        self.ids = ids
        requests.get("https://www.review.xiaozao.org/api/roadmap-evaluation/changeCollege/" + college,
                     headers=self.header,
                     cookies=self.cookies, timeout=1)
        measurement_url = "https://www.review.xiaozao.org/api/roadmap-evaluation/detail/" + self.types + "/" + self.ids
        re = requests.get(measurement_url, headers=self.header, cookies=self.cookies, timeout=2)
        if re.status_code == requests.codes.OK:
            return print("successful measurement_get")
        else:
            raise Exception("https error: %s" % re.status_code)

    def complete_post(self, parameter_list):  # 完成测评
        complete_url = "https://www.review.xiaozao.org/api/roadmap-evaluation/complete/" + self.types + "/" + self.ids
        get = requests.post(complete_url, headers=self.header, cookies=self.cookies, json=parameter_list, timeout=2)
        if get.status_code == requests.codes.OK:
            return print("successful complete_post")
        else:
            raise Exception("https error: %s" % get.status_code)

    def submit_get(self):  # 完成测评结果页
        submit_url = "https://www.review.xiaozao.org/api/roadmap-evaluation/result/2"
        result = requests.get(submit_url, headers=self.header, cookies=self.cookies, timeout=2)
        if result.status_code == requests.codes.OK:
            return print("successful submit_get")
        else:
            raise Exception("https error: %s" % result.status_code)

    def college_get(self):  # 分配学院case页面
        college_url = "https://www.review.xiaozao.org/api/roadmap/current-college"
        results = requests.get(college_url, headers=self.header, cookies=self.cookies, timeout=2)
        if results.status_code == requests.codes.OK:
            if results.json()["response"] is None:
                raise Exception("case 未分配: %s " % results.json()["response"])
            return print("successful college_get")
        else:
            print("https error: %s" % results.status_code)

    def target_get(self):
        rr = requests.get("https://www.review.xiaozao.org/api/roadmap/user-info", headers=self.header,
                          cookies=self.cookies, timeout=2)
        if rr.status_code == requests.codes.OK:
            if rr.json()["response"] is None:
                raise Exception("求职目标 未分配: %s " % rr.json()["response"])
            print(rr.json()["response"])
            return print("successful 求职目标")


if __name__ == '__main__':

    obj = Interface()
    print("执行时间: %s" % datetime.datetime.now())
    number = 0
    while number < 1:
        obj.login_get(obj.login_parameter(), "e71c432bc3ddaca8fc282ea7888ab8a2cd2a50d661373279ff1054a8508bffb6")
        obj.page_get()
        obj.college_parameter()
        obj.measurement_get(obj.list_college[0], obj.list_college[1], obj.list_college[2])
        obj.complete_post(
            [{"tagList": [obj.college_measurement()], "topicId": "5c05fdd7d7e0054f9bf96f64"},
             {"tagList": [obj.college_measurement()], "topicId": "5c089ab3a252072144d91c8e"},
             {"tagList": [obj.college_measurement()], "topicId": "5c089d9ea252072144d91c8f"},
             {"tagList": [obj.college_measurement()], "topicId": "5c089ea7a252072144d91c90"},
             {"tagList": [obj.college_measurement()], "topicId": "5c089ffda252072144d91c93"},
             {"tagList": ["D"], "topicId": "5c08a035a252072144d91c94"},
             {"tagList": ["3"], "topicId": "5c08a082a252072144d91c95"},
             {"tagList": ["C"], "topicId": "5c08a0c3a252072144d91c96"},
             {"tagList": ["C"], "topicId": "5c08a0c3a252072144d91c96"},
             {"tagList": ["D"], "topicId": "5c08a133a252072144d91c97"},
             {"tagList": ["C"], "topicId": "5c08a161a252072144d91c98"},
             {"tagList": ["C"], "topicId": "5c08a189a252072144d91c99"},
             {"tagList": ["D"], "topicId": "5c08a1b1a252072144d91c9a"},
             {"tagList": ["C"], "topicId": "5c10ac42f63395f5d45ee77a"},
             {"tagList": ["D"], "topicId": "5c08a1dda252072144d91c9b"},
             {"tagList": ["A"], "topicId": "5c122d2f2e966d5c3ca37d7a"}])
        obj.submit_get()
        obj.college_get()
        obj.target_get()
        # time.sleep(1)
        # obj.list_login.remove(obj.topic)
        number += 1
    print("执行次数：%s" % number, "\n"
                              "结束时间: %s" % datetime.datetime.now())

    """
            # 咨询
            obj.page_get()
            obj.measurement_get(obj.list_college[3], obj.list_college[4], obj.list_college[5])
            obj.complete_post(
                    [{"tagList": [obj.college_measurement()], "topicId": "5c05fdd7d7e0054f9bf96f64"},
                     {"tagList": [obj.college_measurement()], "topicId": "5c05fdd7d7e0054f9bf96f64"},
                     {"tagList": [obj.college_measurement()], "topicId": "5c089ab3a252072144d91c8e"},
                     {"tagList": [obj.college_measurement()], "topicId": "5c10aa1ef63395f5d45ee779"},
                     {"tagList": [obj.college_measurement()], "topicId": "5c089d9ea252072144d91c8f"},
                     {"tagList": ["C"], "topicId": "5c089ea7a252072144d91c90"},
                     {"tagList": ["D"], "topicId": "5c13456b77dbf264d7d5b414"},
                     {"tagList": ["D"], "topicId": "5c13456b77dbf264d7d5b415"},
                     {"tagList": ["D"], "topicId": "5c13456b77dbf264d7d5b416"},
                     {"tagList": ["C"], "topicId": "5c13456b77dbf264d7d5b417"},
                     {"tagList": ["4"], "topicId": "5c13456b77dbf264d7d5b418"},
                     {"tagList": ["C"], "topicId": "5c13456b77dbf264d7d5b419"},
                     {"tagList": ["B"], "topicId": "5c1345e777dbf264d7d5b41a"},
                     {"tagList": ["A"], "topicId": "5c1345e777dbf264d7d5b41b"},
                     {"tagList": ["A"], "topicId": "5c13461377dbf264d7d5b41c"},
                     {"tagList": ["B"], "topicId": "5c13462177dbf264d7d5b41d"},
                     {"tagList": ["B"], "topicId": "5c13462c77dbf264d7d5b41e"},
                     {"tagList": ["B"], "topicId": "5c13463977dbf264d7d5b41f"},
                     {"tagList": ["A"], "topicId": "5c13464577dbf264d7d5b420"},
                     {"tagList": ["A"], "topicId": "5c13465177dbf264d7d5b421"}])
            obj.submit_get()
            obj.college_get()
            """
