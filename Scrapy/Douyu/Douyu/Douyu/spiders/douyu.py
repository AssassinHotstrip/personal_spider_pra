# -*- coding: utf-8 -*
import json

import scrapy

from ..items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']

    page = 0
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset={}'
    start_urls = [base_url.format(page)]

    def parse(self, response):
        # 返回网页数据中的"data"数据
        data_list = json.loads(response.body)["data"]

        if not data_list:
            return

        for data in data_list:
            item = DouyuItem()
            # 直播间的url地址
            item["room_url"] = "http://www.douyu.com/" + data["room_id"]
            # 图片url地址
            item["vertical_src"] = data["vertical_src"]
            # 昵称
            item["nickname"] = data["nickname"]
            # 城市
            item["anchor_city"] = data["anchor_city"]

            # 保存图片
            yield scrapy.Request(item["vertical_src"], meta={"item" : item}, callback=self.parse_image)

        self.page += 100
        yield scrapy.Request(self.base_url.format(self.page), callback=self.parse)


    def parse_image(self,response):
        item = response.meta["item"]

        filename = item['nickname'] + ".jpg"
        # 图片的路径
        item["image_path"] = "/home/python/Desktop/test/Scrapy/Douyu/Douyu/Douyu/Image/" + filename

        with open(item["image_path"], "wb") as f:
            f.write(response.body)

        yield item





