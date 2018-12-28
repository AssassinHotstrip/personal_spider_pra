# -*- coding: utf-8 -*-
try:
    # python2
    from urllib import unquote
except:
    # python3
    from urllib.parse import unquote

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule, CrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider


from ..items import AqiItem


class AqiRedisCrawlSpider(RedisCrawlSpider):
    name = 'aqi_crawl_spider_redis'
    allowed_domains = ['aqistudy.cn']
    base_url = "https://www.aqistudy.cn/historydata/"
    # start_urls = [base_url]
    redis_key = "aqirediscrawlspider:start_urls"
    rules = [
        # 提取每个城市的链接并发送请求, 返回的响应继续提取新的链接
        #                 正则
        Rule(LinkExtractor(allow=r"monthdata\.php\?city="), follow=True),
        # 提取每个月份的链接，并发送请求，返回的响应会通过parse-day提取该月的所有天数据，并不在提取新的链接
        Rule(LinkExtractor(allow=r"daydata\.php\?city="), callback="parse_day", follow=False)

    ]


    def parse_day(self, response):
        """解析每天的数据"""
        # 取出城市名
        # 方式一:从meta中取出城市名(使用crawlspider时无法使用meta传递数据)
        # city_name = response.meta["city"]
        # 方式二:从url中取出城市名:https://www.aqistudy.cn/historydata/daydata.php?city=%E9%98%BF%E5%9D%9D%E5%B7%9E&month=2014-12
        url = response.url
        city = unquote(url[url.find("=") + 1:url.find("&")]).decode("utf-8")

        # 取出该城市中的每天的数据
        data_list = response.xpath('//tbody/tr')
        # 去除网页中表头数据
        data_list.pop(0)

        for data in data_list:
            item = AqiItem()

            # 城市名
            item["city"] = city
            # 空气数据的日期
            item['date'] = data.xpath("./td[1]/text()").extract_first()
            # 空气质量指数
            item['aqi'] = data.xpath("./td[2]/text()").extract_first()
            # 空气质量等级
            item['level'] = data.xpath("./td[3]/span/text()").extract_first()
            # pm2.5
            item['pm2_5'] = data.xpath("./td[4]/text()").extract_first()
            # pm10
            item['pm10'] = data.xpath("./td[5]/text()").extract_first()
            # 二氧化硫
            item['so2'] = data.xpath("./td[6]/text()").extract_first()
            # 一氧化碳
            item['co'] = data.xpath("./td[7]/text()").extract_first()
            # 二氧化氮
            item['no2'] = data.xpath("./td[8]/text()").extract_first()
            # 臭氧
            item['o3'] = data.xpath("./td[9]/text()").extract_first()

            yield item
