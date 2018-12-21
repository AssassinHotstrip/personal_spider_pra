# -*- coding: utf-8 -*-
# 导入scrapy
import scrapy


from ..items import BaiduItem

# 自定义一个爬虫类,继承于scrapy.Spider
class BaiduSpider(scrapy.Spider):
    # (必选)爬虫名
    name = 'baidu'
    # 允许抓取的域名范围(不指定则默认不限制)
    allowed_domains = ['baidu.com']
    # (必须)程序启动后 发送的第一批请求url地址,不需要构建请求(引擎会读取start_urls并构建每个url请求,再交给调度器保存-->下载器发送请求,返回响应-->解析)
    start_urls = ['http://www.baidu.com/', 'http://news.baidu.com/']

    def parse(self, response):
        # 创建类字典item对象
        item = BaiduItem()

        # 从响应中提取数据并返回至管道
        item["title"] = response.xpath("//title/text()").extract_first()
        item["url"] = response.url

        print(item)




