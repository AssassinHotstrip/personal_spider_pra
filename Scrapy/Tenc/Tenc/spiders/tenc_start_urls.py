# -*- coding: utf-8 -*-

# 提前将要加载的url放进start_urls队列中,以高并发的方式进行爬取

from datetime import datetime

import scrapy

from ..items import TencItem


class TencSpdSpider(scrapy.Spider):
    name = 'tenc_start_urls'
    allowed_domains = ['hr.tencent.com']

    # 将所有要爬取的url地址放进队列
    start_urls = ['https://hr.tencent.com/position.php?start=0' + str(page) for page in range(0, 2861, 10)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencItem()
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
            spider = self.name
            # 抓取时间
            time = str(datetime.now())

            yield item