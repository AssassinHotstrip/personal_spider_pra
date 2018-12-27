# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy.http import HtmlResponse
from selenium import webdriver


class AqiSpiderMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()  # 浏览器支持动态页面的渲染

    def process_request(self, request, spider):
        self.driver.get(request.url)

        # 隐式等待,固定等待时间让浏览器渲染(但不灵活且存在缺陷)
        time.sleep(2)  # 给定时间让浏览器渲染页面

        html = self.driver.page_source

        # 构建响应对象，必须提供下面四个属性：
        # 响应的url地址：response.url
        # 响应网页原始编码字符串：response.body
        # 响应body字符串的编码response.encoding
        # 响应对应的请求对象：response.request
        response = HtmlResponse(
            url=self.driver.current_url,
            body=html.encode("utf-8"),
            encoding="utf-8",
            request=request
        )

        # 在下载中间件中自行处理请求,不通过下载器处理(return让响应直接返回到引擎,而不会调用下载器)
        return response

    def __del__(self):
        self.driver.quit()
