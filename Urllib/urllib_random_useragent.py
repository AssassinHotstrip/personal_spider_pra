import urllib.request
import random

# Cookie池
# 代理池
# User-Agent池
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1"
]


def send_request():
    # 查看http相关参数的网址
    url_list = [
        "http://www.httpbin.org/headers",
        "http://www.httpbin.org/headers",
        "http://www.httpbin.org/headers"
    ]
    # 通过urlopen直接发送的url地址请求，不能附带请求报头
    # urllib.request.urlopen(url)


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; "
                      "Trident/7.0; rv:11.0) like Gecko"
    }
    for url in url_list:
        headers["User-Agent"] = random.choice(USER_AGENT_LIST)

        # 构建一个附带请求报头的请求对象
        request = urllib.request.Request(url, headers=headers)

        response = urllib.request.urlopen(request)

        # 查看响应状态码
        print(response.getcode())

        # 查看响应的url地址
        print(response.geturl())

        # 获取响应原始编码字符串(bytes)
        yield response.read()

if __name__ == "__main__":
    for html in send_request():
        print(html)
