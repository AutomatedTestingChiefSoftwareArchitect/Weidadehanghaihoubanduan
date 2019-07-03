from interfaceTest.common import Log

logger = Log.logger
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
r = requests.get("https://www.baidu.com/", headers=header)
print(r)
logger.error("hahah")
logger.info("123")