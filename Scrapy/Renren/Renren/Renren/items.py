# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenrenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 直播间url地址
    room_url = scrapy.Field()
    # 主播图片url地址
    vertical_src = scrapy.Field()
    # 主播昵称
    nickname = scrapy.Field()
    # 所在城市
    anchor_city = scrapy.Field()
    # 图片的本地磁盘路径
    image_path = scrapy.Field()
