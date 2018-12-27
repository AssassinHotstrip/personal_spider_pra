# coding:utf-8
# 通过请求头发送cookie

### 注意:scrapy中cookie放入headers中不生效,需要单独提出来

import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren_login"
    # allowed_domains =[]
    # start_urls= []

    def start_requests(self):
        """登录并发送登录的post请求,登录成功则记录cookie"""
        # 登录接口
        post_url = "http://www.renren.com/PLogin.do"
        form_data = {
            "email" : "670566875@qq.com",
            "password" : "rr9877"
        }
        # 发送post请求，scrapy会保存cookie，同时程序会跳转到self.parse执行后续代码
        yield scrapy.FormRequest(post_url, formdata=form_data, callback=self.parse)


    def parse(self, response):
        """直接发送好友的页面请求,scrapy会自动传递cookie"""
        # 好友url list
        urls = [
            "http://www.renren.com/893897109/profile",
            "http://www.renren.com/890297976/profile"
        ]
        # scrapy会附带之前保存的cookie，发送每个好友的url地址请求，并通过parse_page解析响应
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page)


    def parse_page(self, response):
        """处理每个好友页面的response响应"""
        title = response.xpath("//title/text()").extract_first()

        with open(title +".html", "w") as f:
            f.write(response.body)



