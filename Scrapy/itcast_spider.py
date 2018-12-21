# -*- coding: utf-8 -*-
import scrapy


class ItcastSpiderSpider(scrapy.Spider):
    name = 'itcast_spider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
