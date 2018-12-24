# -*- coding: utf-8 -*-

### 爬取方式一: 列表页(首页)数据和详情页数据 保存在同一个item对象里

from datetime import datetime
import scrapy


from ..items import TenmultiItem

class TencMultiGradeSpider(scrapy.Spider):
    name = 'tenc_multi_grade'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=' + str(page) for page in range(0, 2861, 10)]


    def parse(self, response):
        """列表页解析方法"""
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TenmultiItem()
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


            # 发送一个职位详情页的请求，并指定回调函数为自定义的parse_detail (回调式处理请求的响应)
            # meta用来传递数据给callback的回调函数
            # 请求的meta属性，将做为请求对应的响应的 meta属性 传递给callback回调函数
            yield scrapy.Request(url=item['position_link'], meta={"item" : item}, callback=self.parse_detail)


    def parse_detail(self, response):
        """解析详情页的响应内容"""
        item = response.meta["item"]

        item['position_responsibility'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item['position_require'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item
