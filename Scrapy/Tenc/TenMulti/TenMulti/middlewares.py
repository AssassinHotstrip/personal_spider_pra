# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import requests

from fake_useragent import UserAgent

from .settings import USER_AGENT_LIST

class RandomUserAgentMiddleware(object):
    """随机选择UserAgent"""
    def __init__(self):
        self.ua_obj = UserAgent()

    def process_request(self, request, spider):

        # 在settings中提前存好useragent列表,并随机从中获取一个useragent
        # user_agent = random.choice(USER_AGENT_LIST)

        # 使用fake_useragent模块(第三方)来随机生成useragent
        user_agent = self.ua_obj.random
        request.headers["UserAgent"] = user_agent
        print("_*-" * 10)
        print(request.headers)

        # 在中间件中不要写return操作,不然request会一直在请求队列和中间件之间来回
        # return request





class RandomProxyMiddleware(object):
    def __init__(self):
        self.proxy_url = "http://kps.kdlapi.com/api/getkps/?orderid=914194268627142&num=1&pt=1&sep=1"  # 使用的代理的url,实际情况中需有多个代理
        self.proxy_list = [requests.get(self.proxy_url).content]
        self.count = 0

    def process_request(self, request, spider):
        # 设置每爬多少次就换一次代理(根据被爬取网页的情况而定)
        if self.count < 20:
            proxy = random.choice(self.proxy_list)
            #  代理通过meta添加               代理url账号: 密码
            request.meta['proxy'] = "http://mzj:ntkn0npx@" + str(proxy)

            self.count += 1
        else:
            self.proxy_list = [requests.get(self.proxy_url).content]
            self.count = 0
