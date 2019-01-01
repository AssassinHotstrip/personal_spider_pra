# coding:utf-8


from ..http.request import Request
from ..http.item import Item


class Spider(object):
    """框架提供的爬虫类原型"""

    # 默认到百度
    start_urls = [
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com/"
    ]

    def start_request(self):
        # 返回第一个请求给引擎--->调度
        for start_url in self.start_urls:
            yield Request(self.start_url)

    def parse(self, response):
        data = {"url" : response.url, "status" : response.status, "content" : response.body}
        return Item(data)

