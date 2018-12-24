# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from .items import TencmultiItem, TencmultiDetailItem

class TencmultiPipeline(object):
    def open_spider(self, spider):
        # 打开(新建)文件
        self.f  = open("tencent.json", "w")

    def process_item(self, item, spider):
        # item在TencmultiItem中时执行
        if isinstance(item, TencmultiItem):
            # 往文件输入数据
            json_str = json.dumps(dict(item))
            self.f.write(json_str)

        return item

    def close_spider(self, spider):
        # 关闭文件
        self.f.close()


class TencmultiDetailPipeline(object):
    def open_spider(self, spider):
        self.f  = open("position.json", "w")

    def process_item(self, item, spider):
        # item在TencmultiDetailItem中时执行
        if isinstance(item, TencmultiDetailItem):
            json_str = json.dumps(dict(item))
            self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()

