# coding:utf-8


from ..http.request import Request
from ..http.item import Item


class Spider(object):
    """框架提供的爬虫类原型"""

    # 默认到百度
    start_url = "www.baidu.com"

    def start_request(self):
        # 返回第一个请求给引擎--->调度器
        return Request(self.start_url)

    def parse(self, response):
        data = {"url" : response.url, "status" : response.status}
        return Item(data)

