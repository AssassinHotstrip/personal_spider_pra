# coding:utf-8


from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline
from ..http.request import Request
from ..http.item import Item


class Engine(object):

    def __init__(self):
        # 构建Spider类实例对象
        self.spider = Spider()
        # 构建Schedular类实例对象
        self.schedular = Scheduler()
        # 构建Downloader类实例对象
        self.downloader = Downloader()
        # 构建Pipeline类实例对象
        self.pipeline = Pipeline()


    def start(self):
        self._start_engine()


    def _start_engine(self):
        # 调用spider的start_request方法,获取首个请求
        start_request = self.spider.start_request()
        # 将请求发送给调度器的add_request
        self.schedular.add_request(start_request)
        # 获取调度器去重后的请求
        request = self.schedular.get_request()
        # 将请求传给下载器的send_request, 并获得响应
        response = self.downloader.send_request(request)
        # 将从下载器获取的响应交给spider的parse去解析
        result = self.spider.parse(response)
        # 处理解析结果:
        ## 如果Request类型,则返回给schedular处理:
        if isinstance(result, Request):
            self.schedular.add_request(result)
        ## 如果三Iten类型,则交给管道:
        elif isinstance(result, Item):
            self.pipeline.process_item(result)
        ## 若都不是,则抛异常
        else:
            raise TypeError("Not support data type : [{}]".format(result))