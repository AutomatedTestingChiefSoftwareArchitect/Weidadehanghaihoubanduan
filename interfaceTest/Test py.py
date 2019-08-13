import requests

url = "https://api.aixiangdao.com/getCityTopics"
data = {"cityId":"29"}
headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, "
                          "like Gecko) Mobile/14G60 MicroMessenger/7.0.2(0x17000222) NetType/WIFI Language/zh_CN",
            "platform": "miniApp",
            "userToken": "e751ed59-6485-4387-8dbf-425f0c635505"
        }

r = requests.post(url, data, headers=headers)
print(r.json())