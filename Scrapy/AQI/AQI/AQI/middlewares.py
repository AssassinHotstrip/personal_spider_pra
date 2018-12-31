# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy.http import HtmlResponse
from selenium import webdriver
from retrying import retry


class AqiSpiderMiddleware(object):
    def __init__(self):
        # selenium+chrome默认为有界面模式
        self.driver = webdriver.Chrome()  # 浏览器支持动态页面的渲染

        # 修改chrome配置为无界面模式
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument("--headless")

        # 创建chrome浏览器，使用该配置
        # self.driver = webdriver.Chrome(options=self.options)


    #             重试次数            等待时间(ms)
    @retry(stop_max_attempt_number=20, wait_fixed=1000)
    def retry_load_page(self, request, spider):
        """页面加载重试(页面加载异常时触发)"""
        # 在页面查找指定数据，如果数据出现，则没有异常，程序正常执行
        # 在页面查找指定数据，如果数据没出现，会出现异常，异常会被retry捕获
        #   retry总共捕获20次，如果20次之后还有异常，则异常抛出给函数调用的地方
        try:
            self.driver.find_element_by_xpath("//tbody/tr[2]/td[1]")
            spider.logger.debug("{} retried {} times".format(request.url, self.count))
            self.count += 1  # 尝试抓取信息次数+1
        except:  # 直接在此捕获异常的话, retry模块就无法捕获异常, 故手动抛出异常
            raise Exception("{} page load failed".format(request))  # try中代码出现异常,手动抛出异常,让retry工作


    def process_request(self, request, spider):
        """发送请求"""
        # 判断当前请求是否是动态页面，
        # 如果if成立表示是动态页面，则自定义构建响应；如果if不成立则表示是静态页面，则让下载器处理请求返回响应(scrapy会自动将请求发给下载器,不需要做手动处理)
        if "monthdata" in request.url or "daydata" in request.url:

            # 通过chrome发送请求
            self.driver.get(request.url)

            # 隐式等待,固定等待时间让浏览器渲染(但不灵活且存在缺陷)
            # time.sleep(2)  # 给定时间让浏览器渲染页面

            # 显式等待：判断页面需要的数据是否渲染成功，如果渲染成功则构建响应返回；没有渲染成功则一直等待。
            try:
                self.count = 1  # 每个信息至少会抓取一次
                self.retry_load_page(request, spider)

                # 获取网页源码字符串(unicode)
                html = self.driver.page_source

                # 构建响应对象:
                    # 响应的url地址：response.url
                    # 响应网页原始编码字符串：response.body
                    # 响应body字符串的编码response.encoding
                    # 响应对应的请求对象：response.request
                response = HtmlResponse(
                    url=self.driver.current_url,
                    body=html.encode("utf-8"),
                    encoding="utf-8",
                    request=request
                )

                # 在下载中间件里自行处理请求，不通过下载器处理
                return response   # return返回响应, 直接处理请求并回到引擎,不经过下载器
            except Exception as e:
                # 如果retry 20次后还有异常，则接收异常并输出到日志里，通过返回request交给引擎-调度器再次重新入队列
                spider.logger.error(e)
                return request


    def __del__(self):
        self.driver.quit()
