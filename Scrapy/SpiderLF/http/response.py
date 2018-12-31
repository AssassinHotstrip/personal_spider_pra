# coding:utf-8

from lxml import etree


class Response(object):
    """框架提供的响应体类, 由下载器构建响应对象"""

    def __init__(self, url, headers, body, status, encoding):
        # 响应url
        self.url = url
        # 响应报头
        self.headers = headers
        # 响应体
        self.body = body
        # 响应状态码
        self.status = status
        # 响应体的字符编码
        self.encoding = encoding


    def xpath(self, rule_str):
        """提取数据"""
        # 获取响应体数据
        html_obj = etree.HTML(self.body)
        # 过滤所需数据并返回
        return html_obj.xpath(rule_str)


