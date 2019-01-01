#coding:utf-8

from SpiderAssassin.core.spider import Spider
from SpiderAssassin.http.item import Item


class BaiduSpider(Spider):
    start_url = [
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com/"
    ]

    def parse(self, response):
        data = {"url" : response.url, "status" : response.status}
        return data