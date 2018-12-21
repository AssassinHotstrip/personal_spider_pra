import urllib.request

def send_request():
    # 查看http相关参数的网址
    url = "http://www.httpbin.org/headers"

    # 通过urlopen直接发送的url地址请求，不能附带请求报头
    # urllib.request.urlopen(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    }

    # 构建一个附带请求报头的请求对象
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    # 获取响应原始编码字符串(bytes)
    return response.read()
if __name__ == "__main__":
    html = send_request()
    print(html)
