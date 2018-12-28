# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from ..items import AqiItem


class AqiRedisSpider(RedisSpider):
    name = 'aqi_spider_redis'
    allowed_domains = ['aqistudy.cn']
    base_url = 'https://www.aqistudy.cn/historydata/'
    # start_urls = [base_url]
    redis_key = "aqiredisspider:start_urls"

    def parse(self, response):
        """解析城市列表页, 获得所有城市的链接"""
        # 所有城市的链接
        city_link_list = response.xpath('//div[@class="all"]//a/@href').extract()
        # 所有城市名字
        city_name_list = response.xpath('//div[@class="all"]//a/text()').extract()

        # 发送每个城市链接的请求，并通过meta传递城市名
        # zip()用于同时遍历多个列表
        for city_link, city_name in zip(city_link_list, city_name_list):
            yield scrapy.Request(url=self.base_url + city_link, meta={"city" : city_name}, callback=self.parse_month)


    def parse_month(self, response):
        """解析每个城市的月份链接"""
        month_link_list = response.xpath('//tbody//tr//a/@href').extract()

        # 发送每个月的链接的请求，并通过meta传递城市名
        for month_link in month_link_list:
            yield scrapy.Request(url=self.base_url + month_link, meta=response.meta, callback=self.parse_day)


    def parse_day(self, response):
        """解析每天的数据"""
        # 取出城市名
        # 方式一:从meta中取出城市名
        city_name = response.meta["city"]
        # 方式二:从url中取出城市名:https://www.aqistudy.cn/historydata/daydata.php?city=%E9%98%BF%E5%9D%9D%E5%B7%9E&month=2014-12
        # try:
        #     # python2
        #     from urllib import unquote
        # except:
        #     # python3
        #     from urllib.parse import unquote
        # url = response.url
        # city = unquote(url[url.find("=") + 1:url.find("&")]).decode("utf-8")


        # 取出该城市中的每天的数据
        data_list = response.xpath('//tbody/tr')
        # 去除网页中表头数据
        data_list.pop(0)


        for data in data_list:
            item = AqiItem()

            # 城市名
            item["city"] = city_name
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