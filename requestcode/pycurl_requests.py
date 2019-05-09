
import pycurl


class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def test_gzip():
    t = Test()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.URL, "https://www.review.xiaozao.org/")
    c.perform()
    # http 状态码
    http_code = c.getinfo(pycurl.HTTP_CODE)

    # 远程服务器连接时间
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)

    # 连接上后到开始传输时的时间
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)

    # 接收到第一个字节的时间
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)

    # 总的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)

    # 下载速度
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
    print('http_code:  %d ' % http_code, "\n"
          'http_size:  %d ' % http_size, "\n"
          'conn_time:  %f ' % http_conn_time, "\n"
          'pre_tran :  %f ' % http_pre_tran, "\n"
          'start_tran: %f ' % http_start_tran, "\n"
          'total_time: %f ' % http_total_time)


if __name__ == '__main__':

    test_gzip()
