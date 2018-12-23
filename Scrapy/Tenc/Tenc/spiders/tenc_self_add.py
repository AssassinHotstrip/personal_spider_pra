# coding: utf-8

# 通过拼接url自增量的方式来处理多页(翻页)采集

from datetime import datetime

import scrapy

from ..items import TencItem


class TencSpdSpider(scrapy.Spider):
    name = 'tenc_self_add'
    allowed_domains = ['hr.tencent.com']

    page = 0
    base_url = 'https://hr.tencent.com/position.php?start={}'
    # 首次(首页)发送请求的地址
    start_urls = [base_url.format(page)]

    def parse(self, response):

        # 每页抓取的信息列表
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        # 当到最后一页时,page再自增,返回的node_list为空,此时停止迭代,退出函数
        if not node_list:
            return

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
            # 通过yield 返回item给引擎-管道处理，并继续执行下一次迭代
            yield item

        # 遍历完一次列表,换下一页
        self.page += 10  # 此网页每翻一页, 数字加10
        next_url = self.base_url.format(self.page)

        # 所有职位迭代完毕，再通过 yield 返回下一页的请求对象给引擎-调度器-下载器，下载器发送请求返回响应，交给callback指定的parse继续结束
        # 构建一个自定义请求，并指定回调函数（请求发送成功后，返回的响应将由指定的回调函数解析）
        yield scrapy.Request(url=next_url, callback=self.parse)

