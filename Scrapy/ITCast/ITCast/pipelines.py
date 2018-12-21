# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class ItcastMongoDBPipeline(object):
    # def __init__(self):
    def open_spider(self, spider):
        """爬虫启动时自动调用"""
        self.client = pymongo.MongoClient()  # 默认存到本地
        self.collection = self.client.itcast.teacher


    def process_item(self, item, spider):
        """引擎每传进来一个item就执行一次"""
        self.collection.insert(dict(item))
        return item


    # def __del__(self, spider):
    def close_spider(self, spider):
        """爬虫关闭时调用"""
        pass

