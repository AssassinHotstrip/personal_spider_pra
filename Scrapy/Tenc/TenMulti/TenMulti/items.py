# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html




import scrapy

######################################################
# 方式一:: 列表页(首页)数据和详情页数据 保存在同一个item对象里

class TenmultiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ### 列表页的 6个字段
    # 职位名
    position_name = scrapy.Field()
    # 详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()


    ### 详情页的 2个字段
    # 工作职责：
    position_responsibility = scrapy.Field()
    # 工作要求
    position_require = scrapy.Field()


    # 爬虫名（数据源）
    spider = scrapy.Field()
    # 抓取时间
    time = scrapy.Field()
######################################################



# 方式二:: 列表页(首页)数据和详情页数据 保存在不同item对象里
class TencmultiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ### 列表页的 6个字段
    # 职位名
    position_name = scrapy.Field()
    # 详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()

    # 爬虫名（数据源）
    spider = scrapy.Field()
    # 抓取时间
    time = scrapy.Field()


class TencmultiDetailItem(scrapy.Item):
    ### 详情页的 2个字段
    # 工作职责：
    position_responsibility = scrapy.Field()
    # 工作要求
    position_require = scrapy.Field()


    # 爬虫名（数据源）
    spider = scrapy.Field()
    # 抓取时间
    time = scrapy.Field()