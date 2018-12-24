# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


from ..items import TencmultiItem, TencmultiDetailItem


class TencCrawlSpider(CrawlSpider):
    name = 'tenc_crawl'
    allowed_domains = ['hr.tencent.com']
    start_urls = ["https://hr.tencent.com/position.php?&start=0"]

    rules = (
        # 1. LinkExtractor 表示一种链接提取方式，allow表示正则表达式，只要链接里href值符合正则表达式，则自动提取这些链接并发送这些链接的请求
        # 2. 请求发送后返回的响应，交给callback解析, callback 表示链接请求的响应,交给callback解析(注意不能写parse)
        # 3. follow是一个bool值：
        #    -1. follow=True表示响应还会继续经过每个Rule提取新的链接，再发送请求（返回的响应还会判断follow...)
        #    -2. follow=False表示响应不会提取链接

        # 提取列表页
        Rule(LinkExtractor(allow=r"start=\d+"), callback='parse_item', follow=True),
        # 提取详情页
        Rule(LinkExtractor(allow=r"position_detail\.php\?id=\d+"), callback="parse_detail", follow=False)
    )



    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

        """ 默认列表页的解析方法"""
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencmultiItem()
            # 职位名
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            # 详情链接
            item['position_link'] = "https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            # 职位类别
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            # 招聘人数
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            # 工作地点
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            # 发布时间
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()
            # 爬虫名（数据源）
            item['spider'] = self.name
            # 抓取时间
            item['time'] = str(datetime.now())

            yield item


    def parse_detail(self, response):
        """ 解析详情页的响应内容"""
        # item = response.meta['item']

        item = TencmultiDetailItem()
        item['position_responsibility'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item['position_require'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item



