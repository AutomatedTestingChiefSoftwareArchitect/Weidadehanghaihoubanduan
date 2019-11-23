"""
import urllib3
from interfaceTest.http_package import configHttp

url = "https://dev.aisinovision.com:64431/sso/connect/token"
data = "userName=admin&password=admin&client_id=ultimo&grant_type=password&client_secret=secret"
headers = {
    "Content-Type":"application/x-www-form-urlencoded;charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}
urllib3.disable_warnings()
r = configHttp.runmain.run_main('post', url, data, headers)
print(r.json())
"""