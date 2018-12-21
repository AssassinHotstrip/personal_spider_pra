import urllib.request
import random


def send_request():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = urllib.request.Request("http://httpbin.org/ip", headers=headers)

    # 构建多个代理ip的代理池（可以是列表、本地文件、数据库，API）
    proxy_pool = [
        {"http": "http://maozhaojun:ntkn0npx@39.96.43.72:16818"},
        {}
    ]

    # 随机选择一个代理
    proxy = random.choice(proxy_pool)

    # 构建代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 使用处理器,构建自动以opener
    opener = urllib.request.build_opener(proxy_handler)
    # 使用opener发送请求,附带处理器
    response = opener.open(request)

    urllib.request.install_opener(opener)
    urllib.request.urlopen(request)

    print(response.read())


if __name__ == '__main__':
    send_request()