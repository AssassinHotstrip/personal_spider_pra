import urllib.request
import urllib.parse

import json

# 重点：必须通过抓包，找到 动态页面传递数据的 文件（json、js），发送这个文件的请求即可。


def send_request():
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    start = 0
    while True:
        query_dict = {"start" : start, "limit" : 20}
        query_str = urllib.parse.urlencode(query_dict)
        full_url = base_url + query_str

        request = urllib.request.Request(full_url, headers=headers)
        response = urllib.request.urlopen(request)

        # 返回json字符串
        html = response.read()
        # json.dumps() : 将 Python数据类型 转为 Json字符串
        # json.loads() : 将 Json字符串 转为对应的 Python数据类型

        movie_list = json.loads(html)

        # 若列表为空,停止取值
        if not movie_list:
            break
        # 若不为空,继续取值
        for movie in movie_list:
            print(movie["title"], movie["score"])

        start += 20


if __name__ == '__main__':
    send_request()
