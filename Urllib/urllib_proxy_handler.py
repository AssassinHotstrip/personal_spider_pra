import urllib.request

def send_request():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib.request.Request("http://httpbin.org/ip", headers=headers)

    proxy = {"http": "http://maozhaojun:ntkn0npx@39.96.43.72:16818"}

    # 构建一个代理处理器对象
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 使用代理处理器对象,构建自定义的opener对象
    opener = urllib.request.build_opener(proxy_handler)
    # 使用opener发送请求,请求会通过之前设定的代理服务器进行转发,并返回响应
    response = opener.open(request)

    print(response.read())
